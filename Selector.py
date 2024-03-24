# importar as Livrarias a usar ------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import threading
#------------------------------------------------------------------------------------------------------------------------
# função para Actualizar Cor --------------------------------------------------------------------------------------------
def atualiza_cor(val):
    # Obtém os valores atuais dos sliders
    r = Svermelho.get()
    g = Sverde.get()
    b = SAzul.get()
    
    # Converte os valores para uma string hexadecimal de cor
    cor_hex = f'#{r:02x}{g:02x}{b:02x}'
    
    # Atualiza a cor de fundo do Lcor
    Lcor['bg'] = cor_hex
    
    # Atualiza os componentes RGB e Hexadecimal
    EHexa.delete(0, END)
    EHexa.insert(0, cor_hex.upper())
    ERGB.delete(0, END)
    ERGB.insert(0, f'{r}, {g}, {b}')
#------------------------------------------------------------------------------------------------------------------------
# Função para copiar o texto para a área de transferência----------------------------------------------------------------
def copiar_hexa():
    texto = EHexa.get()
    janela.clipboard_clear()  # Limpa a área de transferência
    janela.clipboard_append(texto)  # Adiciona o texto à área de transferência
    # Para garantir que o texto fique na área de transferência após o fechamento da aplicação,
    # alguns sistemas podem requerer o uso de janela.clipboard_append(texto) novamente.
    janela.update()  # Atualiza a janela para processar a mudança na área de transferência
    messagebox.showinfo('Codigo','O seu codigo foi copiado com sucesso!...')
#------------------------------------------------------------------------------------------------------------------------
# criar a função para Copiar codigo RGB ---------------------------------------------------------------------------------
def copiar_RGB():
    texto = ERGB.get()
    janela.clipboard_clear()  # Limpa a área de transferência
    janela.clipboard_append(texto)  # Adiciona o texto à área de transferência
    # Para garantir que o texto fique na área de transferência após o fechamento da aplicação,
    # alguns sistemas podem requerer o uso de janela.clipboard_append(texto) novamente.
    janela.update()  # Atualiza a janela para processar a mudança na área de transferência
    messagebox.showinfo('Codigo','O seu codigo foi copiado com sucesso!...')
#-----------------------------------------------------------------------------------------------------------------------
# criar a função Limpar O codico ---------------------------------------------------------------------------------------
def Limpar():
   # Limpar os campos de Entry
    EHexa.delete(0, END)
    ERGB.delete(0, END)
    
    # Ajustar os sliders para 0
    Svermelho.set(0)
    Sverde.set(0)
    SAzul.set(0)
    
    # Opcionalmente, atualizar a cor de fundo do Lcor para preto (ou outra cor de reset)
    Lcor['bg'] = '#000000'  # Aqui escolhi preto como cor de reset
    
    # Atualizar os campos Hexa e RGB para refletir a limpeza
    EHexa.insert(0, '#000000')
    ERGB.insert(0, '0, 0, 0')

    messagebox.showinfo('Valores','Valores Limpos Com sucesso!...')
#-----------------------------------------------------------------------------------------------------------------------
# Função fechar a janela -----------------------------------------------------------------------------------------------
def fechar():
    if messagebox.askyesno("Fechar Programa", "Deseja realmente fechar o programa?Sim/Nao"):  # Passo 3
        janela.destroy()  # Fecha a janela
    else:
        return  # Retorna ao programa, não faz nada
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
janela.title('Selector de cores em Tkinter Dev Joel 2024 PT ©')
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
Svermelho = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255, command=atualiza_cor)
Svermelho.place(x=310, y=10)
#------------------------------------------------------------------------------------------------------------------------
# criar O label Verde e o Sverde ----------------------------------------------------------------------------------------
Lverde= Label(janela, text='Green', font=('arial 13 bold'), bg=co1, fg=co7)
Lverde.place(x=250, y=60)
Sverde = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255, command=atualiza_cor)
Sverde.place(x=310, y=60)
#-----------------------------------------------------------------------------------------------------------------------
# criar o Label e o Sazul ---------------------------------------------------------------------------------------------- 
LAzul= Label(janela, text='Blue', font=('arial 13 bold'), bg=co1, fg=co8)
LAzul.place(x=260, y=120)
SAzul = Scale(janela, orient=HORIZONTAL, bg=co1, length=280, from_=0, to=255, command=atualiza_cor)
SAzul.place(x=310, y=120)
#-----------------------------------------------------------------------------------------------------------------------
# criar Os compunetes de Hexadecimal -----------------------------------------------------------------------------------
EHexa= Entry(janela, bg=co4, font=('arial 14 bold'), width=11,)
EHexa.place(x=10, y=184)
BcopiarHexa= Button(janela, text='Copiar Hexa', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1, command=copiar_hexa)
BcopiarHexa.place(x=140, y=184)
#------------------------------------------------------------------------------------------------------------------------
# criar Os compunentes RGB ----------------------------------------------------------------------------------------------
ERGB= Entry(janela, bg=co4, font=('arial 14 bold'), width=11,)
ERGB.place(x=220, y=184)
BcopiarRGB= Button(janela, text='Copiar RGB', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1, command=copiar_RGB)
BcopiarRGB.place(x=350, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# criar O botão Limpar ---------------------------------------------------------------------------------------------------------------
BLimpar= Button(janela, text='Limpar Codico', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1,command=Limpar)
BLimpar.place(x=425, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# criar o botão Fechar ---------------------------------------------------------------------------------------------------------------
BFechar= Button(janela, text='Fechar', font=('arial 8 bold'), height=1, relief=RAISED, overrelief=RIDGE, bg=co1, command=fechar)
BFechar.place(x=520, y=184)
#-------------------------------------------------------------------------------------------------------------------------------------
# iniciar a Nossa Janela -------------------------------------------------------------------------------------------------------------
janela.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------