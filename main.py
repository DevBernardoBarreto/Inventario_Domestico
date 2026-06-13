from tkinter import *
from tkinter import Tk, ttk, messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date

# importando view--------------------------------------------------
from view import *

# Dolar (Importando a função do arquivo servicos.py)
from servicos import obter_cotacao_dolar

# cores---------------------------------------------------------------
co0 = "#2e2d2b"  # PRETA
co1 = "#feffff"  # BRANCA
co2 = "#4fa882"  # VERDE
co3 = "#38576b"  # VALOR
co4 = "#403d3d"  # LETRA
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # verde escuro
co9 = "#e9edf5"  # fundo

# CRIANDO JANELA----------------------------------------------------
janela = Tk()
janela.title("Inventário Doméstico")
janela.geometry("900x600")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# CRIANDO FRAMES------------------------------------------------------------
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# variáveis globais---------------------------------------------------------
tree = None
b_confirmar = None
imagem = None
imagem_string = ""
l_imagem = None


def normalizar_valor(valor_digitado):
    """
    Aceita valores como 1500, 1500.50, 1.500,50 ou 1500,50.
    Retorna o valor padronizado com ponto decimal para salvar no banco/Supabase.
    """
    valor = str(valor_digitado).strip().replace("R$", "").replace(" ", "")

    if not valor:
        raise ValueError("Valor vazio")

    if "," in valor and "." in valor:
        # Formato brasileiro: 1.234,56
        if valor.rfind(",") > valor.rfind("."):
            valor = valor.replace(".", "").replace(",", ".")
        # Formato internacional: 1,234.56
        else:
            valor = valor.replace(",", "")
    elif "," in valor:
        valor = valor.replace(",", ".")

    numero = float(valor)

    if numero < 0:
        raise ValueError("Valor negativo")

    return f"{numero:.2f}"


def obter_item_selecionado():
    if tree is None:
        raise ValueError("Tabela ainda não carregada")

    selecionado = tree.focus()

    if not selecionado:
        raise ValueError("Nenhum item selecionado")

    dados = tree.item(selecionado)
    valores = dados.get("values", [])

    if not valores:
        raise ValueError("Nenhum item selecionado")

    return valores


def obter_imagem_por_id(id_item):
    """
    Busca a imagem diretamente no Supabase. Assim a imagem não precisa ficar
    escondida dentro da tabela visual.
    """
    try:
        item = ver_item(id_item)
        if not item:
            return ""

        primeiro = item[0]

        if isinstance(primeiro, dict):
            return primeiro.get("imagem", "") or ""

        if len(primeiro) > 8:
            return primeiro[8] or ""

        return ""
    except Exception:
        return ""


def limpar_campos():
    global imagem_string, l_imagem

    e_nome.delete(0, "end")
    e_local.delete(0, "end")
    e_descricao.delete(0, "end")
    e_model.delete(0, "end")
    e_valor.delete(0, "end")
    e_serie.delete(0, "end")
    e_cal.set_date(date.today())

    imagem_string = ""

    if l_imagem is not None:
        l_imagem.destroy()
        l_imagem = None


def ler_campos():
    nome = e_nome.get().strip()
    local = e_local.get().strip()
    descricao = e_descricao.get().strip()
    model = e_model.get().strip()
    data_compra = e_cal.get().strip()
    valor = e_valor.get().strip()
    serie = e_serie.get().strip()

    return nome, local, descricao, model, data_compra, valor, serie


# Funcao inserir------------------------------------------------------------
def inserir():
    global imagem_string

    nome, local, descricao, model, data_compra, valor, serie = ler_campos()

    campos_obrigatorios = [nome, local, descricao, model, data_compra, valor, serie]
    for campo in campos_obrigatorios:
        if campo == "":
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios")
            return

    if imagem_string == "":
        messagebox.showerror("Erro", "Selecione uma imagem para o item")
        return

    try:
        valor = normalizar_valor(valor)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor de compra válido. Exemplo: 1500,00")
        return

    lista_inserir = [nome, local, descricao, model, data_compra, valor, serie, imagem_string]

    try:
        inserir_form(lista_inserir)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos")
        limpar_campos()
        mostrar()
    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível inserir os dados.\nDetalhe: {erro}")


