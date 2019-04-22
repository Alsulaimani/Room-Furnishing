#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the required packages
import PyQt5
from PyQt5 import QtWidgets
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLineEdit, QButtonGroup, QScrollArea, QScrollBar, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import pandas
import numpy


# In[3]:


global data
data = {"Age":[],"Gender":[],"Type":[],"Style":[],"Material":[],"Elemnt":[],"ArtWork":[]}


# In[4]:


#class to open application window
class Window_1 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_1,self).__init__()
        self.setGeometry(200,200,300,270)
        self.setWindowTitle("Design Application")
        self.Window1()
        
    def Window1(self):      
        self.s_text11 = QtWidgets.QLabel("Enter your personal information: ",self)
        self.s_text11.move(50,20) #left and top
        self.s_text11.resize(400,50) #width and hight

        self.s_text01 = QtWidgets.QLabel("Enter your age: ",self)
        self.s_text01.move(50,70) #left and top

        self.textbox0 = QLineEdit(self)
        self.textbox0.move(150, 65)
        self.textbox0.resize(60,25)
        validator = QtGui.QIntValidator(10, 80)
        self.textbox0.setValidator(validator)

        self.s_text02 = QtWidgets.QLabel("Enter your Gender: ",self)
        self.s_text02.move(50,95) #left and top
        self.s_text02.resize(400,50) #width and hight

        self.Mbtn = QtWidgets.QRadioButton('Male',self)
        self.Mbtn.move(50,140)

        self.Fbtn = QtWidgets.QRadioButton('Female',self)
        self.Fbtn.move(120,140)
        
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(200,200)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclicknext)        
        self.show()
        
    def onclicknext(self):
        global data
        data["Age"].append(int(self.textbox0.text()))
        if self.Mbtn.isChecked():
            data["Gender"].append(0)
        elif self.Fbtn.isChecked():
            data["Gender"].append(1)
        self.close()
        self.w2 = Window_2()
        


# In[5]:


