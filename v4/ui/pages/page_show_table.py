'''Results table display page UI setup.

This page shows:
- Measurement results in a table format
- Initial AMSL value
- Navigation buttons

The table displays:
- Point labels
- Backsight and foresight values
- Calculated elevation data
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_show_table(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.frame_3)
        self.back.setObjectName("back")
        self.back.setMaximumSize(QtCore.QSize(100, 16777215))
        self.back.setEnabled(False)
        self.horizontalLayout.addWidget(self.back)
        self.next = QtWidgets.QPushButton(self.frame_3)
        self.next.setObjectName("next")
        self.next.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout.addWidget(self.next)
        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 2)
        self.initial_amsl = QtWidgets.QLabel(Form)
        self.initial_amsl.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.initial_amsl.setFont(font)
        self.initial_amsl.setObjectName("initial_amsl")
        self.gridLayout.addWidget(self.initial_amsl, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "THE RESULT OF LAND MEASUREMENT"))
        self.back.setText(_translate("Form", "← BACK"))
        self.next.setText(_translate("Form", "NEXT →"))
        self.initial_amsl.setText(_translate("Form", "Initial AMSL: "))



