from supabase_db import supabase


# CRUD


# INSERIR DADOS
# INSERIR DADOS
def inserir_form(i):

    dados = {
        "nome": i[0],
        "local": i[1],
        "descricao": i[2],
        "marca": i[3],
        "data_compra": i[4],
        "valor_compra": i[5],
        "serie": i[6],
        "imagem": i[7]
    }

    resposta = supabase.table("inventario").insert(dados).execute()

    print("RESPOSTA SUPABASE:")
    print(resposta.data)



# ATUALIZAR DADOS
def atualizar_(i):

    dados = {
        "nome": i[0],
        "local": i[1],
        "descricao": i[2],
        "marca": i[3],
        "data_compra": i[4],
        "valor_compra": i[5],
        "serie": i[6],
        "imagem": i[7]
    }


    supabase.table("inventario")\
        .update(dados)\
        .eq("id", i[8])\
        .execute()



# DELETAR DADOS
def deletar_form(i):

    supabase.table("inventario")\
        .delete()\
        .eq("id", i)\
        .execute()



# VER DADOS
def ver_form():

    resposta = supabase.table("inventario")\
        .select("*")\
        .execute()

    lista = []

    for item in resposta.data:
        lista.append((
            item["id"],
            item["nome"],
            item["local"],
            item["descricao"],
            item["marca"],
            item["data_compra"],
            item["valor_compra"],
            item["serie"],
            item["imagem"]
        ))

    return lista



# VER DADOS INDIVIDUAIS
def ver_item(id):

    resposta = supabase.table("inventario")\
        .select("*")\
        .eq("id", id)\
        .execute()

    return resposta.data