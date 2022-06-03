# Tkinter는 파이썬을 설치할 때 기본적으로 함께 설치가 되는 파이썬 GUI 제공 모듈
# Tkinter는 GUI를 위한 클래스 포함
# Tcl/Tk언어를 파이썬에서 사용할 수 있게 해줌
# Tkinter를 사용하기 위해서는 Tkinter 모듈을 import. 모듈 내의Tk() 함수로 Tk 클래스 객체를 생성한다.
# Tkinter는 레이블, 버튼, 엔트리, 캔버스, 스크롤바, 이미지 등의 위젯을 제공한다.

# Tkinter 모듈 import 방식
import tkinter as tk
w = tk.Tk()

l = tk.Label(w, text = "안녕하세요")
b = tk.Button(w, text = "확인")
l.pack()
b.pack()

w.mainloop()