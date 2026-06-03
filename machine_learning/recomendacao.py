import sqlite3
from collections import Counter

def recomendar(nome):

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            ip.categoria,
            ip.sabor,
            ip.quantidade
        FROM itens_pedido ip
        INNER JOIN pedidos p
            ON ip.pedido_id = p.id
        WHERE p.nome = ?
    """, (nome,))

    pedidos = cursor.fetchall()

    conexao.close()

    # Cliente novo
    if not pedidos:
        return "Milkshake Chocolate 300ml"

    categorias = []
    sabores = []
    quantidades = []

    # Organiza dados
    for pedido in pedidos:

        categoria = pedido[0]
        sabor = pedido[1]
        quantidade = pedido[2]

        if categoria:
            categorias.append(categoria)

        if sabor:
            sabores.append(sabor)

        if quantidade:
            quantidades.append(quantidade)

    # Favoritos
    categoria_favorita = Counter(categorias).most_common(1)[0][0] if categorias else ""

    sabor_favorito = Counter(sabores).most_common(1)[0][0] if sabores else ""

    quantidade_favorita = Counter(quantidades).most_common(1)[0][0] if quantidades else ""

    # Monta recomendação
    recomendacao = f"{categoria_favorita} {sabor_favorito} {quantidade_favorita}"

    return recomendacao.strip()
