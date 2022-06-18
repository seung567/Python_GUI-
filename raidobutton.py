from tkinter import *



root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정


test_frm = Frame(root)
test_frm.pack()


test_var = IntVar()

test_radio = Radiobutton(test_frm, text="test", value=1, variable=test_var)

test_en = Entry(test_frm)

test_radio1 = Radiobutton(test_frm, text="test1", value=2, variable=test_var)

test_radio.pack(side="left")
test_en.pack(side="left")
test_radio1.pack(side="top")





# Label(root, text="메뉴를 선택하세요").pack()

# burger_var = IntVar() # int 형으로 값을 저장
# btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# test = Entry(root,)
# btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
# btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()

# Label(root, text="음료를 선택하세요").pack()

# drink_var = StringVar()
# btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
# btn_drink1.select()
# btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
# btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

# btn_drink1.pack()
# btn_drink2.pack()
# btn_drink2.pack()

# def btncmd() :

#     print(burger_var.get())
#     print(drink_var.get())


# btn = Button(root, text="주문", command=btncmd)
# btn.pack()


root.mainloop()