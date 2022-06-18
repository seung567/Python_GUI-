from msilib.schema import CheckBox
from tkinter import *

from numpy import var

root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack()



root.mainloop()