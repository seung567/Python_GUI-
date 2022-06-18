from msilib.schema import CheckBox
from tkinter import *

from numpy import var

root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()
# chkbox.deselect()

chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox3 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()
chkbox3.pack()

def btncmd() :
    print(chkvar.get()) # 0 : 체크 해제 , 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()