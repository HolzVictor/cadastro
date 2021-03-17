import mysql.connector
from leitores import *

con = mysql.connector.connect(host='localhost', user='root', password='HORIPEDES')
cursor = con.cursor()


def useBanco():
    cursor.execute('use registros;')

