from dataclasses import field
import pandas as pd
import mysql.connector
import smtplib
from email.message import EmailMessage
import argparse

def create_csv(db_user, db_pasword,db_name,table_name):
    columns_data = []
    all_data_dict = {}
    db = mysql.connector.connect(user=db_user,password=db_pasword,database=db_name)
    cursor = db.cursor()
    query = f'select * from {table_name}'
    cursor.execute(query)
    myalldata = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for _ in range(len(field_names)):
        columns_data.append([])
    for i in range(len(field_names)):
        for j in range(len(myalldata)):
            columns_data[i].append(myalldata[j][i])
    for i in range(len(field_names)):
        all_data_dict[f'{field_names[i]}'] = columns_data[i] 
    df = pd.DataFrame(all_data_dict)
    df.to_csv('location to save')

def email_csv():
    sender_email = ''
    sender_password = ''
    receiver_email = ''
    msg = EmailMessage()
    msg['Subject'] = 'Emailing csv'
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg.set_content('Message body')

    with open('file location','rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data,maintype = 'application',subtype='octet_stream',filename = file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender_email,sender_password)
        smtp.send_message(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_username', type=str, required=True,help='Database username')
    parser.add_argument('--db_password', type=str, required=True,help='Database password')
    parser.add_argument('--db_name', type=str, required=True,help='Database name')
    parser.add_argument('--table_name', type=str, required=True,help='Table name')
    args = parser.parse_args()
    create_csv(args.db_username, args.db_password, args.db_name, args.table_name)
    email_csv()

