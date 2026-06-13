from supabase_db import supabase


def _extrair_id(valor):
    """Aceita id puro ou lista/tupla com id, sem quebrar chamadas antigas."""
    if isinstance(valor, (list, tuple)):
        return valor[0]
    return valor


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
        "imagem": i[7],
    }

    return supabase.table("inventario").insert(dados).execute()


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
        "imagem": i[7],
    }

    id_item = _extrair_id(i[8])

    return (
        supabase.table("inventario")
        .update(dados)
        .eq("id", id_item)
        .execute()
    )


# DELETAR DADOS
def deletar_form(i):
    id_item = _extrair_id(i)

    return (
        supabase.table("inventario")
        .delete()
        .eq("id", id_item)
        .execute()
    )


# VER DADOS
def ver_form():
    resposta = (
        supabase.table("inventario")
        .select("*")
        .order("id", desc=False)
        .execute()
    )

    lista = []

    for item in resposta.data:
        lista.append((
            item.get("id", ""),
            item.get("nome", ""),
            item.get("local", ""),
            item.get("descricao", ""),
            item.get("marca", ""),
            item.get("data_compra", ""),
            item.get("valor_compra", ""),
            item.get("serie", ""),
            item.get("imagem", ""),
        ))

    return lista


# VER DADOS INDIVIDUAIS
def ver_item(id):
    id_item = _extrair_id(id)

    resposta = (
        supabase.table("inventario")
        .select("*")
        .eq("id", id_item)
        .execute()
    )

    return resposta.data
