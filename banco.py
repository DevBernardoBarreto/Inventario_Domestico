#importei sqlite
import sqlite3 as lite
#fiz a conexao
con = lite.connect('dados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_compra DATE, valor_compra DECIMAL, serie TEXT, imagem TEXT)")