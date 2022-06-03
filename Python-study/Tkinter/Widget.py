from tkinter import *

# window = Tk()
# # 레이블 : 문자를 표현할 수 있는 위젯
# # 레이블에 글자 대신 이미지 넣기
# photo = PhotoImage(file = "C:/Users/user/Downloads/dog3.gif")
# label1 = Label(window, image = photo)

# label1.pack()

# window.mainloop()

btnList = [None] * 9
fnameList = ["C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif", "C:/Users/user/Downloads/dog3.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file= "C:/Users/user/Downloads/dog3.gif" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()