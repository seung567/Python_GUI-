import tkinter.ttk as ttk
from tkinter import *



root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정

values = [str(i) + "일"  for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()



def btncmd() :

    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()