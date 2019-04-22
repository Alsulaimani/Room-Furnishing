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


# In[3]:


global data
data = {"Age":[],"Gender":[],"Type":[],"Style":[],"Material":[],"Elemnt":[],"ArtWork":[],"Image1":[],"Image2":[]}


# In[4]:


class Window_1 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_1,self).__init__()
        self.setGeometry(200,200,300,270)
        self.setWindowTitle("Design Application")
        self.Window1()
        
    def Window1(self): 
        #writing text to the window
        self.s_text11 = QtWidgets.QLabel("Enter your personal information: ",self)
        self.s_text11.move(50,20) #left and top
        self.s_text11.resize(400,50) #width and hight

        self.s_text01 = QtWidgets.QLabel("Enter your age: ",self)
        self.s_text01.move(50,70) #left and top
        
        #creating textbox to get user age
        self.textbox0 = QLineEdit(self)
        self.textbox0.move(150, 65)
        self.textbox0.resize(60,25)
        #set a validator to the textbox to accept integers only in range from (10,80)
        validator = QtGui.QIntValidator(10, 80)
        self.textbox0.setValidator(validator)

        self.s_text02 = QtWidgets.QLabel("Enter your Gender: ",self)
        self.s_text02.move(50,95) #left and top
        self.s_text02.resize(400,50) #width and hight
        
        #creating radio button to get user's gender
        self.Mbtn = QtWidgets.QRadioButton('Male',self)
        self.Mbtn.move(50,140)

        self.Fbtn = QtWidgets.QRadioButton('Female',self)
        self.Fbtn.move(120,140)
        
        #creating next button which will take use to the next window
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(200,200)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclicknext)   
        
        #show the window
        self.show()
           
    def onclicknext(self):
        global data
        data["Age"].append(int(self.textbox0.text()))
        #get user's input
        if self.Mbtn.isChecked():
            data["Gender"].append(0)
        elif self.Fbtn.isChecked():
            data["Gender"].append(1)
        #closing the current window
        self.close()
        #running window 2 
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
        #writing text to the window
        self.s_text = QtWidgets.QLabel("Room Furnishing",self)
        self.s_text.move(100,20) #left and top
        self.s_text.resize(400,50) #width and hight

        self.s_text0 = QtWidgets.QLabel("Answer the fllowing Questions:",self)
        self.s_text0.move(150,70) #left and top
        self.s_text0.resize(400,50) #width and hight
        
        self.s_text1 = QtWidgets.QLabel("Q1.Which Room Type do you prefer?",self)
        self.s_text1.move(150,120) #top and left
        self.s_text1.resize(400,50) #width and hight
        
        #creating button group
        self.bgroup1 = QButtonGroup()
        
        #creating radio buttons 1
        self.btn1 = QtWidgets.QRadioButton('       Bedroom       ',self)
        self.btn1.setIcon(QtGui.QIcon("/platform-images/bedroom.png"))
        self.btn1.setIconSize(QtCore.QSize(150,150))
        self.btn1.resize(300,150)
        self.btn1.move(150,170)
        
        #creating radio buttons 2
        self.btn11 = QtWidgets.QRadioButton('    Living room     ',self)
        self.btn11.setIcon(QtGui.QIcon("/platform-images/livingroom.jpg"))
        self.btn11.setIconSize(QtCore.QSize(150,150))
        self.btn11.resize(300,150)
        self.btn11.move(500,170)
        
        #adding the 2 radio buttons to group
        self.bgroup1.addButton(self.btn1, 1)
        self.bgroup1.addButton(self.btn11, 1)
        
        #writing the second question on the window
        self.s_text2 = QtWidgets.QLabel("Q2.Which Roon Style do you prefer?",self)
        self.s_text2.move(150,320) #left and top
        self.s_text2.resize(400,50) #width and hight
        
        #creating button group
        self.bgroup2 = QButtonGroup()
        
        #creating radio buttons 1
        self.btn2 = QtWidgets.QRadioButton('Modern bedroom ',self)
        self.btn2.setIcon(QtGui.QIcon("/platform-images/modern bedroom.jpg"))
        self.btn2.setIconSize(QtCore.QSize(150,150))
        self.btn2.resize(300,150)
        self.btn2.move(150,370)
        
        #creating radio buttons 2
        self.btn21 = QtWidgets.QRadioButton('Classic bedroom ',self)
        self.btn21.setIcon(QtGui.QIcon("/platform-images/classic_bedroom.png"))
        self.btn21.setIconSize(QtCore.QSize(150,150))
        self.btn21.resize(300,150)
        self.btn21.move(500,370)
        
        #adding the 2 radio buttons to group
        self.bgroup2.addButton(self.btn2, 1)
        self.bgroup2.addButton(self.btn21, 1)
        
        #writing the third question on the window
        self.s_text3 = QtWidgets.QLabel("Q3.Which Furniture materials do you prefer?",self)
        self.s_text3.move(150,520) #top and left
        self.s_text3.resize(400,50) #width and hight
        
        #creating button group
        self.bgroup3 = QButtonGroup()
        
        #creating radio buttons 1
        self.btn3 = QtWidgets.QRadioButton('          Wood           ',self)
        self.btn3.setIcon(QtGui.QIcon("/platform-images/wood.jpg"))
        self.btn3.setIconSize(QtCore.QSize(150,150))
        self.btn3.resize(300,150)
        self.btn3.move(150,570)
        
        #creating radio buttons 2
        self.btn31 = QtWidgets.QRadioButton('         Fabric          ',self)
        self.btn31.setIcon(QtGui.QIcon("/platform-images/fabric.jpeg"))
        self.btn31.setIconSize(QtCore.QSize(150,150))
        self.btn31.resize(300,150)
        self.btn31.move(500,570)
        
        #adding the 2 radio buttons to group
        self.bgroup3.addButton(self.btn3, 1)
        self.bgroup3.addButton(self.btn31, 1)
        
        #creating next button
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(800,720)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclickbtn)
        
        #creating previous button
        self.pre_btn = QtWidgets.QPushButton('← Previous',self)
        self.pre_btn.move(150,720)
        self.pre_btn.resize(110,50)
        self.pre_btn.clicked.connect(self.onclickbtn2)
        
        #show the window
        self.show()
    
    #function for next button
    def onclickbtn(self):
        global data
        #get user's input
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
        #close the current window
        self.close()
        #running window 3
        self.w3 = Window_3()
    
    #function for previous button
    def onclickbtn2(self):
        global data
        #close current window
        self.close()
        #running window 1
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
        #writing text to the window
        self.s_text = QtWidgets.QLabel("Room Furnishing",self)
        self.s_text.move(100,20) #left and top
        self.s_text.resize(400,50) #width and hight

        self.s_text0 = QtWidgets.QLabel("Answer the fllowing Questions:",self)
        self.s_text0.move(150,70) #left and top
        self.s_text0.resize(400,50) #width and hight
        
        self.s_text4 = QtWidgets.QLabel("Q4.How many Furniture elements do you prefer?",self)
        self.s_text4.move(150,120) #top and left
        self.s_text4.resize(400,50) #width and hight
        
        #creating button group
        self.bgroup4 = QButtonGroup()
        
        #creating radio button 1
        self.btn4 = QtWidgets.QRadioButton('          Crowded Room          ',self)
        self.btn4.setIcon(QtGui.QIcon("/platform-images/crowded room.jpg"))
        self.btn4.setIconSize(QtCore.QSize(150,150))
        self.btn4.resize(300,150)
        self.btn4.move(150,170)
        
        #creating radio button 2
        self.btn41 = QtWidgets.QRadioButton('         Not Crowded Room         ',self)
        self.btn41.setIcon(QtGui.QIcon("/platform-images/not crowded room.jpg"))
        self.btn41.setIconSize(QtCore.QSize(150,150))
        self.btn41.resize(300,150)
        self.btn41.move(500,170)
        
        #adding the 2 radio buttons to group
        self.bgroup4.addButton(self.btn4, 1)
        self.bgroup4.addButton(self.btn41, 1)

        self.s_text5 = QtWidgets.QLabel("Q5.Which Art Work do you prefer?",self)
        self.s_text5.move(150,370) #top and left
        self.s_text5.resize(400,50) #width and hight
        
        #creating button group
        self.bgroup5 = QButtonGroup()

        #creating radio buttons 1
        self.btn5 = QtWidgets.QRadioButton('          Abstract Art Works          ',self)
        self.btn5.setIcon(QtGui.QIcon("/platform-images/abstract artwork1.jpg"))
        self.btn5.setIconSize(QtCore.QSize(150,150))
        self.btn5.resize(300,150)
        self.btn5.move(150,420)

        #creating radio buttons 2
        self.btn51 = QtWidgets.QRadioButton('         LandScape Art Works         ',self)
        self.btn51.setIcon(QtGui.QIcon("/platform-images/landscape asrtwork1.jpg"))
        self.btn51.setIconSize(QtCore.QSize(150,150))
        self.btn51.resize(300,150)
        self.btn51.move(500,420)
        
        #adding the 2 radio buttons to group
        self.bgroup5.addButton(self.btn5, 1)
        self.bgroup5.addButton(self.btn51, 1)
        
        #creating next button
        self.next_btn = QtWidgets.QPushButton('Next →',self)
        self.next_btn.move(600,620)
        self.next_btn.resize(80,50)
        self.next_btn.clicked.connect(self.onclickbtn)
        
        #creating previous button
        self.pre_btn = QtWidgets.QPushButton('← Previous',self)
        self.pre_btn.move(150,620)
        self.pre_btn.resize(110,50)
        self.pre_btn.clicked.connect(self.onclickbtn2)
        
        #show the window
        self.show() 
        
    #function to get user's input
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
        
    #function for next button
    def onclickbtn(self):
        global data
        #get user's input
        self.getData()
        #closing the current window
        self.close()
        #running window 4
        self.w4 = Window_4()
        
    #function for previous button
    def onclickbtn2(self):
        global data
        #closing the current window
        self.close()
        #running the previous window
        self.w2 = Window_2()


