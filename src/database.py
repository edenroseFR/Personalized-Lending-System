import mysql.connector as mysql

database = mysql.connect(
    host='localhost',
    user='root',
    password='edenrose',
    database='lending_information'
)

cursor = database.cursor()

def borrowers_name(query = 'SELECT id, first_name, middle_name, last_name from creditors'):

    ''' This function will return all the borrowers' full_name in list structure '''

    cursor.execute(query)
    borrowers = cursor.fetchall()
    name_of_borrowers = []

    for i in borrowers:
        name = str(list(i)[0])+ list(i)[1] + ' ' + list(i)[2] + ' ' + list(i)[3]
        name_of_borrowers.append(name)

    return name_of_borrowers


def searched_names(key=None):
    borrowers = borrowers_name()
    selected_borrowers = []
    for i in borrowers:
        if key.lower() in i.lower():
            selected_borrowers.append(i)

    return selected_borrowers

def get_address(person=None):
    cursor.execute('SELECT purok FROM creditors WHERE id=%d' % person)
    purok = cursor.fetchall()
    purok = purok[0][0]
    return purok

def addCreditor(first=None, middle=None, last=None, purok=None, barangay=None, municipality=None):
    cursor.execute('''
    INSERT INTO creditors (first_name, middle_name, last_name, purok, barangay, municipality)
    VALUES ('%s','%s','%s','%s','%s','%s')
    ''' %(first,middle,last,purok,barangay,municipality))

    database.commit()
    return

def lastInsertedID():
    cursor.execute('SELECT last_insert_id()')
    return int(cursor.fetchone()[0])

def attendeeID(name=None):
    cursor.execute("SELECT id FROM attendees WHERE full_name = '%s'" % name)
    return int(cursor.fetchone()[0])


def getAttendees():
    cursor.execute('SELECT full_name FROM attendees')
    attendees = cursor.fetchall()
    attendees = [i[0] for i in attendees]
    return attendees

def record_borrowed_money(amount=None, interest=None,
                          date=None, creditorID=None, attendeeID=None):
    cursor.execute('''
    INSERT INTO credits (name, quantity, price_or_amount, interest, date, creditor_id, attendee_id)
    VALUES ('cash', 1, %d,%d,'%s',%d,%d)
    ''' %(amount,interest,date,creditorID,attendeeID))

    database.commit()

def record_borrowed_item(name=None, quantity=None, price_or_amount=None, date=None,
                         creditorID=None, attendeeID=None):
    cursor.execute('''
    INSERT INTO credits (name, quantity, price_or_amount, interest, date, creditor_id, attendee_id)
    VALUES ('%s',%d, %d,%d,'%s',%d,%d)
    ''' %(name, quantity,price_or_amount,0,date,creditorID,attendeeID))

    database.commit()


def creditorHistory(ID=None):
    cursor.execute('''
    SELECT c.id, c.name, c.price_or_amount, c.date, a.full_name FROM credits c
    JOIN attendees a ON c.attendee_id = a.id
    WHERE creditor_id = %d
    ORDER BY date ASC
    ''' %(ID))

    history = [list(i) for i in cursor.fetchall()]
    payments = paymentHistory(ID)
    history = history+payments

    return history

def paymentHistory(ID=None):
    cursor.execute('''
    SELECT p.id, p.amount, p.date, a.full_name FROM payment p
    JOIN attendees a 
    ON p.attendee_id = a.id
    WHERE p.creditor_id = %d
    ORDER BY p.date ASC
    '''%ID)

    res = cursor.fetchall()
    res = [list(i) for i in res]
    res = [[i[0],i[1], i[2], i[3]] for i in res]
    return res



def getCreditInformation(creditID=None):
    cursor.execute('''
    select c.name, c.quantity, c.price_or_amount, c.interest, c.date, a.full_name FROM credits c
    JOIN attendees a
    ON c.attendee_id = a.id
    WHERE c.id = %d
    ''' %creditID)

    name, quantity, amount, interest, date, attendee= cursor.fetchone()
    return {'name':name,'quantity':quantity,'amount':amount,'interest':interest,'date':date,'attendee':attendee}


def updateCreditInfo(creditID=None,data=None):
    cursor.execute('''
    UPDATE credits
    SET name='%s', quantity=%d, price_or_amount=%d, interest=%d, date='%s', attendee_id=%d
    WHERE id=%d
    ''' %(data['name'], data['quantity'], data['amount'], data['interest'], data['date'], data['attendee'], creditID))

    database.commit()


def deleteCredit(creditID=None):
    cursor.execute('''
    DELETE FROM credits WHERE id=%d
    '''% creditID)

    database.commit()


def get_paidAmount(ID=None):
    cursor.execute('''
    SELECT TRIM(sum(amount))+0 FROM payment
    WHERE creditor_id = %d
    '''%ID)

    res = str(cursor.fetchone())
    res = res[1:-2]
    try:
        return float(res)
    except:
        return 0


def allCreditorInfo():
    cursor.execute('''
    SELECT * FROM creditors
    ''')

    res = cursor.fetchall()
    res = [[i[0], i[1] + ' ' + i[2] + ' ' + i[3], i[4], i[5], i[6]] for i in res]
    return res


def creditors_balance():
    cursor.execute('''
    SELECT c.id, c.first_name, c.last_name,
    trim(sum(b.price_or_amount+(b.price_or_amount*(b.interest/100))))+0 as balance,
    c.purok 
    FROM creditors c
    JOIN credits b
    ON c.id = b.creditor_id
    GROUP BY c.id
    ''')

    res = cursor.fetchall()
    res = [[i[0], i[1] + ' ' + i[2], float(i[3]), i[4]] for i in res]
    for i in res:
        i[2] = i[2] - get_paidAmount(i[0])
    return res


def sortedCollectibles(a=None):
    from mergesort import mergeSort

    data = creditors_balance()
    sortedData = []
    if a =='amount':
        amount = [i[2] for i in data]
        sortedAmount = mergeSort(amount)

        for amount in sortedAmount:
            for person in data:
                if amount == person[2]:
                    sortedData.append(person)
                    data.remove(person)

    elif a == 'address':
        address = [i[3] for i in data]
        sortedAddress = mergeSort(address)

        for address in sortedAddress:
            for person in data:
                if address == person[3]:
                    sortedData.append(person)
                    data.remove(person)

    return sortedData


def getBalance(creditorID = None):
    borrowers = creditors_balance()
    for i in borrowers:
        if creditorID == i[0]:
            return i[2]


def allCreditors():
    cursor.execute('''
    SELECT id FROM creditors
    ''')

    return len(cursor.fetchall())


def getCreditorInformation(ID=None):
    cursor.execute('''
    SELECT * FROM creditors
    WHERE id = %d
    ''' %ID)

    return list(cursor.fetchone())


def updateCreditorInformation(ID=None, newData=None):
    cursor.execute('''
    UPDATE creditors
    SET first_name = '%s', middle_name = '%s', last_name = '%s', purok = '%s', barangay = '%s', municipality = '%s'
    WHERE id = %d
    ''' % (newData['first'], newData['middle'], newData['last'],
           newData['purok'], newData['barangay'], newData['municipality'], ID))

    database.commit()


def getFullName(id=None):
    cursor.execute('''
    SELECT first_name, middle_name, last_name FROM creditors
    WHERE id = %d
    ''' %id)

    first, middle, last = cursor.fetchone()
    return first + ' ' + middle + ' ' + last


def deleteCreditor(id=None):
    cursor.execute('''
    DELETE FROM creditors
    WHERE id = %d
    ''' % id)

    database.commit()


def recordPayment(amount=None, date=None, creditorID=None, attendeeID=None):
    cursor.execute('''
    INSERT INTO payment (amount, date, creditor_id, attendee_id)
    VALUES(%d, '%s', %d, %d)
    ''' %(amount, date, creditorID, attendeeID))

    database.commit()


def getSearchResult(input=None, table=None):
    inp = input.lower()
    result = []

    if table == 'collectible':
        data = creditors_balance()
        for person in data:
            j = [person[1].lower(), person[3].lower()]
            for item in j:
                if inp in item:
                    result.append(person)


    elif table == 'borrowers':
        data = allCreditorInfo()
        for person in data:
            j = [person[1].lower(), person[2].lower(), person[3].lower(), person[4].lower()]
            for item in j:
                if inp in item:
                    result.append(person)

    elif table == 'payments':
        data = payments()
        for person in data:
            j = [person[0].lower(), person[3].lower()]
            for item in j:
                if inp in item:
                    result.append(person)

    return result


def payments():
    cursor.execute('''
    SELECT c.first_name, c.middle_name, c.last_name, p.amount, p.date, a.full_name 
    FROM payment p
    JOIN creditors c on p.creditor_id = c.id
    JOIN attendees a on p.attendee_id = a.id
    ''')

    res = cursor.fetchall()
    res = [[i[0] + ' ' + i[1] + ' ' + i[2], i[3], i[4].strftime('%Y, %B %d'), i[5]] for i in res]

    return res


def getDues():
    import datetime

    cursor.execute('''
    SELECT c.first_name, c.middle_name, c.last_name, i.name, i.date
    FROM credits i
    JOIN creditors c
    ON i.creditor_id = c.id
    ''')

    res = cursor.fetchall()
    res = [list(i) for i in res]
    due = []
    dateToday = datetime.date.today()

    for i in res:
        daysPassed = dateToday - i[4]
        daysPassed = int(daysPassed.days)
        if (daysPassed) == 30:
            due.append(i)

    return due


