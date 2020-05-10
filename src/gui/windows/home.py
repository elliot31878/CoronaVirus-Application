from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPieSeries, QPieSlice, QLineSeries,QAreaSeries
from PyQt5.QtGui import QPen, QLinearGradient, QColor
from PyQt5.QtCore import QPointF
from PyQt5.Qt import QGradient, Qt, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from bs4 import BeautifulSoup
import pyautogui

import requests
import sys
import os
from gui.windows.page_ways_to_prevent import Ui_Dialog_page_way_to_prevent

#-----------GlobalVariebleList---------------
"""this list for save value in the site"""
list_alls=[]
"""this lists for split special value in the listAlls"""
list_country=[]
list_total_case=[]
list_new_case=[]
list_total_deaths=[]
list_new_deaths=[]
list_total_recovered=[]
list_active_case=[]
list_serious_critical=[]
list_tot_cases=[]
list_death_case=[]
list_totla_tests=[]
list_tests=[]
list_cases=[]
#--------------------------------------------
display_width,display_height=965, 889
width,height=pyautogui.size()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((width-display_width)/2,(height-display_height)/2)
#----------------------------------
def empty_list():
    global list_alls,list_country,list_total_case,list_new_case,list_total_deaths,list_new_deaths,list_total_recovered,list_active_case,list_serious_critical,list_tot_cases,list_death_case,list_totla_tests,list_tests
    list_alls=[]
    list_country=[]
    list_total_case=[]
    list_new_case=[]
    list_total_deaths=[]
    list_new_deaths=[]
    list_total_recovered=[]
    list_active_case=[]
    list_serious_critical=[]
    list_tot_cases=[]
    list_death_case=[]
    list_totla_tests=[]
    list_tests=[]
def get_information_covid19():
    global list_country
    get_request=requests.get("https://www.worldometers.info/coronavirus")
    soup=BeautifulSoup(get_request.text,"html.parser")
    for cases in soup.find_all(class_="maincounter-number"):
        list_cases.append(cases.text.strip())
    """Do Work :)"""
    count=-1
    # for i in soup.find_all("tr",attrs={"style":""}):
    #     print
    for country in soup.find_all("td"):
        list_alls.append(country.text.strip())
    for counter in range(0,int(len(list_alls)/2)):
        if count==12:
            count=-1
            "Go to Next Row Table"
        if count ==-1:
            """Split country from listAlls and Push to CountryList """
            list_country.append(list_alls[counter])
        elif count==0:
            """Split totalCase from listAlls and Push to totalCaseList """
            list_total_case.append(list_alls[counter])
        elif count==1:
            """Split newCase from listAlls and Push to newCaseList """
            list_new_case.append(list_alls[counter])
        elif count==2:
            """Split totalDeath from listAlls and Push to totalDeathList """
            list_total_deaths.append(list_alls[counter])
        elif count==3:
            """Split newDeath from listAlls and Push to newDeathList """
            list_new_deaths.append(list_alls[counter])
        elif count==4:
            """Split totalRecoverd from listAlls and Push to totalRecoverdList """
            list_total_recovered.append(list_alls[counter])
        elif count==5:
            """Split activeCase from listAlls and Push to activeCaseList """
            list_active_case.append(list_alls[counter])
        elif count==6:
            """Split seriousCritical from listAlls and Push to seriousCriticalList """
            list_serious_critical.append(list_alls[counter])
        elif count==7:
            """Split totCase from listAlls and Push to totCaseList """
            list_tot_cases.append(list_alls[counter])
        elif count==8:
            """Split deadthCase from listAlls and Push to deadthCaseList """
            list_death_case.append(list_alls[counter])
        elif count==9:
            """Split totalTests from listAlls and Push to totalTestsList """
            list_totla_tests.append(list_alls[counter])
        elif count==10:
            """Split Tests from listAlls and Push to TestsList """
            list_tests.append(list_alls[counter])
        #Increases Global Counter in the Loop
        count=count+1
    for i in range(0,7):
        list_country.pop(0)
        list_total_case.pop(0)
        list_new_case.pop(0)
        list_total_deaths.pop(0)
        list_new_deaths.pop(0)
        list_total_recovered.pop(0)
        list_active_case.pop(0)
        list_serious_critical.pop(0)
        list_tot_cases.pop(0)
        list_death_case.pop(0)
        list_totla_tests.pop(0)
        list_tests.pop(0)

    for i in range(0,7):
        list_country.pop(214)
        list_total_case.pop(214)
        list_new_case.pop(214)
        list_total_deaths.pop(214)
        list_new_deaths.pop(214)
        list_total_recovered.pop(214)
        list_active_case.pop(214)
        list_serious_critical.pop(214)
        list_tot_cases.pop(214)
        list_death_case.pop(214)
        list_totla_tests.pop(214)
        list_tests.pop(214)
