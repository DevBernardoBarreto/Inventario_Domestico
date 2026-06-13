# Arquivo mantido para compatibilidade com a versão antiga SQLite.
# A versão atual do projeto usa Supabase em view.py.
import sqlite3 as lite

con = lite.connect("dados.db")

with con:
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            local TEXT,
            descricao TEXT,
            marca TEXT,
            data_compra DATE,
            valor_compra DECIMAL,
            serie TEXT,
            imagem TEXT
        )
        """
    )
