import socket
import random
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 7510
    s.bind((host,port))
    s.listen(5)
    c,ad = s.accept()
    print('Connection Established with: '+ad[0])
    words = ['black','violet','blue','green','yellow','orange','red','pink','white']
    start = True
    randomWord = ''
    sentWord = ''
    while True:
        if(start):
            randomWord = words [random.randint(0,len(words)-1)]
            sentWord = "-"*len(randomWord)
            c.send(sentWord.encode('ascii'))
            start = False
        else:
            ltrRecieved = c.recv(2048).decode('ascii')
            if(ltrRecieved == 'reset'):
                start = True
                randomWord = ''
                sentWord = ''
            else:    
                index = []
                newStr = ''
                if (randomWord.find(ltrRecieved) != -1):
                    for i in range(0,len(randomWord)):
                        if(ltrRecieved == randomWord[i]):
                            newStr += ltrRecieved
                        else :
                            newStr += sentWord[i]
                    sentWord = newStr
                    c.send(sentWord.encode('ascii'))
                else :
                    c.send('False'.encode('ascii'))     
    s.close()
except socket.error as e :
    print(e)
except KeyboardInterrupt :
    print('chat ended')