from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox

from tkinter import filedialog as fd

#impotando imagem da pillow-----------------------------------------------
from PIL import Image, ImageTk

#importando calendario tk---------------------------------------------
from tkcalendar import Calendar, DateEntry 
from datetime import date

# importando view--------------------------------------------------
from view import *

#cores---------------------------------------------------------------

co0 = "#2e2d2b" #PRETA
co1 = "#feffff" #BRANCA
co2 = "#4fa882" #VERDE
co3 = "#38576b" #VALOR
co4 = "#403d3d" #LETRA
co5 = "#e06636" #- profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" #+ verde
co9 = "#e9edf5" #+ verde

#CRIANDO JANELA----------------------------------------------------

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


#CRIANDO FRAMES------------------------------------------------------------

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)


frameMeio = Frame(janela, width=1043, height=303, bg=co1,pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0,padx=1, sticky=NSEW)


#criando funçoes---------------------------------------------------------
global tree
b_confirmar = None

#Funcao inserir------------------------------------------------------------

def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    date = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, date, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos')

    e_nome.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serie.delete(0, 'end')


    mostrar()


#funçao atualizar-----------------------------------------------------------------------
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_local.delete(0,'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serie.delete(0, 'end')


        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0,treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0,treev_lista[6])
        e_serie.insert(0,treev_lista[7])
        imagem_string = treev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            date = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_serie.insert(0,treev_lista[7])

            lista_atualizar = [nome, local, descricao, model, date, valor, serie, imagem,id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_local.delete(0,'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serie.delete(0, 'end')
             
            mostrar()  # recarrega a Treeview-----------

        
    except Exception as e:
        messagebox.showerror('Erro', 'Selecione um item na tabela')


    global b_confirmar

    

    if b_confirmar != None:
        b_confirmar.destroy()
        

    b_confirmar = Button(frameMeio,command=update,width=13,text='Confirmar'.upper(),overrelief=RIDGE,font=('Ivy 8 bold'),bg=co2,fg=co1)

    b_confirmar.place(x=330, y=185)


#funçao Deletar-----------------------------------------------------------------------
def deletar():
    
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]


        deletar_form([valor])

        messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')
     
        mostrar()
    
        
    except Exception as e:
        messagebox.showerror('Erro', 'Selecione um item na tabela')


# Funcao para escolher imagem-----------------------------------------------------------------------------------------
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1,fg=co4)
    l_imagem.place(x=700, y=10)

#função para ver imagem--------------------------------------------------------------------

def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)
    imagem = item[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((175,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem,bg=co1,fg=co4)
    l_imagem.place(x=700, y=10)

    
#ABRINDO IMAGEM-------------------------------------------------------------
app_img = Image.open('icons8-agenda-64.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventario Domestico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1,fg=co4)
app_logo.place(x=0, y=0)


#CRIANDO ENTRADAS------------------------------------------------------------
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Sala/Area', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)


l_descricao = Label(frameMeio, text='Descricao', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)


l_model = Label(frameMeio, text='Marca/Modelo', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_model.place(x=130, y=101)


l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12,Background='darkblue',bordwidth=2,year=2026)
e_cal.place(x=130, y=131)


l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_valor.place(x=130, y=161)


l_serie = Label(frameMeio, text='Numero de serie', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_serie.place(x=130, y=191)

#criando botoes------------------------------------------------------------------

#botao carregar

l_carregar = Label(frameMeio, text='Imagem Item', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_carregar.place(x=10, y=220)

b_carregar = Button(frameMeio,command=escolher_imagem,width=30, text='carregar'.upper(),compound=CENTER, anchor=CENTER,overrelief=RIDGE,font=('Ivy 8 bold'), bg=co1, fg=co0 )
b_carregar.place(x=130, y=221)

# botao inserir

b_inserir = Button(frameMeio,command=inserir,width=15, text='Inserir'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE,font=('Ivy 8 bold'), bg=co1, fg=co0 )
b_inserir.place(x=330, y=10)

#botao atualizar

b_update = Button(frameMeio,command=atualizar,width=15, text='Atualizar'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE,font=('Ivy 8 bold'), bg=co1, fg=co0 )
b_update.place(x=330, y=50)

#botao deletar

b_delete = Button(frameMeio,command=deletar,width=15, text='Deletar'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE,font=('Ivy 8 bold'), bg=co1, fg=co0 )
b_delete.place(x=330, y=90)

#botao ver imagem
b_item = Button(frameMeio,command=ver_imagem,width=15, text='Ver item'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE,font=('Ivy 8 bold'), bg=co1, fg=co0 )
b_item.place(x=360, y=221)


#Labels Quantidade Total e Valores--------------------------------------------------

# Valor total

l_total_valor = Label(frameMeio, text='', width=14, height=2,
                      anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total_valor.place(x=450, y=17)

l_total_texto = Label(frameMeio, text='   Valor total de todos os itens  ',
                      height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_texto.place(x=450, y=12)

# Quantidade----------------------

l_qtd_valor = Label(frameMeio, text='', width=14, pady=5, height=2,
                    anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd_valor.place(x=450, y=90)

l_qtd_texto = Label(frameMeio, text='  Quantidade total de itens  ',
                    height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_texto.place(x=450, y=92)


#tabela---------------------------------------------------------
def mostrar():
    global tree

#Criando tabela------------------------------------
    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total_valor['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd_valor['text'] = Total_itens

mostrar()

janela.mainloop()

