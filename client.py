import tkinter
from PIL import ImageTk, Image
from functools import partial
import socket
import _thread
import time
client = 0
livesRemaining = 6
def sendChosenLetter (ltr):
    client.send(ltr.encode('ascii'))
           
def resetButton():
    client.send('reset'.encode('ascii'))
    global livesRemaining
    livesRemaining = 6
    time.sleep(2)
    lives.text='Lives Remaining: '+str(livesRemaining)
    
    
def displayRemainingLives (livesRemaining):
    lives['text']='Lives Remaining: '+str(livesRemaining)
    if (livesRemaining == 6):
        img = ImageTk.PhotoImage(Image.open("0.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 5):
        img = ImageTk.PhotoImage(Image.open("1.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 4):
        img = ImageTk.PhotoImage(Image.open("2.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 3):
        img = ImageTk.PhotoImage(Image.open("3.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 2):
        img = ImageTk.PhotoImage(Image.open("4.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 1):
        img = ImageTk.PhotoImage(Image.open("5.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
    elif (livesRemaining == 0):
        img = ImageTk.PhotoImage(Image.open("6.png"))
        imageLabel = tkinter.Label(window,image=img)
        imageLabel.image=img
        imageLabel.grid(column=6,rowspan=6,row=1,padx=20,pady=0)
        lives['text']='YOU LOST'
        resetButton()
            
def socketCreation():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 7510
    c.connect((host,port))
    global client
    client = c
    global livesRemaining
    while True:
        displayRemainingLives(livesRemaining)
        msg= c.recv(2048).decode('ascii')
        if(msg == 'False'):
            livesRemaining -= 1
            displayRemainingLives(livesRemaining)
        elif(msg.find('-') != -1):
            wordLBL['text'] = msg
        elif(msg.find('-') == -1 and livesRemaining > 0):
            lives['text']='YOU WON !!'
            wordLBL['text'] = msg
            resetButton()
#Creating a window
window = tkinter.Tk()
window.title("Hangman")
window['bg']='white'
window['padx']=15
window['pady']=15
#Word To Guess
wordLBL = tkinter.Label(window)
wordLBL['font']=("",25)
wordLBL['bg']='white'
wordLBL.grid(columnspan=3,column=2,row=0,padx=5,pady=5)
#wordLBL
lives = tkinter.Label(window)
lives['font']=("",25)
lives['bg']='white'
lives.grid(column=6,row=0,padx=5,pady=5)

for i in range(26):
    btn = tkinter.Button(window,text=chr(97+i),command=partial(sendChosenLetter,chr(97+i)))
    btn['relief']=tkinter.GROOVE
    btn['bg']='white'
    btn['font']=25
    btn['width']= 6
    btn['height']= 3
    btn.grid(column=(i%5)+1,row=int(i/5)+1,padx=5,pady=5)
resetBtn = tkinter.Button(window,text='RESET',command=resetButton)
resetBtn['relief']=tkinter.GROOVE
resetBtn['bg']='white'
resetBtn['font']=25
resetBtn['width']= 15
resetBtn['height']= 3
resetBtn.grid(columnspan=2,column=4,row=6,padx=5,pady=5)
#Socket Thread
    
_thread.start_new_thread(socketCreation, () )
window.mainloop()