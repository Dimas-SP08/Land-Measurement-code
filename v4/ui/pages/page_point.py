'''Point input page UI setup.

This page is for entering:
- Number of measurement points
- Initial AMSL (Above Mean Sea Level) value

Features:
- Input validation (only numbers allowed)
- Warning messages for invalid inputs
- Next button that activates only when inputs are valid
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_point(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(600, 600))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.judultitle = QtWidgets.QLabel(Form)
        self.judultitle.setMinimumSize(QtCore.QSize(50, 40))
        self.judultitle.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.judultitle.setFont(font)
        self.judultitle.setAlignment(QtCore.Qt.AlignCenter)
        self.judultitle.setObjectName("judultitle")
        self.verticalLayout_2.addWidget(self.judultitle)
        self.groupinput = QtWidgets.QGroupBox(Form)
        self.groupinput.setMaximumSize(QtCore.QSize(16666, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupinput.setFont(font)
        self.groupinput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupinput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupinput.setObjectName("groupinput")
        self.gridLayout = QtWidgets.QGridLayout(self.groupinput)
        self.gridLayout.setContentsMargins(90, 50, 90, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.points_Lb = QtWidgets.QLabel(self.groupinput)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.points_Lb.setFont(font)
        self.points_Lb.setObjectName("points_Lb")
        self.gridLayout.addWidget(self.points_Lb, 0, 0, 1, 1)
        self.warning_point = QtWidgets.QLabel(self.groupinput)
        self.warning_point.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.warning_point.setFont(font)
        self.warning_point.setObjectName("warning_point")
        self.gridLayout.addWidget(self.warning_point, 6, 1, 1, 1)
        self.points_inp = QtWidgets.QLineEdit(self.groupinput)
        self.points_inp.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.points_inp.setFont(font)
        self.points_inp.setAlignment(QtCore.Qt.AlignCenter)
        self.points_inp.setObjectName("points_inp")
        self.points_inp.setValidator(QtGui.QIntValidator(0,99))
        self.points_inp.inputRejected.connect(self.point_)
        self.points_inp.textChanged.connect(self.reset_LP)
        self.points_inp.textChanged.connect(self.act_btn)
        self.points_inp.returnPressed.connect(self.focus_next_child)
        self.gridLayout.addWidget(self.points_inp, 0, 1, 1, 1)
        self.warning_amsl = QtWidgets.QLabel(self.groupinput)
        self.warning_amsl.setEnabled(False)
        self.gridLayout.addWidget(self.warning_amsl, 9, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.warning_amsl.setFont(font)
        self.warning_amsl.setObjectName("warning_amsl")
        self.amsl_lb = QtWidgets.QLabel(self.groupinput)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.amsl_lb.setFont(font)
        self.amsl_lb.setObjectName("amsl_lb")
        self.gridLayout.addWidget(self.amsl_lb, 7, 0, 1, 1)
        self.amsl_inp = QtWidgets.QLineEdit(self.groupinput)
        self.amsl_inp.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.amsl_inp.setFont(font)
        self.amsl_inp.setAlignment(QtCore.Qt.AlignCenter)
        self.amsl_inp.setObjectName("amsl_inp")
        self.amsl_inp.setValidator(QtGui.QDoubleValidator())
        self.amsl_inp.inputRejected.connect(self.amsl_)
        self.amsl_inp.textChanged.connect(self.reset_LA)
        self.amsl_inp.textChanged.connect(self.act_btn)
        self.gridLayout.addWidget(self.amsl_inp, 7, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupinput)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_next = QtWidgets.QPushButton(self.frame)
        self.btn_next.setEnabled(False)
        self.btn_next.setMaximumSize(QtCore.QSize(100, 20))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HAL 2"))
        self.judultitle.setText(_translate("Form", "LAND MEASUREMENT"))
        self.groupinput.setTitle(_translate("Form", "Input Number of Points and AMSL"))
        self.points_Lb.setText(_translate("Form", "How Many Points All There :"))
        self.warning_amsl.setText(_translate("Form", "Must be an integer or decimal and maks 10 digit !"))
        self.warning_point.setText(_translate("Form", "Must be an integer and maks 10 digit !"))
        self.amsl_lb.setText(_translate("Form", "Enter AMSL (m)                   :"))
        self.btn_next.setText(_translate("Form", "NEXT"))

    def focus_next_child(self):
        self.amsl_inp.setFocus()
                    
    def act_btn(self):
        self.btn_next.setEnabled(
            bool(self.points_inp.text().strip()) and 
            bool(self.amsl_inp.text().strip())
        )

    def reset_LP(self):
        self.warning_point.setStyleSheet("color: black;")
        self.warning_point.setEnabled(False)

    def reset_LA(self):
        self.warning_amsl.setStyleSheet("color: black;")
        self.warning_amsl.setEnabled(False)
      
    def point_(self):
        self.warning_point.setEnabled(True)
        self.warning_point.setStyleSheet("color: red;")
        
    def amsl_(self):
        self.warning_amsl.setEnabled(True)
        self.warning_amsl.setStyleSheet("color: red;")



