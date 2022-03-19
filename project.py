import pyttsx3
from plyer import notification
import time
import xlrd
import inflect
p=inflect.engine()

file_location="list.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

def notify(title,message):
    notification.notify(title=title,message=message,app_icon="icon3.ico",timeout = 15, )

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",135)
engine.setProperty("volume",1.0)

def values(n,t):
    name=n
    timer=t
    value1 = 0
    i=1
    while True:
        value2=0
        msg="__WORD__:  "+sheet.cell_value(value1,value2)+"\n\n__MEANING__:  "+sheet.cell_value(value1,value2+1)
        text="hellow  " + name + f" here is your {p.ordinal(i)} word "
        engine.say(text)
        notify("VOCABULARY",msg)
        engine.runAndWait()
        value1=value1+1
        i=i+1
        time.sleep(timer)
