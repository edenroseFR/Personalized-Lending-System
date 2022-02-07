import re
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


def validEmail(email=None):
    PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(PATTERN, email)):
        return True

def SendMail(sender, content):
    email_address = os.getenv('EMAIL_ADDRESS')
    email_key = os.getenv('EMAIL_KEY')
    # Load .env file
    load_dotenv('.env')

    # Compose a message
    msg = EmailMessage()
    msg['Subject'] = 'Feedback'
    msg['From'] = 'Lending Co.'
    msg['To'] = email_address
    msg.set_content(str(content + '\n From: ' + sender))

    # Establish connection
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_address, email_key)

    # Send mail
    server.send_message(msg)
    return

def mergeSort(nlist):
    '''Code by w3resource.com
    Link: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php'''
    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

    return nlist

