import time
from threading import Thread
import socket
import tkinter

def save():
    global HOST 
    global PORT
    global NAME
    global PORT2
    HOST = ent1.get()
    PORT = int(ent2.get())
    NAME = ent3.get()
    if ent4.get()=='':
        PORT2=5353
    PORT2 = int(ent4.get())
    label3.configure(text='Attempting to connect..')
    startconnection()
    
def startconnection():
    t = Thread(target=server, args=())
    t.start()
    t = Thread(target=client, args=())
    t.start()
    return
       
def client():
    global c
    while True:
        try:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((HOST,PORT))
            break
        except socket.error:
            label3.configure(text='Trying to reconnect..')
    t = Thread(target=chatf, args=())
    t.start()
    return

def server():
    HOST2= ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST2,PORT2))
    except TypeError:
        label3.configure(text='Wrong IP or PORT!')
        return
    s.listen(0)
    conn, addr = s.accept()
    while 1:
        data = conn.recv(1024)
        if not data: break
        ordenchat(data.decode())
    conn.close()
    return

def chatf():
      top.destroy()
      return

def ordenchat(mensaje):
    chatarray = [lbl1.cget('text'), lbl2.cget('text') , lbl3.cget('text') , lbl4.cget('text') , lbl5.cget('text'), mensaje]
    lbl5.configure(text=chatarray[5])
    lbl4.configure(text=chatarray[4])
    lbl3.configure(text=chatarray[3])
    lbl2.configure(text=chatarray[2])
    lbl1.configure(text=chatarray[1])
    lbl0.configure(text=chatarray[0])
    return
def send():
    mensaje = str(ent0.get())
    try:
        message = c.sendall(mensaje.encode())
        ent0.delete(0, 100)
        ordenchat(mensaje)
        return
    except socket.error:
        client()
        return

while True:
    while 1:
        top = tkinter.Tk()
        top.title('Made by Mancos for Mancos')
        top.geometry('450x300')
        top.configure(background='#a1dbcd')

        fr0 = tkinter.Frame(top,bg='#a1dbcd')
        fr1 = tkinter.Frame(top,bg='#a1dbcd')
        fr2 = tkinter.Frame(top,bg='#a1dbcd')
        fr3 = tkinter.Frame(top,bg='#a1dbcd')
        fr4 = tkinter.Frame(top,bg='#a1dbcd')
        fr5 = tkinter.Frame(top,bg='#a1dbcd')
        fr6 = tkinter.Frame(top,bg='#a1dbcd')
        fr7 = tkinter.Frame(top,bg='#a1dbcd')
        fr8 = tkinter.Frame(top,bg='#a1dbcd')


        label01 = tkinter.Label(fr0,text='',bg='#a1dbcd')
        label0 = tkinter.Label(fr1,text='Username: ',bg='#a1dbcd')
        label11 = tkinter.Label(fr2,text='',bg='#a1dbcd')
        label1 = tkinter.Label(fr2,text='    IP:          ',bg='#a1dbcd')
        label21 = tkinter.Label(fr3,text='',bg='#a1dbcd')
        label2 = tkinter.Label(fr4,text='PORT:        ',bg='#a1dbcd')
        label3 = tkinter.Label(fr5,text='',bg='#a1dbcd')
        label4 = tkinter.Label(fr6,text='Your port:  ',bg='#a1dbcd')
        label5 = tkinter.Label(fr7,text='',bg='#a1dbcd')
        label6 = tkinter.Label(fr8,text='           --> ',bg='#a1dbcd')

        ent1 = tkinter.Entry(fr2)
        ent2 = tkinter.Entry(fr4)
        ent3 = tkinter.Entry(fr1)
        ent4 = tkinter.Entry(fr6)

        boton1= tkinter.Button(fr8, text='Connect!', fg='#a1dbcd', bg='#383a39', command=save)

        fr0.pack()
        label01.pack()
        fr1.pack(side='top')
        label0.pack(side='left')
        ent3.pack(side='left')
        fr2.pack(side='top')
        label11.pack()
        label1.pack(side='left')
        ent1.pack(side='left')
        fr3.pack()
        label21.pack()
        label2.pack(side='left')
        ent2.pack(side='left')
        fr4.pack()
        label3.pack()
        fr5.pack()
        label4.pack(side='left')
        ent4.pack(side='left')
        fr6.pack()
        label5.pack()
        fr7.pack()
        label6.pack(side='left')
        boton1.pack(side='left')
        fr8.pack()
        top.mainloop()
        break
    while 1:
        chat = tkinter.Tk()
        chat.title('Made by Mancos for Mancos')
        chat.geometry('512x220')
        chat.configure(background='#a1dbcd')

        global chatarray
        chatarray= ['','','','','','']
        
        f1 = tkinter.Frame(chat, bg='white')
        f2 = tkinter.Frame(chat, bg='white')
        f3 = tkinter.Frame(chat, bg='white')
        f4 = tkinter.Frame(chat, bg='white')
        f5 = tkinter.Frame(chat, bg='white')
        f6 = tkinter.Frame(chat, bg='white')
        f7 = tkinter.Frame(chat, bg='#a1dbcd')
        
        lbl0 = tkinter.Label(f1,text='', bg='white')
        lbl1 = tkinter.Label(f2,text='', bg='white')
        lbl2 = tkinter.Label(f3,text='', bg='white')
        lbl3 = tkinter.Label(f4,text='', bg='white')
        lbl4 = tkinter.Label(f5,text='', bg='white')
        lbl5 = tkinter.Label(f6,text='', bg='white')
        lbl6 = tkinter.Label(chat,text='', bg='#a1dbcd')
        
        ent0 = tkinter.Entry(f7)
        boton0 = tkinter.Button(f7, text='Send', bg='#a1dbcd', fg='#383a39', command=send)

        f1.pack(fill='both')
        lbl0.pack(side='left')
        f2.pack(fill='both')
        lbl1.pack(side='left')
        f3.pack(fill='both')
        lbl2.pack(side='left')
        f4.pack(fill='both')
        lbl3.pack(side='left')
        f5.pack(fill='both')
        lbl4.pack(side='left')
        f6.pack(fill='both')
        lbl5.pack(side='left')
        f6.pack()
        lbl6.pack()
        f7.pack()
        ent0.pack(fill='x', side='left')
        boton0.pack(side='right')
        chat.mainloop()
        break
    break
