from utils import mergeSort
import datetime
from config import database, cursor


def borrowers_name(query=None):
    if not query:
        query = f'''
            SELECT id, 
                   first_name, 
                   middle_name, 
                   last_name 
            from creditors
        '''
    cursor.execute(query)
    borrowers = cursor.fetchall()
    name_of_borrowers = []

    for i in borrowers:
        nameWithID = str(list(i)[0]) + list(i)[1] + ' ' + list(i)[2] + ' ' + list(i)[3]
        name_of_borrowers.append(nameWithID)

    return name_of_borrowers


def searched_names(key=None):
    borrowers = borrowers_name()
    selected_borrowers = []
    for name in borrowers:
        if key.lower() in name.lower():
            selected_borrowers.append(name)

    return selected_borrowers


def get_address(person=None):
    query = f'''
        SELECT purok 
        FROM creditors 
        WHERE id={person}
    '''
    cursor.execute(query)
    purok = cursor.fetchall()
    purok = purok[0][0]
    return purok


def addCreditor(first=None, middle=None, last=None, purok=None, barangay=None, municipality=None):
    query = f'''
        INSERT INTO creditors (
            first_name, 
            middle_name, 
            last_name, 
            purok, 
            barangay, 
            municipality
        )
        VALUES (
            '{first}',
            '{middle}',
            '{last}',
            '{purok}',
            '{barangay}',
            '{municipality}'
        )
    '''
    cursor.execute(query)
    database.commit()
    return


def lastInsertedID():
    query = f'''
        SELECT last_insert_id()
    '''
    cursor.execute(query)
    last_ID = int(cursor.fetchone()[0])
    return last_ID


def attendeeID(name=None):
    query = f'''
        SELECT id 
        FROM attendees 
        WHERE full_name = '{name}'
    '''
    cursor.execute(query)
    attendee_id = int(cursor.fetchone()[0])
    return attendee_id


def getAttendees():
    query = f'''
        SELECT full_name 
        FROM attendees
    '''
    cursor.execute(query)
    attendees = cursor.fetchall()
    attendees = [i[0] for i in attendees]
    return attendees


def record_borrowed_money(amount=None, 
                          interest=None,
                          date=None,
                          creditorID=None, 
                          attendeeID=None):
    query = f'''
        INSERT INTO credits (
            name, 
            quantity, 
            price_or_amount, 
            interest, 
            date, 
            creditor_id, 
            attendee_id
        )
        VALUES (
            'cash', 
            1, 
            {amount},
            {interest},
            '{date}',
            {creditorID},
            {attendeeID}
        )
    '''
    cursor.execute(query)
    database.commit()


def record_borrowed_item(name=None, 
                         quantity=None, 
                         price_or_amount=None, 
                         date=None,
                         creditorID=None, 
                         attendeeID=None):
    query = f'''
        INSERT INTO credits (
            name, 
            quantity, 
            price_or_amount, 
            interest, 
            date, 
            creditor_id, 
            attendee_id
        )
        VALUES (
            '{name}',
            {quantity}, 
            {price_or_amount},
            0,
            '{date}',
            {creditorID},
            {attendeeID}
        )
    '''
    cursor.execute(query)
    database.commit()


def creditorHistory(ID=None):
    query = f'''
        SELECT c.id, 
               c.name, 
               c.price_or_amount, 
               c.date, 
               a.full_name 
        FROM credits c
        JOIN attendees a ON c.attendee_id = a.id
        WHERE creditor_id = {ID}
        ORDER BY date ASC
    '''
    cursor.execute(query)
    history = [list(i) for i in cursor.fetchall()]
    payments = paymentHistory(ID)
    history = history + payments
    return history


def paymentHistory(ID=None):
    query = f'''
        SELECT p.id, 
               p.amount, 
               p.date, 
               a.full_name 
        FROM payment p
        JOIN attendees a 
        ON p.attendee_id = a.id
        WHERE p.creditor_id = {ID}
        ORDER BY p.date ASC
    '''
    cursor.execute(query)
    paymentMade = cursor.fetchall()
    paymentMade = [list(i) for i in paymentMade]
    paymentMade = [[i[0], i[1], i[2], i[3]] for i in paymentMade]
    return paymentMade


def getCreditInformation(creditID=None):
    query = f'''
        SELECT c.name, 
               c.quantity, 
               c.price_or_amount, 
               c.interest, 
               c.date, 
               a.full_name 
        FROM credits c
        JOIN attendees a
        ON c.attendee_id = a.id
        WHERE c.id = {creditID}
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    name, quantity, amount, interest, date, attendee = result
    return {
        'name' : name,
        'quantity' : quantity,
        'amount' : amount,
        'interest' : interest,
        'date' : date,
        'attendee' : attendee
    }


def updateCreditInfo(creditID=None,data=None):
    query = f'''
        UPDATE credits
        SET name='{data['name']}', 
            quantity={data['quantity']}, 
            price_or_amount={data['amount']}, 
            interest={data['interest']}, 
            date='{data['date']}', 
            attendee_id={data['attendee']}
        WHERE id={creditID}
    '''
    cursor.execute(query)
    database.commit()


def deleteCredit(creditID=None):
    query = f'''
        DELETE FROM credits 
        WHERE id={creditID}
    '''
    cursor.execute(query)
    database.commit()


def get_paidAmount(ID=None):
    query = f'''
        SELECT TRIM(sum(amount))+0 
        FROM payment
        WHERE creditor_id = {ID}
    '''
    cursor.execute(query)
    paidAmount = str(cursor.fetchone())
    paidAmount = paidAmount[1:-2]

    try:
        return float(paidAmount)
    except:
        return 0


def allCreditorInfo():
    query = f'''
        SELECT * FROM creditors
    '''
    cursor.execute(query)

    listOfCreditorsInATuple = cursor.fetchall()
    listOfCreditorsInAList = [[i[0], i[1] + ' ' + i[2] + ' ' + i[3], i[4], i[5], i[6]] for i in listOfCreditorsInATuple]
    return listOfCreditorsInAList


def creditors_balance():
    query = f'''
        SELECT c.id, 
               c.first_name, 
               c.last_name,
               trim(sum(b.price_or_amount+(b.price_or_amount*(b.interest/100))))+0 as balance,
               c.purok 
        FROM creditors c
        JOIN credits b
        ON c.id = b.creditor_id
        GROUP BY c.id
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    listed_info = [[i[0], i[1] + ' ' + i[2], float(i[3]), i[4]] for i in result]
    for creditors_balance in listed_info:
        balance = creditors_balance[2] - get_paidAmount(creditors_balance[0])
        creditors_balance[2] = balance

    return listed_info


