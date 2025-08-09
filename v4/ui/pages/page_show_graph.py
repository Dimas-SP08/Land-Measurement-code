'''Graph display page UI setup.

This page shows:
- Visualization of elevation data
- Navigation buttons

Graph types:
1. Elevation profile
2. Height difference
3. Distance vs elevation scatter plot
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_show_graph(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setMaximumSize(QtCore.QSize(600, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QLabel(self.widget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout_2.addWidget(self.header)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.verticalLayout_2.addWidget(self.label)
        self.frame_btn = QtWidgets.QFrame(self.widget)
        self.frame_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.frame_btn)
        self.back.setMaximumSize(QtCore.QSize(100, 16777215))
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.next = QtWidgets.QPushButton(self.frame_btn)
        self.next.setMaximumSize(QtCore.QSize(100, 16777215))
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayout_2.addWidget(self.frame_btn)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "RESULT OF GRAPHIC"))
        self.back.setText(_translate("Form", "← BACK"))
        self.next.setText(_translate("Form", "NEXT →"))



    
