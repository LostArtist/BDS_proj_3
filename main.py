import psycopg2
from config import host, user, pas, db_name
import sys
from psycopg2 import Error
import cv2
import pickle
import struct
from cryptography import fernet
from PyQt5 import QtCore, QtGui, QtWidgets
import rsa
import hashlib
from des_LoginForm import *
from des_MainForm_Layout_Widgets import *
from des_MainForm_GraphicsView import *
from des_QueryForm import *
from query import *
import db_check

#  Generate keys

# def generate_keys():
#     (pubKey, privKey) = rsa.newkeys(1024)
#     with open('key/pubKey.pem', "wb") as f:
#         f.write(pubKey.save_pkcs1("PEM"))
#
#     with open('key/privKey.pem', "wb") as f:
#         f.write(privKey.save_pkcs1("PEM"))
#
# def load_keys():
#     with open('key/pubKey.pem', "rb") as f:
#         pubKey = rsa.PublicKey.load_pkcs1(f.read())
#
#     with open('key/privKey.pem', "rb") as f:
#         privKey = rsa.PrivateKey.load_pkcs1(f.read())
#
#     return pubKey, privKey
# generate_keys()
# (pubKey,privKey) = load_keys()


# class MainForm(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainForm()
#         self.ui.setupUi(self)

class LoginForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

class QueryForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QueryForm()
        self.ui.setupUi(self)


def one_click_reg():
    login = LoginForm.ui.lineEdit.text()
    password = LoginForm.ui.lineEdit_2.text()
    db_check.db_reg(login, password)


def one_click_log():
    login = LoginForm.ui.lineEdit.text()
    password = LoginForm.ui.lineEdit_2.text()

    if db_check.db_login(login, password) == 1:
        LoginForm.close()
        print('Logging succesful')
        QueryForm.show()

def one_click_query():
    query = QueryForm.ui.lineQ.text()
    query.test(query)
    print("ne ok")
    query.crud(query)
    QueryForm.show()

                    #This part of the code works, but does not apply to the GUI-task

# def crud():
#
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=pas,
#         database=db_name
#     )
#     cursor = connection.cursor()
#
#     print("1. SELECT\n"
#           "2. INSERT\n"
#           "3. UPDATE\n"
#           "4. DELETE\n"
#           "5. EXIT"
#           )
#
#     i = int(input("Choose the type of operation: "))
#     print (i)
#     if i == 1:
#         print("Write a SELECT statement:")
#         try:
#             sql = QueryForm.ui.lineEdit.text()
#             if 'SELECT' not in sql:
#                 print('Wrong query. Try again')
#                 crud()
#             cursor.execute(sql)
#             connection.commit()
#             crst = cursor.fetchall()
#             print(crst)
#         except: ValueError
#         crud()
#     elif i == 2:
#         print("Write a INSERT statement:")
#         try:
#             sql = QueryForm.ui.lineEdit.text()
#             if 'INSERT' not in sql:
#                 print('Wrong query. Try again')
#                 crud()
#             cursor.execute(sql)
#             connection.commit()
#             crst = cursor.fetchall()
#             print(crst)
#         except: ValueError
#         crud()
#     elif i == 3:
#         print("Write a UPDATE statement:")
#         try:
#             sql = input()
#             if 'UPDATE' not in sql:
#                 print('Wrong query. Try again')
#                 crud()
#             cursor.execute(sql)
#             connection.commit()
#             crst = cursor.fetchall()
#             print(crst)
#         except: ValueError
#         crud()
#     elif i == 4:
#         print("Write a DELETE statement:")
#         try:
#             sql = input()
#             if 'DELETE' not in sql:
#                 print('Wrong query. Try again')
#                 crud()
#             cursor.execute(sql)
#             connection.commit()
#             crst = cursor.fetchall()
#             print(crst)
#         except:
#             ValueError
#         crud()
#     elif i == 5:
#         connection.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = LoginForm()
    QueryForm = QueryForm()
    LoginForm.show()
    LoginForm.ui.pushButton.clicked.connect(one_click_reg)
    LoginForm.ui.pushButton_2.clicked.connect(one_click_log)
    # QueryForm.show()
    QueryForm.ui.pushButton_q.clicked.connect(one_click_query)
# try:
#      # Connection to exist database
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         password=pas,
#         database=db_name
#     )
#
#     # the cursor for performing database operations
#
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT * FROM car_service.cars;"
#         )
#         print(f"Result: {cursor.fetchall()}")
#
# except Exception as _ex:
#     print("[INFO] Error while working with PostgreSQL.", _ex)
# finally:
#      if not connection:
#          connection.close()
#          print("[INFO] PostgreSQL connection closed ")

sys.exit(app.exec())