# função atualizar-----------------------------------------------------------------------
def atualizar():
    global imagem_string, b_confirmar

    try:
        treev_lista = obter_item_selecionado()
        id_item = int(treev_lista[0])

        e_nome.delete(0, "end")
        e_local.delete(0, "end")
        e_descricao.delete(0, "end")
        e_model.delete(0, "end")
        e_valor.delete(0, "end")
        e_serie.delete(0, "end")

        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.set_date(treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serie.insert(0, treev_lista[7])

        imagem_string = obter_imagem_por_id(id_item)

    except Exception:
        messagebox.showerror("Erro", "Selecione um item na tabela")
        return

    def update():
        global imagem_string, b_confirmar

        nome, local, descricao, model, data_compra, valor, serie = ler_campos()

        campos_obrigatorios = [nome, local, descricao, model, data_compra, valor, serie]
        for campo in campos_obrigatorios:
            if campo == "":
                messagebox.showerror("Erro", "Preencha todos os campos obrigatórios")
                return

        if imagem_string == "":
            messagebox.showerror("Erro", "Selecione uma imagem para o item")
            return

        try:
            valor = normalizar_valor(valor)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor de compra válido. Exemplo: 1500,00")
            return

        lista_atualizar = [nome, local, descricao, model, data_compra, valor, serie, imagem_string, id_item]

        try:
            atualizar_(lista_atualizar)
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso")
            limpar_campos()

            if b_confirmar is not None:
                b_confirmar.destroy()
                b_confirmar = None

            mostrar()
        except Exception as erro:
            messagebox.showerror("Erro", f"Não foi possível atualizar os dados.\nDetalhe: {erro}")

    if b_confirmar is not None:
        b_confirmar.destroy()

    b_confirmar = Button(
        frameMeio,
        command=update,
        width=13,
        text="Confirmar".upper(),
        overrelief=RIDGE,
        font=("Ivy 8 bold"),
        bg=co2,
        fg=co1,
    )
    b_confirmar.place(x=330, y=185)


# função Deletar-----------------------------------------------------------------------
def deletar():
    try:
        treev_lista = obter_item_selecionado()
        id_item = int(treev_lista[0])
        nome_item = treev_lista[1]
    except Exception:
        messagebox.showerror("Erro", "Selecione um item na tabela")
        return

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Tem certeza que deseja deletar o item '{nome_item}'?"
    )

    if not confirmar:
        return

    try:
        deletar_form(id_item)
        messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")
        mostrar()
    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível deletar o item.\nDetalhe: {erro}")


# Funcao para escolher imagem-----------------------------------------------------------------------------------------
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    caminho_imagem = fd.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("Todos os arquivos", "*.*"),
        ],
    )

    if not caminho_imagem:
        return

    try:
        imagem_string = caminho_imagem

        imagem_aberta = Image.open(caminho_imagem)
        imagem_aberta = imagem_aberta.resize((170, 170))
        imagem = ImageTk.PhotoImage(imagem_aberta)

        if l_imagem is not None:
            l_imagem.destroy()

        l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=700, y=10)

    except Exception:
        imagem_string = ""
        messagebox.showerror("Erro", "Não foi possível carregar a imagem selecionada")


# função para ver imagem--------------------------------------------------------------------
def ver_imagem():
    global imagem, l_imagem

    try:
        treev_lista = obter_item_selecionado()
        id_item = int(treev_lista[0])
        caminho_imagem = obter_imagem_por_id(id_item)

        if not caminho_imagem:
            messagebox.showwarning("Imagem", "Este item não possui imagem cadastrada")
            return

        imagem_aberta = Image.open(caminho_imagem)
        imagem_aberta = imagem_aberta.resize((175, 170))
        imagem = ImageTk.PhotoImage(imagem_aberta)

        if l_imagem is not None:
            l_imagem.destroy()

        l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=700, y=10)

    except Exception:
        messagebox.showerror("Erro", "Selecione um item válido ou verifique se a imagem ainda existe no computador")


def buscar():
    termo = e_busca.get().strip().lower()

    if termo == "":
        mostrar()
        return

    try:
        lista_itens = ver_form()
        filtrados = []

        for item in lista_itens:
            texto_item = " ".join(str(campo).lower() for campo in item[:8])
            if termo in texto_item:
                filtrados.append(item)

        mostrar(filtrados)
    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível realizar a busca.\nDetalhe: {erro}")


def exportar_csv():
    try:
        lista_itens = ver_form()

        if not lista_itens:
            messagebox.showwarning("Exportar", "Não há itens para exportar")
            return

        caminho = fd.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivo CSV", "*.csv")],
            title="Salvar relatório do inventário",
            initialfile="inventario_domestico.csv",
        )

        if not caminho:
            return

        with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([
                "ID",
                "Nome",
                "Sala/Área",
                "Descrição",
                "Marca/Modelo",
                "Data da compra",
                "Valor da compra",
                "Número de série",
                "Imagem",
            ])
            escritor.writerows(lista_itens)

        messagebox.showinfo("Exportar", "Relatório exportado com sucesso")

    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível exportar o relatório.\nDetalhe: {erro}")


# import csv após as funções auxiliares da interface
import csv


# ABRINDO IMAGEM-------------------------------------------------------------
try:
    app_img = Image.open("icons8-agenda-64.png")
    app_img = app_img.resize((45, 45))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(
        frameCima,
        image=app_img,
        text=" Inventário Doméstico",
        width=900,
        compound=LEFT,
        relief=RAISED,
        anchor=NW,
        font=("Verdana 20 bold"),
        bg=co1,
        fg=co4,
    )
except Exception:
    app_logo = Label(
        frameCima,
        text=" Inventário Doméstico",
        width=900,
        relief=RAISED,
        anchor=NW,
        font=("Verdana 20 bold"),
        bg=co1,
        fg=co4,
    )