class Window_2 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_2,self).__init__()
        self.setGeometry(200,200,1000,800)
        self.setWindowTitle("Design Application")
        self.Window2()
        
    def Window2(self):        
        self.s_text = QtWidgets.QLabel("Room Furnishing",self)
        self.s_text.move(100,20) #left and top
        self.s_text.resize(400,50) #width and hight

        self.s_text0 = QtWidgets.QLabel("Answer the fllowing Questions:",self)
        self.s_text0.move(150,70) #left and top
        self.s_text0.resize(400,50) #width and hight

        self.s_text1 = QtWidgets.QLabel("Q1.Which Room Type do you prefer?",self)
        self.s_text1.move(150,120) #top and left
        self.s_text1.resize(400,50) #width and hight

        self.bgroup1 = QButtonGroup()
        
        self.btn1 = QtWidgets.QRadioButton('       Bedroom       ',self)
        self.btn1.setIcon(QtGui.QIcon("/platform-images/bedroom.png"))
        self.btn1.setIconSize(QtCore.QSize(150,150))
        self.btn1.resize(300,150)
        self.btn1.move(150,170)
        

        self.btn11 = QtWidgets.QRadioButton('    Living room     ',self)
        self.btn11.setIcon(QtGui.QIcon("/platform-images/livingroom.jpg"))
        self.btn11.setIconSize(QtCore.QSize(150,150))
        self.btn11.resize(300,150)
        self.btn11.move(500,170)
        
        self.bgroup1.addButton(self.btn1, 1)
        self.bgroup1.addButton(self.btn11, 1)

        self.s_text2 = QtWidgets.QLabel("Q2.Which Roon Style do you prefer?",self)
        self.s_text2.move(150,320) #left and top
        self.s_text2.resize(400,50) #width and hight
        
        self.bgroup2 = QButtonGroup()
        
        self.btn2 = QtWidgets.QRadioButton('Modern bedroom ',self)
        self.btn2.setIcon(QtGui.QIcon("/platform-images/modern bedroom.jpg"))
        self.btn2.setIconSize(QtCore.QSize(150,150))
        self.btn2.resize(300,150)
        self.btn2.move(150,370)

        self.btn21 = QtWidgets.QRadioButton('Classic bedroom ',self)
        self.btn21.setIcon(QtGui.QIcon("/platform-images/classic_bedroom.png"))
        self.btn21.setIconSize(QtCore.QSize(150,150))
        self.btn21.resize(300,150)
        self.btn21.move(500,370)
        
        self.bgroup2.addButton(self.btn2, 1)
        self.bgroup2.addButton(self.btn21, 1)

        self.s_text3 = QtWidgets.QLabel("Q3.Which Furniture materials do you prefer?",self)
        self.s_text3.move(150,520) #top and left
        self.s_text3.resize(400,50) #width and hight
        
        self.bgroup3 = QButtonGroup()

        self.btn3 = QtWidgets.QRadioButton('          Wood           ',self)
        self.btn3.setIcon(QtGui.QIcon("/platform-images/wood.jpg"))
        self.btn3.setIconSize(QtCore.QSize(150,150))
        self.btn3.resize(300,150)
        self.btn3.move(150,570)

        self.btn31 = QtWidgets.QRadioButton('         Fabric          ',self)
        self.btn31.setIcon(QtGui.QIcon("/platform-images/fabric.jpeg"))
        self.btn31.setIconSize(QtCore.QSize(150,150))
        self.btn31.resize(300,150)
        self.btn31.move(500,570)
        
        self.bgroup3.addButton(self.btn3, 1)
        self.bgroup3.addButton(self.btn31, 1)
        
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(800,720)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclickbtn)
        
        self.pre_btn = QtWidgets.QPushButton('← Previous',self)
        self.pre_btn.move(150,720)
        self.pre_btn.resize(110,50)
        self.pre_btn.clicked.connect(self.onclickbtn2)
        
        self.show()
        
    def onclickbtn(self):
        global data
        if self.btn1.isChecked():
            data["Type"].append(0)
        elif self.btn11.isChecked():
            data["Type"].append(1)
        if self.btn2.isChecked():
            data["Style"].append(0)
        elif self.btn21.isChecked():
            data["Style"].append(1)
        if self.btn3.isChecked():
            data["Material"].append(0)
        elif self.btn31.isChecked():
            data["Material"].append(1)
        self.close()
        self.w3 = Window_3()
        
    def onclickbtn2(self):
        global data
        #self.getData()
        #self.store_data()
        self.close()
        self.w1 = Window_1()


# In[6]:


