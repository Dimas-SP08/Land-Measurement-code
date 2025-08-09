'''Thread measurement input page UI setup.

This page is for entering:
- Backsight measurements (top, mid, bottom)
- Foresight measurements (top, mid, bottom)
- Distance between points

Features:
- Input validation (only numbers allowed)
- Dynamic button activation
- Navigation between multiple point pages
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_thread(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QLabel(self.widget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout_2.addWidget(self.header)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.top_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.top_1.setFont(font)
        self.top_1.setObjectName("top_1")
        self.gridLayout_2.addWidget(self.top_1, 0, 0, 1, 1)
        self.inp_t1 = QtWidgets.QLineEdit(self.groupBox)
        self.inp_t1.setObjectName("inp_t1")
        self.gridLayout_2.addWidget(self.inp_t1, 0, 1, 1, 1)
        self.mid_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mid_1.setFont(font)
        self.mid_1.setObjectName("mid_1")
        self.gridLayout_2.addWidget(self.mid_1, 1, 0, 1, 1)
        self.inp_m1 = QtWidgets.QLineEdit(self.groupBox)
        self.inp_m1.setObjectName("inp_m1")
        self.gridLayout_2.addWidget(self.inp_m1, 1, 1, 1, 1)
        self.bottom_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bottom_1.setFont(font)
        self.bottom_1.setObjectName("bottom_1")
        self.gridLayout_2.addWidget(self.bottom_1, 2, 0, 1, 1)
        self.inp_b1 = QtWidgets.QLineEdit(self.groupBox)
        self.inp_b1.setObjectName("inp_b1")
        self.gridLayout_2.addWidget(self.inp_b1, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.top_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.top_2.setFont(font)
        self.top_2.setObjectName("top_2")
        self.gridLayout.addWidget(self.top_2, 0, 0, 1, 1)
        self.inp_t1_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_t1_2.setObjectName("inp_t1_2")
        self.gridLayout.addWidget(self.inp_t1_2, 0, 1, 1, 1)
        self.mid_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mid_2.setFont(font)
        self.mid_2.setObjectName("mid_2")
        self.gridLayout.addWidget(self.mid_2, 1, 0, 1, 1)
        self.inp_m1_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_m1_2.setObjectName("inp_m1_2")
        self.gridLayout.addWidget(self.inp_m1_2, 1, 1, 1, 1)
        self.bottom_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bottom_2.setFont(font)
        self.bottom_2.setObjectName("bottom_2")
        self.gridLayout.addWidget(self.bottom_2, 2, 0, 1, 1)
        self.inp_b1_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_b1_2.setObjectName("inp_b1_2")
        self.gridLayout.addWidget(self.inp_b1_2, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Ld = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Ld.setFont(font)
        self.Ld.setObjectName("Ld")
        self.gridLayout_3.addWidget(self.Ld, 0, 0, 1, 1)
        self.Id = QtWidgets.QLineEdit(self.groupBox_3)
        self.Id.setObjectName("Id")
        self.gridLayout_3.addWidget(self.Id, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.frame_btn = QtWidgets.QFrame(self.widget)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.maximumSize
        self.back = QtWidgets.QPushButton(self.frame_btn)
        self.back.setObjectName("back")
        self.back.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout.addWidget(self.back)
        self.finish = QtWidgets.QPushButton(self.frame_btn)
        self.finish.hide()
        self.finish.setEnabled(False)
        self.finish.setObjectName("finish")
        self.finish.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout.addWidget(self.finish)
        self.next = QtWidgets.QPushButton(self.frame_btn)
        self.next.setObjectName("next")
        self.next.setMaximumSize(QtCore.QSize(100, 16777215))
        self.next.setEnabled(False)
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayout_2.addWidget(self.frame_btn)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Validator
        self.inp_t1.setValidator(QtGui.QDoubleValidator())
        self.inp_b1.setValidator(QtGui.QDoubleValidator())
        self.inp_m1.setValidator(QtGui.QDoubleValidator())
        self.inp_b1_2.setValidator(QtGui.QDoubleValidator())
        self.inp_m1_2.setValidator(QtGui.QDoubleValidator())
        self.inp_t1_2.setValidator(QtGui.QDoubleValidator())
        self.Id.setValidator(QtGui.QDoubleValidator())

        # Set Focus
        self.inp_t1.returnPressed.connect(lambda: self.focus_next_child(self.inp_t1))
        self.inp_m1.returnPressed.connect(lambda: self.focus_next_child(self.inp_m1))
        self.inp_b1.returnPressed.connect(lambda: self.focus_next_child(self.inp_b1))
        self.inp_t1_2.returnPressed.connect(lambda: self.focus_next_child(self.inp_t1_2))
        self.inp_m1_2.returnPressed.connect(lambda: self.focus_next_child(self.inp_m1_2))
        self.inp_b1_2.returnPressed.connect(lambda: self.focus_next_child(self.inp_b1_2))
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "INPUT MID THREAD"))
        self.groupBox.setTitle(_translate("Form", "(BACKSIGHT)"))
        self.top_1.setText(_translate("Form", "top, if there is'nt, enter 0"))
        self.mid_1.setText(_translate("Form", "mid"))
        self.bottom_1.setText(_translate("Form", "bottom, if there is'nt, enter 0"))
        self.groupBox_2.setTitle(_translate("Form", "(FORESIGHT)"))
        self.top_2.setText(_translate("Form", "top, if there is'nt, enter 0"))
        self.mid_2.setText(_translate("Form", "mid"))
        self.bottom_2.setText(_translate("Form", "bottom, if there is'nt, enter 0"))
        self.groupBox_3.setTitle(_translate("Form", "DISTANCES"))
        self.Ld.setText(_translate("Form", "distances (m)"))
        self.back.setText(_translate("Form", "←BACK"))
        self.finish.setText(_translate("Form", "FINISH"))
        self.next.setText(_translate("Form", "NEXT→"))
        
    def focus_next_child(self, current_field):
        focus_order = [
            self.inp_t1, self.inp_m1, self.inp_b1,
            self.inp_t1_2, self.inp_m1_2, self.inp_b1_2,
            self.Id
        ]
        
        idx = focus_order.index(current_field)
        next_field = focus_order[idx + 1]
        next_field.setFocus()
        
    def act_btn(self, ui3):
        ui3.next.setEnabled(
            bool(ui3.inp_m1.text().strip()) and 
            bool(ui3.inp_b1.text().strip()) and
            bool(ui3.inp_t1.text().strip()) and
            bool(ui3.inp_b1_2.text().strip()) and
            bool(ui3.inp_m1_2.text().strip()) and
            bool(ui3.inp_t1_2.text().strip()) and
            bool(ui3.Id.text().strip())
            )
        
    def act_btn2(self, ui3):
        if (
                bool(ui3.inp_m1.text().strip()) and 
                bool(ui3.inp_b1.text().strip()) and
                bool(ui3.inp_t1.text().strip()) and
                bool(ui3.inp_b1_2.text().strip()) and
                bool(ui3.inp_m1_2.text().strip()) and
                bool(ui3.inp_t1_2.text().strip()) and
                bool(ui3.Id.text().strip())
            ):
            ui3.finish.show()
        

        
        
        



