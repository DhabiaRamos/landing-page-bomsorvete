import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


def recomendar(nome):

    conexao = sqlite3.connect("database.db")

    consulta = """
        SELECT
            p.nome,
            ip.categoria,
            ip.sabor,
            ip.quantidade
        FROM itens_pedido ip
        INNER JOIN pedidos p
            ON ip.pedido_id = p.id
    """

    df = pd.read_sql_query(
        consulta,
        conexao
    )

    conexao.close()

    df = df.dropna()

    print(df)
    print("Quantidade de registros:", len(df))

    if len(df) < 10:
        return "Milkshake Chocolate"

    encoder_cliente = LabelEncoder()
    encoder_categoria = LabelEncoder()
    encoder_sabor = LabelEncoder()

    df["cliente_cod"] = encoder_cliente.fit_transform(
        df["nome"]
    )

    df["categoria_cod"] = encoder_categoria.fit_transform(
        df["categoria"]
    )

    df["sabor_cod"] = encoder_sabor.fit_transform(
        df["sabor"]
    )

    X = df[[
        "cliente_cod",
        "quantidade"
    ]]

    y = (
        df["categoria"]
        + " "
        + df["sabor"]
    )

    modelo = DecisionTreeClassifier()

    modelo.fit(X, y)

    print("Modelo treinado!")
    print("Classes aprendidas:")
    print(modelo.classes_)

    if nome not in encoder_cliente.classes_:
        return "Milkshake Chocolate"

    cliente_cod = encoder_cliente.transform(
        [nome]
    )[0]

    quantidade_media = int(
        df[df["nome"] == nome]
        ["quantidade"]
        .mean()
    )

    entrada = pd.DataFrame(
    [[cliente_cod, quantidade_media]],
    columns=[
        "cliente_cod",
        "quantidade"
    ]
)

    previsao = modelo.predict(entrada)

    return previsao[0]