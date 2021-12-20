from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") #padx, pady는 버튼 가로세로가 넓어짐
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3") #왼쪽 오른쪽 공간, 위 아래 공간을 더 사용
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") #width, height는 버튼의 크기 일정함
btn4.pack()

btn5 = Button(root, fg="red", bg='yellow', text="버튼5") 
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()