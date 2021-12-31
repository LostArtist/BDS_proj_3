import psycopg2
from PyQt5.QtWidgets import QMessageBox
from config import host, user, pas, db_name

def test(query):

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=pas,
        database=db_name
    )
    print("ok")
    cursor = connection.cursor()
    sql = query
    # i = int(input("Choose the type of operation: "))
    # print (i)
    # if i == 1:
    #     print("Write a SELECT statement:")
    print(query)

    if 'SELECT' not in sql:
        msg = QMessageBox()
        msg.setWindowTitle("Query")
        msg.setText("Wrong query")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        return 1
    cursor.execute(sql)
    connection.commit()
    crst = cursor.fetchall()
    msg = QMessageBox()
    msg.setWindowTitle("Query result")
    msg.setText(crst)
    msg.exec_()

