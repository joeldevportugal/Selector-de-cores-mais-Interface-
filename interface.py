# importar as Livrarias a usar ------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import threading
#------------------------------------------------------------------------------------------------------------------------




#Cria as Cores a Usar ---------------------------------------------------------------------------------------------------
co1='#ffffff'
co2='#eef5e7'
co3='#000000'
co4='#f2f3f5'
co5='#f2f3ea'
co6='#ff0000'
co7='#008d00'
co8='#0000ff'
#-------------------------------------------------------------------------------------------------------------------------
# configurar a Janela ----------------------------------------------------------------------------------------------------
janela = Tk()
janela.geometry('600x230+100+100')
janela.resizable(0,0)
janela.title('Selector de cores em Tkinter Dev Joel 2024 PT  interface ©')
janela.config(bg=co1)
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\Selector de Cores\\icon.ico')
#-------------------------------------------------------------------------------------------------------------------------
# criar O label Cor ------------------------------------------------------------------------------------------------------
Lcor= Label(janela, width=33, height=10, bg=co3)
Lcor.place(x=10, y=10)
#-------------------------------------------------------------------------------------------------------------------------
# cria o Label Vermelho e o Svermelho ------------------------------------------------------------------------------------
Lvermelho= Label(janela, text='Reed', font=('arial 13 bold'), bg=co1, fg=co6)
Lvermelho.place(x=260, y=10)
Svermelho = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255)
Svermelho.place(x=310, y=10)
#------------------------------------------------------------------------------------------------------------------------
# criar O label Verde e o Sverde ----------------------------------------------------------------------------------------
Lverde= Label(janela, text='Green', font=('arial 13 bold'), bg=co1, fg=co7)
Lverde.place(x=250, y=60)
Sverde = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255)
Sverde.place(x=310, y=60)
#-----------------------------------------------------------------------------------------------------------------------
# criar o Label e o Sazul ---------------------------------------------------------------------------------------------- 
LAzul= Label(janela, text='Blue', font=('arial 13 bold'), bg=co1, fg=co8)
LAzul.place(x=260, y=120)
SAzul = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255)
SAzul.place(x=310, y=120)
#-----------------------------------------------------------------------------------------------------------------------
# criar Os compunetes de Hexadecimal -----------------------------------------------------------------------------------
EHexa= Entry(janela, bg=co4, font=('arial 14 bold'), width=11,)
EHexa.place(x=10, y=184)
BcopiarHexa= Button(janela, text='Copiar Hexa', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1)
BcopiarHexa.place(x=140, y=184)
#------------------------------------------------------------------------------------------------------------------------
# criar Os compunentes RGB ----------------------------------------------------------------------------------------------
ERGB= Entry(janela, bg=co4, font=('arial 14 bold'), width=11,)
ERGB.place(x=220, y=184)
BcopiarRGB= Button(janela, text='Copiar RGB', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1)
BcopiarRGB.place(x=350, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# criar O botão Limpar ---------------------------------------------------------------------------------------------------------------
BLimpar= Button(janela, text='Limpar Codico', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1)
BLimpar.place(x=425, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# criar o botão Fechar ---------------------------------------------------------------------------------------------------------------
BFechar= Button(janela, text='Fechar', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1, )
BFechar.place(x=520, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# iniciar a Nossa Janela -------------------------------------------------------------------------------------------------------------
janela.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------