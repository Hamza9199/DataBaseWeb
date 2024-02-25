#import os
#import sqlite3
import mysql.connector


def ispisBaze():

    connection = mysql.connector.connect(host="localhost", user="root", password="root", database="projekat")
    #conn = sqlite3.connect('baza1.sqlite')

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM baza1")

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records
