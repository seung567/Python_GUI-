import tkinter.ttk as ttk
from tkinter import *
import time



root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정


#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()


# def btncmd() :

#     progressbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2() :
    for i  in range(1, 101) :
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()