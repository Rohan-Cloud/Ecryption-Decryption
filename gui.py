from tkinter import *
from tkinter import filedialog
import os

a=Tk()
a.title="ENCRYPTON-DECRYPTION"
a.geometry("500x600")



def mfileSourceopen():
    file= filedialog.askopenfile()
    file1=file.name
    global fil1
    fil1=str(os.path.basename(file1))    

def mfileDestinationopen():
    file = filedialog.askopenfile()
    file2=file.name
    global fil2
    fil2=str(os.path.basename(file2))


def Encrypt():
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890!@#$%^&*()_+{}:<>?-=.,;][\n "

    with open(fil1,'r') as f:
        a=f.read()
        print(a)
    key = 30
    lenalph=int(len(alphabet))
    
    newmsg=""

    for ch in a:
        position = alphabet.find(ch)
        newposition=(position-key)%lenalph
        newchar=alphabet[newposition]
        newmsg+=newchar

    with open(fil2,'w') as fw:
        fw.write(newmsg)

    print("decrypted Msg is :\n",newmsg);

def Decrypt():
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890!@#$%^&*()_+{}:<>?-=.,;][\n " 

    with open(fil1,'r') as f:
        a=f.read()
        print(a)
    key = 30
    lenalph=int(len(alphabet))
    
    newmsg=""

    for ch in a:
        position = alphabet.find(ch)
        newposition=(position+key)%lenalph
        newchar=alphabet[newposition]
        newmsg+=newchar

    with open(fil2,'w') as fw:
        fw.write(newmsg)

    print("decrypted Msg is :\n",newmsg);
    



    



button1 = Button(a,text="select Source file",width=30,command=mfileSourceopen).pack()

button2 =Button(a,text="select Destination File",width=30,command=mfileDestinationopen).pack()

button3=Button(a,text="Encrypt File", width=15,command=Encrypt,bg="red",fg="black").pack()

button4=Button(a,text="Decrypt File", width=15,command=Decrypt,bg="red",fg="black").pack()

a.mainloop()
