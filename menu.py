from tkinter import *

root = Tk()
root.title("GUI_test") # GUI 타이틀

root.geometry("600x400+300+300") # 가로 x 세로 + 창위치 x 값 , 창위차 y 값
root.resizable(False, False) # x , y 값 변경 불가 설정

def create_new_file() :
    print("새 파일을 만듭니다")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Windows")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴 ( 빈 값 )
menu.add_cascade(label="Edit")

# radio 메뉴
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)


# 체크박스 메뉴

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)

root.mainloop()