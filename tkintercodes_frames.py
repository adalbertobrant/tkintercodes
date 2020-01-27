from tkinter import *


class MyFrame(Frame):
    def __init__(self , parent):
        Frame.__init__(self , parent)
        self.text=Label(self , text='Name')
        self.text.pack()
        vcmd=parent.register(self.validate)

        self.variavel=StringVar()

        self.name=Entry(self , textvariable=self.variavel , validate='key' , validatecommand=(vcmd , '%P'))
        self.name.pack()
        self.name.focus_set()
        self.variavel.trace("w" , self.show_choices)
        self.submit=Button(self , text='Submit' , width=10 , state=DISABLED , command=self.callback)
        self.submit.pack()
        self.entered=Label(self , text='You entered: ')
        self.entered.pack()
        self.cpf_char=[ ]

    def show_choices(self , *dummy):
        cara=self.variavel.get()

    def callback(self):
        self.entered.config(text='You entered: ' + self.name.get())
        self.name.delete(0 , END)

    def validate(self , P):
        self.submit.config(state=(NORMAL if P else DISABLED))
        #avaliar se P é um número e adicionar no self.conta_char e retornar o P + "/" ou "."
        if P.isnumeric():
            self.conta_char=P
            return P + "/"


root=Tk()
frame=MyFrame(root)
frame.pack()
root.mainloop()