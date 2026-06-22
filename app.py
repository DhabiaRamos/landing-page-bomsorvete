import sqlite3
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from dotenv import load_dotenv
from machine_learning.recomendacao_ml import recomendar
from machine_learning.interpretador import interpretar_pedido

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

SENHA_ADMIN = os.getenv(
    "SENHA_ADMIN"
)

@app.route("/teste")
def teste():
    resultado = recomendar("João")
    return str(resultado)

# Função para criar o banco no railway

def criar_tabelas():

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        pedido_original TEXT NOT NULL,
        status TEXT DEFAULT 'Pendente',
        arquivado INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens_pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pedido_id INTEGER NOT NULL,
        categoria TEXT,
        sabor TEXT,
        quantidade INTEGER,
        volume INTEGER,
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        mensagem TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")


# Página de produtos
@app.route("/produtos")
def produtos():
    return render_template("products.html")


# =========================
# CONTATO
# =========================

@app.route("/contato", methods=["POST"])
def contato():

    try:

        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({
                "mensagem": "Erro ao receber os dados"
            }), 400

        nome = dados["nome"]
        email = dados["email"]
        telefone = dados["telefone"]
        mensagem = dados["mensagem"]

        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                mensagem TEXT NOT NULL
            )
        """)

        cursor.execute("""
            INSERT INTO contatos
            (nome, email, telefone, mensagem)
            VALUES (?, ?, ?, ?)
        """, (nome, email, telefone, mensagem))

        conexao.commit()
        conexao.close()

        return jsonify({
            "mensagem": "Contato enviado com sucesso!"
        })

    except Exception as erro:

        print("ERRO CONTATO:", erro)

        return jsonify({
            "mensagem": "Erro ao salvar contato"
        }), 500


# =========================
# PEDIDO
# =========================

@app.route("/pedido", methods=["POST"])
def pedido():

    try:

        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({
                "mensagem": "JSON inválido"
            }), 400

        nome = dados["nome"]
        telefone = dados["telefone"]
        pedido_cliente = dados["pedido"]

        itens = interpretar_pedido(pedido_cliente)

        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO pedidos
            (nome, telefone, pedido_original)
            VALUES (?, ?, ?)
        """, (
            nome,
            telefone,
            pedido_cliente
        ))

        pedido_id = cursor.lastrowid

        for item in itens:

            cursor.execute("""
                INSERT INTO itens_pedido
                (
                    pedido_id,
                    categoria,
                    sabor,
                    quantidade,
                    volume
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                pedido_id,
                item.get("categoria"),
                item.get("sabor"),
                item.get("quantidade"),
                item.get("volume")
            ))

        conexao.commit()
        conexao.close()

# =========================
# MACHINE LEARNING
# =========================

        produto_recomendado = recomendar(nome)

        descricao_itens = ""

        for item in itens:

            descricao_itens += (
                f"• {item['quantidade']} "
                f"{item['categoria']} "
                f"{item['sabor']}\n"
            )
        

        # =========================
        # MENSAGEM WHATSAPP
        # =========================


        mensagem_whatsapp = f"""
        Olá {nome} 🍦

        Seu pedido foi recebido com sucesso!

        🧾 Pedido identificado:

        {descricao_itens}

        ⭐ Recomendação da IA:
        {produto_recomendado}

        BomSorvete 😄
        """

        # Remove espaços e quebra linha
        mensagem_formatada = mensagem_whatsapp.replace("\n", "%0A")

        # Remove caracteres do telefone
        telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        # Link do WhatsApp
        link_whatsapp = f"https://wa.me/55{telefone}?text={mensagem_formatada}"

        return jsonify({
            "mensagem": "Pedido enviado com sucesso!",
            "whatsapp": link_whatsapp,
            "recomendacao": produto_recomendado
        })

    except Exception as erro:

        import traceback
        traceback.print_exc()

        print("ERRO PEDIDO:", erro)

        return jsonify({
            "mensagem": "Erro ao salvar pedido"
        }), 500

# =========================
# LOGIN ADMIN
# =========================

@app.route("/login-admin", methods=["GET", "POST"])
def login_admin():

    if request.method == "POST":

        senha = request.form["senha"]

        if senha == SENHA_ADMIN:

            session["admin"] = True

            return redirect("/admin")

        return render_template(
            "login_admin.html",
            erro=True
        )

    return render_template(
        "login_admin.html"
    )

def admin_logado():

    return session.get("admin")

# SAIR DO ADMIN

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

# =========================
# ADMIN
# =========================

@app.route("/admin")
def admin():

    if not admin_logado():

        return redirect(
            "/login-admin"
        )

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            telefone,
            pedido_original,
            status
        FROM pedidos
        WHERE arquivado = 0
        ORDER BY id DESC
    """)

    pedidos = cursor.fetchall()

    total_pedidos = len(pedidos)

    pendentes = len(
        [p for p in pedidos if p[4] == "Pendente"]
    )

    producao = len(
        [p for p in pedidos if p[4] == "Produção"]
    )

    entregues = len(
        [p for p in pedidos if p[4] == "Entregue"]
    )

    conexao.close()

    return render_template(
        "admin.html",
        pedidos=pedidos,
        total_pedidos=total_pedidos,
        pendentes=pendentes,
        producao=producao,
        entregues=entregues
    )

# VER PEDIDO - ADMIN

@app.route("/pedido/<int:pedido_id>")
def ver_pedido(pedido_id):

    if not admin_logado():

        return redirect(
            "/login-admin"
        )

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            telefone,
            pedido_original,
            status
        FROM pedidos
        WHERE id = ?
    """, (pedido_id,))

    pedido = cursor.fetchone()

    cursor.execute("""
        SELECT
            categoria,
            sabor,
            quantidade,
            volume
        FROM itens_pedido
        WHERE pedido_id = ?
    """, (pedido_id,))

    itens = cursor.fetchall()

    conexao.close()

    return render_template(
        "ver_pedido.html",
        pedido=pedido,
        itens=itens
    )


# ALTERAR STATUS DO PEDIDO - ADMIN 

@app.route(
    "/alterar-status/<int:pedido_id>",
    methods=["POST"]
)
def alterar_status(pedido_id):

    if not admin_logado():

        return redirect(
            "/login-admin"
        )

    novo_status = request.form["status"]

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pedidos
        SET status = ?
        WHERE id = ?
    """, (
        novo_status,
        pedido_id
    ))

    conexao.commit()
    conexao.close()

    return redirect(
        f"/pedido/{pedido_id}"
    )


# ARQUIVAR PEDIDO - ADMIN 

@app.route("/arquivar/<int:pedido_id>")
def arquivar_pedido(pedido_id):

    if not admin_logado():

        return redirect(
            "/login-admin"
        )

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT status
        FROM pedidos
        WHERE id = ?
    """, (pedido_id,))

    resultado = cursor.fetchone()

    if not resultado:

        flash(
            "Pedido não encontrado.",
            "erro"
        )

        conexao.close()

        return redirect("/admin")

    status = resultado[0]

    if status != "Entregue":

        flash(
            "Só é possível arquivar pedidos entregues.",
            "erro"
        )

        conexao.close()

        return redirect("/admin")

    cursor.execute("""
        UPDATE pedidos
        SET arquivado = 1
        WHERE id = ?
    """, (pedido_id,))

    conexao.commit()
    conexao.close()

    flash(
        "Pedido arquivado com sucesso.",
        "sucesso"
    )

    return redirect("/admin")


# =========================
# INICIAR SERVIDOR
# =========================

criar_tabelas()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )