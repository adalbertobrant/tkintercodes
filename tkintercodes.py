from tkinter import *

# Classe Janela com a propriedade title -> título da janela
class Janela:
    def __init__(self,mestre):
# liga o self.mestre -> mestre
        self.mestre = mestre
        mestre.title("Main Window")

# cria a variável root que tem as propriedades da classe Tk()
root = Tk()
# imprime na tela o tipo de root - root é do tipo classe tkinter.tk
print(type(root))
wdw = Janela(root)
# propriedade __main__ -> da classe Janela herdada da classe Tk()
print(type(wdw))
# mudança do título que estava dentro da classe Janela
root.title("New Title")
root.mainloop()



