import sqlite3 as lite

con = lite.connect('dados.db')

#CRUD


#INSERIR DADOS
def inserir_form(i):

    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra, valor_compra, serie, imagem)VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i) 


#ATUALIZAR DADOS
def atualizar_(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i) 




#DELETAR DADOS
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)


#VER DADOS
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#VER DADOS INDIVIDUAIS
def ver_item(id):
    ver_dados_individuais = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)
    return ver_dados_individuais