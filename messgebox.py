import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정

def info() :

    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")


def warn() :

    msgbox.showwarning("경고", "해당 좌석은 매진 되었습니다.")

def error() :

    msgbox.showerror("에러", "결제오류가 발생했습니다.")

def okcancel() :

    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()


Button(root, command=okcancel, text="확인 취소").pack()


root.mainloop()