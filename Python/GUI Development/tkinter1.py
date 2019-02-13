from tkinter import *

root = Tk(screenName='Window1', baseName='Window2')
# label = Label(root, text='hi world')
# label.pack()

root.title('Hello World')
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Button 1', fg='red')
button2 = Button(topFrame, text='Button 2', fg='green')

button3 = Button(bottomFrame, text='Button 3', fg='orange')
button4 = Button(bottomFrame, text='Button 4', fg='black')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

root.mainloop()