def sortedCollectibles(type=None):
    data = creditors_balance()
    print(data)
    sortedData = []

    if type == 'amount':
        amount = [i[2] for i in data]
        sortedAmount = mergeSort(amount)

        for amount in sortedAmount:
            for CreditorInfo in data:
                if amount == CreditorInfo[2]:
                    sortedData.append(CreditorInfo)
                    data.remove(CreditorInfo)

    elif type == 'address':
        address = [i[3] for i in data]
        sortedAddress = mergeSort(address)

        for address in sortedAddress:
            for CreditorInfo in data:
                if address == CreditorInfo[3]:
                    sortedData.append(CreditorInfo)
                    data.remove(CreditorInfo)

    return sortedData


def getBalance(creditorID = None):
    borrowers = creditors_balance()
    for borrower in borrowers:
        if creditorID == borrower[0]:
            return borrower[2]


def allCreditors():
    query = f'''
        SELECT id FROM creditors
    '''
    cursor.execute(query)
    all_creditor_length = len(cursor.fetchall())
    return all_creditor_length


def getCreditorInformation(ID=None):
    query = f'''
        SELECT * FROM creditors
        WHERE id = {ID}
    '''
    cursor.execute(query)
    return list(cursor.fetchone())


def updateCreditorInformation(ID=None, newData=None):
    query = f'''
        UPDATE creditors
        SET first_name = '{newData['first']}', 
            middle_name = '{newData['middle']}', 
            last_name = '{newData['last']}', 
            purok = '{newData['purok']}', 
            barangay = '{newData['barangay']}', 
            municipality = '{newData['municipality']}'
        WHERE id = {ID}
    '''
    cursor.execute(query)
    database.commit()


def getFullName(id=None):
    query = f'''
        SELECT first_name, 
               middle_name, 
               last_name 
        FROM creditors
        WHERE id = {id}
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    first, middle, last = result
    full_name = first + ' ' + middle + ' ' + last
    return full_name


def deleteCreditor(id=None):
    query = f'''
        DELETE FROM creditors
        WHERE id = {id}
    '''
    cursor.execute(query)
    database.commit()


def recordPayment(amount=None, date=None, creditorID=None, attendeeID=None):
    query = f'''
        INSERT INTO payment (
            amount, 
            date, 
            creditor_id, 
            attendee_id
        )
        VALUES(
            {amount}, 
            '{date}', 
            {creditorID}, 
            {attendeeID}
        )
    '''
    cursor.execute(query)
    database.commit()


def getSearchResult(input=None, table=None):
    userInput = input.lower()
    searchResult = []

    if table == 'collectible':
        data = creditors_balance()
        for person in data:
            creditors_info = [
                person[1].lower(), 
                person[3].lower()
            ]
            for item in creditors_info:
                if userInput in item:
                    searchResult.append(person)

    elif table == 'borrowers':
        data = allCreditorInfo()
        for person in data:
            creditors_info = [
                person[1].lower(), 
                person[2].lower(), 
                person[3].lower(), 
                person[4].lower()
            ]
            for item in creditors_info:
                if userInput in item:
                    searchResult.append(person)

    elif table == 'payments':
        data = payments()
        for person in data:
            creditors_info = [
                person[0].lower(), 
                person[3].lower()
            ]
            for item in creditors_info:
                if userInput in item:
                    searchResult.append(person)

    return searchResult


def payments():
    query = f'''
        SELECT c.first_name, 
               c.middle_name, 
               c.last_name, 
               p.amount, 
               p.date, 
               a.full_name 
        FROM payment p
        JOIN creditors c on p.creditor_id = c.id
        JOIN attendees a on p.attendee_id = a.id
    '''
    cursor.execute(query)

    result = cursor.fetchall()
    payments = []
    for p in result:
        data = [p[0] + ' ' + p[1] + ' ' + p[2], p[3], p[4].strftime('%Y, %B %d'), p[5]]
        payments.append(data)

    return payments


def getDues():
    query = f'''
        SELECT c.first_name, 
               c.middle_name, 
               c.last_name, 
               i.name, 
               i.date
        FROM credits i
        JOIN creditors c
        ON i.creditor_id = c.id
    '''
    cursor.execute(query)
    dueCredits = cursor.fetchall()
    dueCredits = [list(i) for i in dueCredits]
    dateToday = datetime.date.today()
    dues = []

    for i in dueCredits:
        daysPassed = dateToday - i[4]
        daysPassed = int(daysPassed.days)
        if (daysPassed) == 30:
            dues.append(i)

    return dues


