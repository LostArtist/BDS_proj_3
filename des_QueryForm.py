from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QueryForm(object):
    def setupUi(self, QueryForm):
        QueryForm.setObjectName("QueryForm")
        QueryForm.resize(263, 223)
        self.layoutWidget = QtWidgets.QWidget(QueryForm)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineQ = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineQ.setObjectName("lineQ")
        self.verticalLayout.addWidget(self.lineQ)
        self.pushButton_q = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_q.setObjectName("pushButton_q")
        self.verticalLayout.addWidget(self.pushButton_q)

        self.retranslateUi(QueryForm)
        QtCore.QMetaObject.connectSlotsByName(QueryForm)

    def retranslateUi(self, QueryForm):
        _translate = QtCore.QCoreApplication.translate
        QueryForm.setWindowTitle(_translate("QueryForm", "Form"))
        self.lineQ.setPlaceholderText(_translate("QueryForm", "Query"))
        self.pushButton_q.setText(_translate("QueryForm", "Proceed"))