app_logo.place(x=0, y=0)


# CRIANDO ENTRADAS------------------------------------------------------------
l_nome = Label(frameMeio, text="Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text="Sala/Área", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text="Descrição", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text="Marca/Modelo", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(frameMeio, text="Data da compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background="darkblue", bordwidth=2, year=2026)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text="Valor da compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(frameMeio, text="Número de série", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_serie.place(x=130, y=191)

# criando botoes------------------------------------------------------------------
l_carregar = Label(frameMeio, text="Imagem Item", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)

b_carregar = Button(
    frameMeio,
    command=escolher_imagem,
    width=30,
    text="Carregar".upper(),
    compound=CENTER,
    anchor=CENTER,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_carregar.place(x=130, y=221)

b_inserir = Button(
    frameMeio,
    command=inserir,
    width=15,
    text="Inserir".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_inserir.place(x=330, y=10)

b_update = Button(
    frameMeio,
    command=atualizar,
    width=15,
    text="Atualizar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_update.place(x=330, y=50)

b_delete = Button(
    frameMeio,
    command=deletar,
    width=15,
    text="Deletar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_delete.place(x=330, y=90)

b_limpar = Button(
    frameMeio,
    command=limpar_campos,
    width=15,
    text="Limpar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_limpar.place(x=330, y=130)

b_item = Button(
    frameMeio,
    command=ver_imagem,
    width=15,
    text="Ver item".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_item.place(x=360, y=221)


# Labels Quantidade Total e Valores--------------------------------------------------
# Aqui ficou tudo em um único Label para não ter texto em cima do valor.
l_total_valor = Label(
    frameMeio,
    text="",
    width=25,
    height=4,
    anchor=CENTER,
    justify=CENTER,
    font=("Ivy 10 bold"),
    bg=co7,
    fg=co1,
)
l_total_valor.place(x=450, y=12)

l_qtd_valor = Label(
    frameMeio,
    text="",
    width=25,
    height=4,
    anchor=CENTER,
    justify=CENTER,
    font=("Ivy 10 bold"),
    bg=co7,
    fg=co1,
)
l_qtd_valor.place(x=450, y=90)

# Busca e exportação---------------------------------------------------------
l_busca = Label(frameMeio, text="Buscar item", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_busca.place(x=450, y=160)

e_busca = Entry(frameMeio, width=22, justify="left", relief=SOLID)
e_busca.place(x=540, y=161)

b_buscar = Button(
    frameMeio,
    command=buscar,
    width=10,
    text="Buscar".upper(),
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_buscar.place(x=685, y=157)

b_mostrar_todos = Button(
    frameMeio,
    command=lambda: mostrar(),
    width=12,
    text="Mostrar todos".upper(),
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_mostrar_todos.place(x=770, y=157)

b_exportar = Button(
    frameMeio,
    command=exportar_csv,
    width=20,
    text="Exportar CSV".upper(),
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
b_exportar.place(x=700, y=221)


# tabela---------------------------------------------------------
def mostrar(lista_personalizada=None):
    global tree

    # Evita empilhar várias tabelas e barras de rolagem ao atualizar a tela.
    for widget in frameBaixo.winfo_children():
        widget.destroy()

    tabela_head = [
        "#Item",
        "Nome",
        "Sala/Área",
        "Descrição",
        "Marca/Modelo",
        "Data da compra",
        "Valor da compra",
        "Número de série",
    ]

    try:
        lista_itens = lista_personalizada if lista_personalizada is not None else ver_form()
    except Exception as erro:
        lista_itens = []
        messagebox.showerror("Erro", f"Não foi possível carregar os dados.\nDetalhe: {erro}")

    tree = ttk.Treeview(frameBaixo, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    frameBaixo.grid_rowconfigure(0, weight=12)
    frameBaixo.grid_columnconfigure(0, weight=1)

    alinhamentos = ["center", "center", "center", "center", "center", "center", "center", "center"]
    larguras = [40, 150, 100, 160, 130, 100, 100, 100]

    for n, col in enumerate(tabela_head):
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=larguras[n], anchor=alinhamentos[n])

    for item in lista_itens:
        # item[8] é a imagem. Não exibimos na tabela, mas mantemos no Supabase.
        tree.insert("", "end", values=item[:8])

    valores = []
    for item in lista_itens:
        try:
            valores.append(float(item[6]))
        except (ValueError, TypeError):
            valores.append(0.0)

    total_valor = sum(valores)
    total_itens = len(valores)

    cotacao = obter_cotacao_dolar()

    if cotacao > 1.0:
        total_dolar = total_valor / cotacao
        l_total_valor["text"] = "Valor total de todos os itens\nR$ {:,.2f}\nUS$ {:,.2f}".format(total_valor, total_dolar)
    else:
        l_total_valor["text"] = "Valor total de todos os itens\nR$ {:,.2f}".format(total_valor)

    l_qtd_valor["text"] = f"Quantidade total de itens\n{total_itens}"


mostrar()
janela.mainloop()