#----------------------------------
get_information_covid19()
class Ui_Dialog(QMainWindow):
    def show_ways_to_prevent(self):
        self.dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog_page_way_to_prevent()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
    #------------------------------------------------------------------------------
    def show_piechart(self):
        """""
        This Method For Show Pie Chart
        """""
        #--------------------------------------------------------------------------------------------
        totalcase=int((str(list_cases[0].replace("+","")).replace(",","")))
        newcase=int((str(list_new_case[0]).replace("+","")).replace(",",""))
        totaldeath=int((str(list_cases[1].replace("+","")).replace(",","")))
        new_deaths=int((str(list_new_deaths[0]).replace("+","")).replace(",",""))
        #----------------------------------------------------------------------------------------------
        series = QPieSeries()
        series.append("TotalCase : "+str(totalcase)+"K",totalcase)
        series.append("NewCase : "+str(newcase)+"K",newcase)
        series.append("TotalDeaths : "+str(totaldeath)+"K",totaldeath)
        series.append("NewDeaths : "+str(new_deaths)+"K",new_deaths)
        #--------------------------------------------------------------------------------------------------------
        Slice=QPieSlice()
        for i in range(0,4):
            Slice=series.slices()[i]
            Slice.setLabelVisible(True)
        Slice=series.slices()[3]
        Slice.setExploded(True)
        #------------------------------------------------------------------
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Chart increase Coronavirus")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chart.createDefaultAxes()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/virus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #-------------------------------------------------------------
        self.setCentralWidget(chartView)
        self.setCentralWidget(chartView)
        self.resize(800, 800)
        self.setWindowIcon(icon)
        self.setWindowTitle("PieChart")
        self.show()
    #------------------------------------------------------------------------------
    def table_setting(self):
        """""   
            This Method For Fill And Do works Table
        """""
        for i in range(0,len(list_country)):
            self.mytbl.setItem(i,0,QtWidgets.QTableWidgetItem(list_country[i]))
        for i in range(0,len(list_total_case)):
            self.mytbl.setItem(i,1,QtWidgets.QTableWidgetItem(list_total_case[i]))
        for i in range(0,len(list_new_case)):
            self.mytbl.setItem(i,2,QtWidgets.QTableWidgetItem(list_new_case[i]))
        for i in range(0,len(list_total_deaths)):
            self.mytbl.setItem(i,3,QtWidgets.QTableWidgetItem(list_total_deaths[i]))
        for i in range(0,len(list_new_deaths)):
            self.mytbl.setItem(i,4,QtWidgets.QTableWidgetItem(list_new_deaths[i]))
        for i in range(0,len(list_total_recovered)):
            self.mytbl.setItem(i,5,QtWidgets.QTableWidgetItem(list_total_recovered[i]))
        for i in range(0,len(list_active_case)):
            self.mytbl.setItem(i,6,QtWidgets.QTableWidgetItem(list_active_case[i]))
        for i in range(0,len(list_serious_critical)):
            self.mytbl.setItem(i,7,QtWidgets.QTableWidgetItem(list_serious_critical[i]))    
        for i in range(0,len(list_tot_cases)):
            self.mytbl.setItem(i,8,QtWidgets.QTableWidgetItem(list_tot_cases[i]))
        for i in range(0,len(list_death_case)):
            self.mytbl.setItem(i,9,QtWidgets.QTableWidgetItem(list_death_case[i]))
        for i in range(0,len(list_totla_tests)):
            self.mytbl.setItem(i,10,QtWidgets.QTableWidgetItem(list_totla_tests[i]))
        for i in range(0,len(list_tests)):
            self.mytbl.setItem(i,11,QtWidgets.QTableWidgetItem(list_tests[i]))
        #Change Header
        #self.mytbl.verticalHeader().setVisible(False)
        self.mytbl.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("Country"))
        self.mytbl.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("Total Case"))
        self.mytbl.setHorizontalHeaderItem(2,QtWidgets.QTableWidgetItem("New Case"))
        self.mytbl.setHorizontalHeaderItem(3,QtWidgets.QTableWidgetItem("Total Deaths"))
        self.mytbl.setHorizontalHeaderItem(4,QtWidgets.QTableWidgetItem("New Deaths"))
        self.mytbl.setHorizontalHeaderItem(5,QtWidgets.QTableWidgetItem("Total Recovered"))
        self.mytbl.setHorizontalHeaderItem(6,QtWidgets.QTableWidgetItem("Active Case"))
        self.mytbl.setHorizontalHeaderItem(7,QtWidgets.QTableWidgetItem("Serious Critical"))
        self.mytbl.setHorizontalHeaderItem(8,QtWidgets.QTableWidgetItem("Tot Cases"))
        self.mytbl.setHorizontalHeaderItem(9,QtWidgets.QTableWidgetItem("Death Case"))
        self.mytbl.setHorizontalHeaderItem(10,QtWidgets.QTableWidgetItem("Totla Tests"))
        self.mytbl.setHorizontalHeaderItem(11,QtWidgets.QTableWidgetItem("Tests"))
        #Change Style Sheet
        self.mytbl.horizontalHeader().setFixedHeight(50)
        self.mytbl.horizontalHeader().setStyleSheet("font: 75 10pt \"Tahoma\";padding-top:10px")
        try:
                #Change Text Alignment Row
            for i in range(0,12):
                self.mytbl.horizontalHeaderItem(i).setTextAlignment(QtCore.Qt.AlignLeft)
                #ChangeColor First Row
            for first_row in range(0,12):
                self.mytbl.item(0,first_row).setBackground(QtCore.Qt.lightGray)
                #ChangeColor New Deaths Row 
            for index_new_death in range(0,len(list_new_deaths)-1):
                if str(list_new_deaths[index_new_death])!="":
                    self.mytbl.item(index_new_death,4).setBackground(QtCore.Qt.red)
                    self.mytbl.item(index_new_death,4).setForeground(QtGui.QBrush(QtGui.QColor(255,255,255)))
                #Change Color New Case Row
                for index_new_case in range(0,len(list_new_case)-1):
                    if str(list_new_case[index_new_case])!="":
                        self.mytbl.item(index_new_case,2).setBackground(QtGui.QBrush(QtGui.QColor(255,238,170)))
        except Exception as ex:
            print(ex)
    #------------------------------------------------------------------------------
    def all_settings(self):
        empty_list()
        get_information_covid19()
        self.table_setting()
    #------------------------------------------------------------------------------
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(965, 889)
        Dialog.setMaximumSize(965, 889)
        Dialog.setMinimumSize(965, 889)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/virus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: #8E9DC6;\n""font: 8pt \"Tahoma\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 943, 867))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.pic_detailes = QtWidgets.QLabel(self.frame_4)
        self.pic_detailes.setAutoFillBackground(False)
        self.pic_detailes.setText("")
        self.pic_detailes.setPixmap(QtGui.QPixmap("assets/startup.png"))
        self.pic_detailes.setAlignment(QtCore.Qt.AlignCenter)

        self.pic_detailes.setObjectName("pic_detailes")

        self.verticalLayout_3.addWidget(self.pic_detailes)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 897, 412))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(255,255,255);\n""border-radius: 10px;")
        self.scrollAreaWidgetContents_2.setContentsMargins(10,10,10,10)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.mytbl = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.mytbl.setMaximumSize(QtCore.QSize(591, 391))
        self.mytbl.setObjectName("mytbl")
        self.mytbl.setStyleSheet("background-color: rgb(255,255,255); ")
        self.mytbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mytbl.setColumnCount(12)
        self.mytbl.setRowCount(len(list_country)-1)
        self.mytbl.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.mytbl.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        
        #-------------------------------------------------------------
        self.table_setting()
        self.horizontalLayout.addWidget(self.mytbl)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_3.setStyleSheet("background-color: rgb(35,34,75);\n""color:rgb(255,255,255);\n""border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lbl_covidCase = QtWidgets.QLabel(self.frame_3)
        self.lbl_covidCase.setContentsMargins(10,10,10,10)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_covidCase.setFont(font)
        self.lbl_covidCase.setStyleSheet("font: 10pt \"Tahoma\";")
        self.lbl_covidCase.setObjectName("lbl_covidCase")
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setStyleSheet("background-color: rgb(35,34,55);\n""color:rgb(255,255,255);\n""border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_deaths = QtWidgets.QLabel(self.frame)
        self.lbl_deaths.setContentsMargins(10,10,10,10)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_deaths.setFont(font)
        self.lbl_deaths.setStyleSheet("font: 10pt \"Tahoma\";\n""color: rgb(255, 255, 255);")
        self.lbl_deaths.setObjectName("lbl_deaths")
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2.setStyleSheet("background-color: rgb(35,34,75);\n""color:rgb(255,255,255);\n""border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl_Recoverd = QtWidgets.QLabel(self.frame_2)
        self.lbl_Recoverd.setContentsMargins(10,10,10,10)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_Recoverd.setFont(font)
        self.lbl_Recoverd.setStyleSheet("font: 10pt \"Tahoma\";")
        self.lbl_Recoverd.setObjectName("lbl_Recoverd")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_4.setContentsMargins(0,30,0,30)
        self.btn_showPieChart=QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_showPieChart.setText("Show PieChart")
        self.btn_showPieChart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_showPieChart.setMouseTracking(False)
        self.btn_showPieChart.setStyleSheet("color: rgb(255, 255, 255);\n""border:2px solid rgb(34,34,35);\n""background-color: rgb(60,60,60);\n"";padding-left:10; padding-top:10; padding-bottom:10; padding-right:10;")
        self.btn_showPieChart.setCheckable(False)
        self.btn_showPieChart.setChecked(False)
        self.btn_showPieChart.setDefault(False)
        self.btn_showPieChart.setFlat(True)
        self.btn_showPieChart.setObjectName("btn_showPieChart")
        self.btn_showPieChart.clicked.connect(self.show_piechart)

        self.btn_Ways_to_prevent=QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_Ways_to_prevent.setText("Ways to prevent")
        self.btn_Ways_to_prevent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Ways_to_prevent.setMouseTracking(False)
        self.btn_Ways_to_prevent.setStyleSheet("color: rgb(255, 255, 255);\n""border:2px solid rgb(34,34,35);\n""background-color: rgb(60,60,60);\n""padding-left:10; padding-top:10; padding-bottom:10; padding-right:10;")
        self.btn_Ways_to_prevent.setCheckable(False)
        self.btn_Ways_to_prevent.setChecked(False)
        self.btn_Ways_to_prevent.setDefault(False)
        self.btn_Ways_to_prevent.setFlat(True)
        self.btn_Ways_to_prevent.setObjectName("btn_showPieChart")
        self.btn_Ways_to_prevent.clicked.connect(self.show_ways_to_prevent)

        self.btn_UpdateData=QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_UpdateData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_UpdateData.setMouseTracking(False)
        self.btn_UpdateData.setText("Update")
        self.btn_UpdateData.setStyleSheet("color: rgb(255, 255, 255);\n""border:2px solid rgb(34,34,35);\n""background-color: rgb(60,60,60);\n""padding-left:10; padding-top:10; padding-bottom:10; padding-right:10;")
        self.btn_UpdateData.setCheckable(False)
        self.btn_UpdateData.setChecked(False)
        self.btn_UpdateData.setDefault(False)
        self.btn_UpdateData.setFlat(True)
        self.btn_UpdateData.setObjectName("btn_UpdateData")
        self.btn_UpdateData.clicked.connect(self.all_settings)
        self.verticalLayout_4.addWidget(self.btn_showPieChart)
        self.verticalLayout_4.addWidget(self.btn_Ways_to_prevent)
        self.verticalLayout_4.addWidget(self.btn_UpdateData)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    #------------------------------------------------------------------------------
    def retranslateUi(self, Dialog):
        #--------------------------------------------------------------------------------------------
        try:
            totalcase=list_cases[0]
            totalrecoverd=list_cases[1]
            totaldeaths=list_cases[2]
        except Exception as ex:
            totalcase=0
            totalrecoverd=0
            totaldeaths=0
        #----------------------------------------------------------------------------------------------
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Covid 19 Status"))
        self.lbl_covidCase.setText(_translate("Dialog", "Coronavirus Cases : "+totalcase))
        self.lbl_deaths.setText(_translate("Dialog", "Deaths : "+totaldeaths))
        self.lbl_Recoverd.setText(_translate("Dialog", "Recovered : "+totalrecoverd))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    
if __name__ == "__main__":
    main()