class Window_3 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_3,self).__init__()
        self.setGeometry(200,200,1000,800)
        self.setWindowTitle("Design Application")
        self.Window3()
        
    def Window3(self):
        self.s_text = QtWidgets.QLabel("Room Furnishing",self)
        self.s_text.move(100,20) #left and top
        self.s_text.resize(400,50) #width and hight

        self.s_text0 = QtWidgets.QLabel("Answer the fllowing Questions:",self)
        self.s_text0.move(150,70) #left and top
        self.s_text0.resize(400,50) #width and hight
        
        self.s_text4 = QtWidgets.QLabel("Q4.How many Furniture elements do you prefer?",self)
        self.s_text4.move(150,120) #top and left
        self.s_text4.resize(400,50) #width and hight
        
        self.bgroup4 = QButtonGroup()
        
        self.btn4 = QtWidgets.QRadioButton('          Crowded Room          ',self)
        self.btn4.setIcon(QtGui.QIcon("/platform-images/crowded room.jpg"))
        self.btn4.setIconSize(QtCore.QSize(150,150))
        self.btn4.resize(300,150)
        self.btn4.move(150,170)

        self.btn41 = QtWidgets.QRadioButton('         Not Crowded Room         ',self)
        self.btn41.setIcon(QtGui.QIcon("/platform-images/not crowded room.jpg"))
        self.btn41.setIconSize(QtCore.QSize(150,150))
        self.btn41.resize(300,150)
        self.btn41.move(500,170)
        
        self.bgroup4.addButton(self.btn4, 1)
        self.bgroup4.addButton(self.btn41, 1)

        self.s_text5 = QtWidgets.QLabel("Q5.Which Art Work do you prefer?",self)
        self.s_text5.move(150,370) #top and left
        self.s_text5.resize(400,50) #width and hight
        
        self.bgroup5 = QButtonGroup()

        self.btn5 = QtWidgets.QRadioButton('          Abstract Art Works          ',self)
        self.btn5.setIcon(QtGui.QIcon("/platform-images/abstract artwork1.jpg"))
        self.btn5.setIconSize(QtCore.QSize(150,150))
        self.btn5.resize(300,150)
        self.btn5.move(150,420)

        self.btn51 = QtWidgets.QRadioButton('         LandScape Art Works         ',self)
        self.btn51.setIcon(QtGui.QIcon("/platform-images/landscape asrtwork1.jpg"))
        self.btn51.setIconSize(QtCore.QSize(150,150))
        self.btn51.resize(300,150)
        self.btn51.move(500,420)
        
        self.bgroup5.addButton(self.btn5, 1)
        self.bgroup5.addButton(self.btn51, 1)
        
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(600,620)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclickbtn)
        
        self.pre_btn = QtWidgets.QPushButton('← Previous',self)
        self.pre_btn.move(150,620)
        self.pre_btn.resize(110,50)
        self.pre_btn.clicked.connect(self.onclickbtn2)
        
        self.show() 
        
    
        
    def getData(self):
        global data
        if self.btn4.isChecked():
            data["Elemnt"].append(0)
        elif self.btn41.isChecked():
            data["Elemnt"].append(1)
        if self.btn5.isChecked():
            data["ArtWork"].append(0)
        elif self.btn51.isChecked():
            data["ArtWork"].append(1)
            
    def store_data(self):
        global data
        df1 = pandas.read_csv("Data.csv")
        df2 = pandas.DataFrame(data)
        df = pandas.concat([df1,df2])
        df.to_csv("Data.csv",index=False)
        
    def onclickbtn(self):
        global data
        self.getData()
        self.store_data()
        self.close()
        self.w4 = Window_4()
        
    def onclickbtn2(self):
        global data
        #self.getData()
        #self.store_data()
        self.close()
        self.w2 = Window_2()


# In[7]:


from sklearn.externals import joblib
model= joblib.load('model.pkl')


# In[9]:


class Window_4 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_4,self).__init__()
        self.setGeometry(200,200,1000,800)
        self.setWindowTitle("Design Application")
        self.Window4()
        
    def Window4(self):
        global data
        data2=numpy.array(list(data.values())).reshape(1,7)
        x=model.predict(data2)
        image1=int(x[0][0])
        image2=int(x[0][1])
        print('predicting',image1,image2)
        
        if (image1==0):
            self.s_text = QtWidgets.QLabel("We recommend you this room layout",self)
            self.s_text.move(100,100) 
            
            self.image1 = QLabel(self)
            self.pixmap = QtGui.QPixmap("/Rooms/bedroom1.png")
            self.image1.resize(350, 350)
            self.image1.setPixmap(self.pixmap.scaled(self.image1.size(), QtCore.Qt.IgnoreAspectRatio))
            self.image1.move(250,250)
        
        else:
            self.s_text = QtWidgets.QLabel("We recommend you this room layout",self)
            self.s_text.move(100,100) #left and top
            self.s_text.resize(400,50) #width and hight
            
            self.image1 = QLabel(self)
            self.pixmap = QtGui.QPixmap("/Rooms/bedroom2.png")
            self.image1.resize(350, 350)
            self.image1.setPixmap(self.pixmap.scaled(self.image1.size(), QtCore.Qt.IgnoreAspectRatio))
            self.image1.move(250,250)
        
        self.sbmt_btn = QtWidgets.QPushButton('Done!! ',self)
        self.sbmt_btn.move(750,650)
        self.sbmt_btn.resize(80,50)
        self.sbmt_btn.clicked.connect(self.onclickbtn)
        self.show()
            
    def onclickbtn(self):
        global data
        self.close()


# In[10]:


app = QtWidgets.QApplication(sys.argv)
w=Window_1()
sys.exit(app.exec_())