# In[7]:


class Window_4 (QtWidgets.QMainWindow):
    global data
    def __init__(self):
        super(Window_4,self).__init__()
        self.setGeometry(200,200,1000,800)
        self.setWindowTitle("Design Application")
        self.Window4()
        
    def Window4(self):
        global data
        if data["Type"][0] ==0 or data["Type"][0] ==1:
            #show bedroom image 1
            self.image1 = QLabel(self)
            self.pixmap = QtGui.QPixmap("/Rooms/bedroom1.png")
            self.image1.resize(300, 300)
            self.image1.setPixmap(self.pixmap.scaled(self.image1.size(), QtCore.Qt.IgnoreAspectRatio))
            self.image1.move(110,150)
            
            #creating button group
            self.bdgroup1 = QButtonGroup()
            
            #creating radio buttons for image 1
            self.bd1like = QtWidgets.QRadioButton('Like',self)
            self.bd1like.move(150,500)
            
            #show bedroom image 2
            self.image2 = QLabel(self)
            self.pixmap = QtGui.QPixmap("/Rooms/bedroom2.png")
            self.image2.resize(350, 350)
            self.image2.setPixmap(self.pixmap.scaled(self.image2.size(), QtCore.Qt.IgnoreAspectRatio))
            self.image2.move(550,100)

            #creating radio buttons for image 2
            self.bd2like = QtWidgets.QRadioButton('Like',self)
            self.bd2like.move(600,500)
            
            #adding the 2 radio buttons to group
            self.bdgroup1.addButton(self.bd1like, 1)
            self.bdgroup1.addButton(self.bd2like, 1)
            
            #creating submit button
            self.sbmt_btn = QtWidgets.QPushButton('Submit ',self)
            self.sbmt_btn.move(750,650)
            self.sbmt_btn.resize(80,50)
            self.sbmt_btn.clicked.connect(self.onclickbtn)

            #creating start new button
            self.start_btn2 = QtWidgets.QPushButton('Start New ',self)
            self.start_btn2.move(850,650)
            self.start_btn2.resize(100,50)
            self.start_btn2.clicked.connect(self.onclickbtn2)
            
            self.show()
            
    #geting user's input
    def getImageData(self):
        global data
        if self.bd1like.isChecked():
            data["Image1"].append(0)
            data["Image2"].append(1)
        elif self.bd2like.isChecked():
            data["Image2"].append(0)
            data["Image1"].append(1)
        
    #store the data in dataframe        
    def store_data(self):
        global data
        df1 = pandas.read_csv("Data.csv")
        df2 = pandas.DataFrame(data)
        df = pandas.concat([df1,df2])
        df.to_csv("Data.csv",index=False)
            
    #function for submit button
    def onclickbtn(self):
        global data
        #get user's input
        self.getImageData()
        #storing the data in dataframe
        self.store_data()
        #closing the current window
        self.close()
        
    #function for start new button
    def onclickbtn2(self):
        global data
        #get user's input
        self.getImageData()
        #storing the data in dataframe
        self.store_data()
        #closing the current window
        self.close()
        #data = {"Age":[],"Gender":[],"Type":[],"Style":[],"Material":[],"Elemnt":[],"ArtWork":[],
                #"Image1":[],"Image2":[]} #hash it while running this file in py form       
        #running the first window again
        self.w = Window_1()


# In[9]:


app = QtWidgets.QApplication(sys.argv)
w=Window_1()
sys.exit(app.exec_())


# In[ ]:




