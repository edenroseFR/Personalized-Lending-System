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

    res = cursor.fetchall()
    res = [list(i) for i in res]
    return res



def allCreditors():
    pass
    #cursor.execute('SELECT first_name, middle_name, last_name, ')
