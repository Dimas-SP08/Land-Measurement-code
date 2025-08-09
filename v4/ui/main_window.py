'''Main application for land measurement program.

This program helps calculate land elevation measurements using surveying techniques.

Features:
- Multi-page interface for data input
- Automatic calculations
- Data visualization
- Export options (CSV, Excel, PNG)

Usage:
1. Enter number of points and initial AMSL
2. Input measurement data for each point
3. View results in table format
4. See elevation graphs
5. Export data as needed
'''

from PyQt5 import QtWidgets,QtCore
import pandas as pd
from PyQt5.QtGui import QPixmap
import ui.pages as pages
import core as core
import utils as utils

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculation = core.Survey_CTRL()
        self.current_survey_idx = 0  
        self.list_ins = []
        self.result = []
        
        # Crate stackedwidget
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # First page (welcome screen)
        self.page1 = QtWidgets.QWidget()
        self.ui1 = pages.Ui_Form_first()
        self.ui1.setupUi(self.page1)
        self.stack.addWidget(self.page1)
        self.ui1.pushButton.clicked.connect(self.goto_input_page)
        
        # Point input page
        self.page2 = QtWidgets.QWidget()
        self.ui2 = pages.Ui_Form_point()
        self.ui2.setupUi(self.page2)
        self.stack.addWidget(self.page2)
        self.ui2.btn_next.clicked.connect(self.goto_thread_pages)
    
    def goto_input_page(self):
        self.stack.setCurrentIndex(1)
    
    # Thread measurement page
    def goto_thread_pages(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setWindowTitle("confirm")
        msg_box.setText("Are your inputs correct?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        response = msg_box.exec_()
    
        if response == QtWidgets.QMessageBox.Cancel:
            return  
        
        for i in reversed(range(self.stack.count())):
            widget = self.stack.widget(i)
            if widget not in [self.page1, self.page2]:  
                widget.deleteLater()
        self.list_ins.clear() 

        try:
                self.p = int(self.ui2.points_inp.text())
        except:
                QtWidgets.QMessageBox.warning(self, "Error", "The point must be positif number!")
                return

        for i in range(self.p):
            page3 = QtWidgets.QWidget()
            ui3 = pages.Ui_Form_thread()
            ui3.setupUi(page3)
            label,label1,label2 = self.calculation.add_point()
            ui3.groupBox.setTitle(f"{label1} (BACKSIGHT)")
            ui3.groupBox_2.setTitle(f"{label2} (FORESIGHT)")
            ui3.groupBox_3.setTitle(f"DISTANCES {label}")
            self.list_ins.append(ui3)

            if i < 1 :
                ui3.back.setEnabled(False)
                
            if i+1 != self.p :
                ui3.inp_t1.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.inp_b1.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.inp_m1.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.inp_b1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.inp_m1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.inp_t1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
                ui3.Id.textChanged.connect(lambda _, u=ui3: ui3.act_btn(u))
            
            if i+1 == self.p:
                ui3.inp_t1.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.inp_b1.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.inp_m1.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.inp_b1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.inp_m1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.inp_t1_2.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.Id.textChanged.connect(lambda _, u=ui3: ui3.act_btn2(u))
                ui3.next.setEnabled(False)
                ui3.finish.setEnabled(True)
            
            ui3.Id.returnPressed.connect(ui3.next.click)
            ui3.finish.clicked.connect(self.show_table)
            ui3.next.clicked.connect(lambda _, idx=i+2: self.next_thread_page(idx))
            ui3.back.clicked.connect(lambda _, idx=i+2: self.back_thread_page(idx))
            self.stack.addWidget(page3)
            self.calculation.ascii += 1
            self.calculation.point_group_index += 1

        self.stack.setCurrentIndex(2)
            

    # Results table page
    def show_table(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setWindowTitle("confirm")
        msg_box.setText("Are your inputs correct?")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Cancel:
            return  
        
        all_data = []
        ascii_=97
        self.amsl=float(self.ui2.amsl_inp.text().replace(",","."))
        for idx, ui3 in enumerate(self.list_ins):
            data_point = {
                'backsight': {
                    'top': ui3.inp_t1.text().replace(",","."),
                    'mid': ui3.inp_m1.text().replace(",","."),
                    'bottom': ui3.inp_b1.text().replace(",","."),
                },
                'foresight': {
                    'top': ui3.inp_t1_2.text().replace(",","."),
                    'mid': ui3.inp_m1_2.text().replace(",","."),
                    'bottom': ui3.inp_b1_2.text().replace(",","."),
                },
                'distance': ui3.Id.text().replace(",","."),
                'label':f'P{idx+1}{chr(ascii_)} - P{idx+1}{chr(ascii_+1)}'
            }
            all_data.append(data_point)
            ascii_+=1

        for data in all_data:
            try:
                # Backsight 
                t1 = float(data['backsight']['top']) if data['backsight']['top'] else 0
                m1 = float(data['backsight']['mid'])
                b1 = float(data['backsight']['bottom']) if data['backsight']['bottom'] else 0
                backsight = self.calculation.calculate_mid_thread(t1, m1, b1)

                # Foresight
                t2 = float(data['foresight']['top']) if data['foresight']['top'] else 0
                m2 = float(data['foresight']['mid'])
                b2 = float(data['foresight']['bottom']) if data['foresight']['bottom'] else 0
                foresight = self.calculation.calculate_mid_thread(t2, m2, b2)

                distances =float(data['distance'])
                labels= data['label']

                models=core.Survey_Point(labels,backsight,foresight,distances,self.amsl)
                model= models.to_dict(models.label,models.backsight,models.foresight,models.distance,models.heightdiff,models.elevation,models.status)
                self.amsl = models.elevation
                self.result.append(model)

            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Error", f"Invalid input at {data['label']}")

        page_table = QtWidgets.QWidget()
        ui_table = pages.Ui_Form_show_table()
        ui_table.setupUi(page_table)
        self.df = pd.DataFrame(self.result)
        headers = list(self.result[0].keys())

        ui_table.tableWidget.setRowCount(len(self.result))
        ui_table.tableWidget.setColumnCount(len(headers))
        ui_table.tableWidget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(self.result):
            for col_idx, header in enumerate(headers):
                value = str(row_data.get(header, ""))  
                item = QtWidgets.QTableWidgetItem(value)                
                item.setTextAlignment(QtCore.Qt.AlignCenter)           
                ui_table.tableWidget.setItem(row_idx, col_idx, item)

        ui_table.tableWidget.resizeColumnsToContents()
        ui_table.tableWidget.resizeRowsToContents()
        ui_table.initial_amsl.setText(f'Initial AMSL : {float(self.ui2.amsl_inp.text().replace(",","."))}')

        self.stack.addWidget(page_table)
        self.stack.setCurrentIndex(2+self.p)
        ui_table.next.clicked.connect(self.graph_elev)
        
    # Graph display page
    def graph_elev(self):
        graph1=utils.make_graphic_file_io(self.df)
        self.elevation_profile = graph1['elevation_profile'].getvalue()
        self.height_difference = graph1['height_difference'].getvalue()
        self.elevation_scatter = graph1['elevation_scatter'].getvalue()

        page_graph1 = QtWidgets.QWidget()
        hal_graph1 = pages.Ui_Form_show_graph()
        hal_graph1.setupUi(page_graph1)
        pixmap = QPixmap()
        pixmap.loadFromData(self.elevation_profile, format='PNG')
        hal_graph1.label.setPixmap(pixmap)
        self.stack.addWidget(page_graph1)
        self.stack.setCurrentIndex(3+self.p)
        hal_graph1.back.clicked.connect(lambda _, idx=2: self.back_graphic_display(idx))
        hal_graph1.next.clicked.connect(self.graph_height_diff)

        
    def graph_height_diff(self):
        page_graph2 = QtWidgets.QWidget()
        hal_graph2 = pages.Ui_Form_show_graph()
        hal_graph2.setupUi(page_graph2)
        pixmap = QPixmap()
        pixmap.loadFromData(self.height_difference, format='PNG')
        hal_graph2.label.setPixmap(pixmap)
        self.stack.addWidget(page_graph2)
        self.stack.setCurrentIndex(4+self.p)
        hal_graph2.back.clicked.connect(lambda _, idx=3: self.back_graphic_display(idx))
        hal_graph2.next.clicked.connect(self.distance_vs_elev)

    def distance_vs_elev(self):
        page_graph3 = QtWidgets.QWidget()
        hal_graph3 = pages.Ui_Form_show_graph()
        hal_graph3.setupUi(page_graph3)
        pixmap = QPixmap()
        pixmap.loadFromData(self.elevation_scatter, format='PNG')
        hal_graph3.label.setPixmap(pixmap)
        self.stack.addWidget(page_graph3)
        self.stack.setCurrentIndex(5+self.p)
        hal_graph3.back.clicked.connect(lambda _, idx=4: self.back_graphic_display(idx))
        hal_graph3.next.clicked.connect(self.Page_Last)

    # Final page
    def Page_Last(self):
        page_last = QtWidgets.QWidget()
        self.ui_last = pages.Ui_Form_last_page()
        self.ui_last.setupUi(page_last)
        self.stack.addWidget(page_last)
        self.stack.setCurrentIndex(6+self.p)
        self.ui_last.back.clicked.connect(lambda _, idx=5: self.back_graphic_display(idx))
        self.ui_last.closed.clicked.connect(self.close)
        self.ui_last.csv.clicked.connect(self.Export_csv)
        self.ui_last.xlsx.clicked.connect(self.Export_excel)
        self.ui_last.png.clicked.connect(self.Export_png)

    def Export_csv(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Simpan File CSV","Elevation Data.csv","CSV Files (*.csv)")
        if not file_path:
            return
        
        try:
            if not file_path.endswith('.csv'):
                file_path += '.csv'
            utils.export_to_csv(self.df,file_path)
            self.ui_last.csv.setEnabled(False)
            QtWidgets.QMessageBox.information(self, "Succes", f"The file has been created in:\n{file_path}")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to save CSV:\n{str(e)}")
    
    def Export_excel(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Simpan File Excel","Elevation Data with graphic.xlsx","Excel Files (*.xlsx)")
        
        if not file_path:
            return
        
        try:
            if not file_path.endswith('.xlsx'):
                file_path += '.xlsx'
                
            utils.export_to_excel(self.df,file_path)
            self.ui_last.xlsx.setEnabled(False)
            QtWidgets.QMessageBox.information(self, "Sukses", f"The file has been created in:\n{file_path}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to save Excel:\n{str(e)}")
    
    def Export_png(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose folder to save file","" )
        
        if not folder_path:
            return
        
        try:
            utils.make_graphic_file_user(self.df,folder_path)
            self.ui_last.png.setEnabled(False)
            QtWidgets.QMessageBox.information(self, "Sukses", f"The file has been created in:\n{folder_path}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to save PNG:\n{str(e)}")
         
    def next_thread_page(self,current_idx):
        self.stack.setCurrentIndex(current_idx+1) 
        
    def back_thread_page(self,current_idx):
        self.stack.setCurrentIndex(current_idx-1) 

    def back_graphic_display(self,i):
        self.stack.setCurrentIndex(i+self.p)




