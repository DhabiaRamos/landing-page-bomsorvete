# 🍦 BomSorvete

## Sobre o Projeto

O BomSorvete é um sistema web desenvolvido para auxiliar uma sorveteria no gerenciamento de pedidos realizados pelos clientes.

A ideia do projeto surgiu como uma forma de aplicar, na prática, conhecimentos adquiridos durante meus estudos em Desenvolvimento Full Stack, envolvendo desenvolvimento web, banco de dados, responsividade, autenticação de usuários e conceitos introdutórios de Inteligência Artificial.
O sistema permite que clientes realizem pedidos online de maneira simples e que os administradores acompanhem todo o processo através de um painel administrativo.

Além disso, o projeto conta com um módulo capaz de interpretar automaticamente os pedidos digitados pelos clientes e gerar recomendações de produtos.

---

### 🌐 Acesse o projeto

https://bomsorvete.up.railway.app/

---

# Objetivos do Projeto

Durante o desenvolvimento deste sistema, os principais objetivos foram:

* Desenvolver uma aplicação web completa utilizando Python e Flask.
* Criar uma interface amigável e responsiva utilizando TailwindCSS.
* Trabalhar com persistência de dados utilizando SQLite.
* Implementar autenticação para área administrativa.
* Aplicar conceitos de organização de código em módulos.
* Praticar integração entre frontend e backend.
* Explorar conceitos básicos de Inteligência Artificial e Machine Learning.
* Realizar o deploy da aplicação em ambiente de produção.

---

# Funcionalidades

## Área do Cliente

### Página Inicial

A aplicação possui uma Landing Page responsiva contendo:

* Apresentação da sorveteria
* Informações sobre produtos
* Perguntas frequentes
* Formulário de contato
* Links para realização de pedidos

### Catálogo de Produtos

Os clientes podem visualizar os produtos disponíveis, incluindo:

* Sorvetes
* Picolés
* Milkshakes
* Açaís
* Sundaes

### Formulário de Contato

Permite que os usuários enviem dúvidas, sugestões ou solicitações diretamente para a empresa.

As informações ficam armazenadas no banco de dados para futuras consultas.

### Sistema de Pedidos

O cliente pode realizar pedidos diretamente pelo sistema.

Os dados enviados são processados pelo backend e armazenados no banco de dados para acompanhamento posterior.

### Integração com WhatsApp

Após a realização do pedido, o sistema gera automaticamente uma mensagem formatada para o WhatsApp, facilitando a comunicação com o cliente.

---

# Inteligência Artificial

Um dos diferenciais do projeto é a utilização de um módulo simples de Inteligência Artificial.

## Interpretador de Pedidos

O sistema consegue interpretar o texto digitado pelo cliente e identificar informações como:

* Categoria do produto
* Sabor
* Quantidade
* Volume

Esses dados são organizados automaticamente e armazenados em tabelas específicas do banco de dados.

## Sistema de Recomendação

Após o processamento do pedido, o sistema gera uma sugestão de produto para o cliente, simulando um mecanismo simples de recomendação.

O objetivo dessa funcionalidade foi aplicar conceitos iniciais relacionados à área de Machine Learning.

---

# Área Administrativa

O sistema possui uma área administrativa protegida por autenticação.

## Login Administrativo

O acesso ao painel é realizado através de senha armazenada em variável de ambiente.

Isso evita que informações sensíveis fiquem expostas no código-fonte.

## Dashboard de Pedidos

O administrador pode visualizar:

* Total de pedidos
* Pedidos pendentes
* Pedidos em produção
* Pedidos entregues

## Visualização Detalhada

Cada pedido possui uma tela própria contendo:

* Dados do cliente
* Telefone
* Pedido original
* Itens identificados pelo sistema

## Controle de Status

Os pedidos podem ser atualizados para diferentes etapas:

* Pendente
* Produção
* Pronto
* Entregue
* Cancelado

## Arquivamento

Após a entrega, o pedido pode ser arquivado.

Essa funcionalidade foi criada para evitar que o painel administrativo fique sobrecarregado com pedidos antigos.

---

# Tecnologias Utilizadas

## Backend

* Python
* Flask
* SQLite

## Frontend

* HTML5
* TailwindCSS
* JavaScript

## Ferramentas

* Git
* GitHub
* Railway
* VS Code

## Inteligência Artificial

* Processamento de texto
* Interpretação de pedidos
* Sistema simples de recomendação

---

# Estrutura do Projeto

```text
BomSorvete
│
├── app.py
├── criar_db.py
├── requirements.txt
│
├── machine_learning
│   ├── interpretador.py
│   └── recomendacao.py
│
├── templates
│   ├── index.html
│   ├── products.html
│   ├── admin.html
│   ├── login_admin.html
│   └── ver_pedido.html
│
├── static
│   ├── img
│   ├── script.js
│   └── output.css
│
└── .env
```

---

# Banco de Dados

O projeto utiliza SQLite como banco de dados.

Foram criadas as seguintes tabelas:

## contatos

Responsável por armazenar os dados enviados pelo formulário de contato.

Campos:

* id
* nome
* email
* telefone
* mensagem

## pedidos

Responsável por armazenar informações gerais dos pedidos.

Campos:

* id
* nome
* telefone
* pedido_original
* status
* arquivado

## itens_pedido

Responsável por armazenar os itens identificados pelo interpretador de pedidos.

Campos:

* id
* pedido_id
* categoria
* sabor
* quantidade
* volume

---

# Segurança

Durante o desenvolvimento foram aplicadas algumas medidas básicas de segurança:

* Uso de variáveis de ambiente
* Proteção da área administrativa
* Controle de sessão com Flask
* Arquivo .gitignore para evitar envio de dados sensíveis ao GitHub

Informações como:

* SECRET_KEY
* SENHA_ADMIN

não são armazenadas diretamente no código-fonte.

---

# Como Executar o Projeto

## Clonar o Repositório

```bash
git clone https://github.com/DhabiaRamos/landing-page-bomsorvete.git
```

## Acessar a Pasta

```bash
cd bomsorvete
```

## Criar Ambiente Virtual

```bash
python -m venv venv
```

## Ativar Ambiente Virtual

Windows:

```bash
venv\Scripts\activate
```

## Instalar Dependências

```bash
pip install -r requirements.txt
```

## Criar Arquivo .env

```env
SECRET_KEY=sua_chave_secreta
SENHA_ADMIN=sua_senha
```

## Criar Banco de Dados

```bash
python criar_db.py
```

## Executar Aplicação

```bash
python app.py
```

---

# Aprendizados

Durante o desenvolvimento deste projeto tive a oportunidade de praticar diversos conceitos importantes, como:

* Estruturação de aplicações Flask
* Criação de rotas e templates
* Manipulação de banco de dados SQLite
* Integração entre frontend e backend
* Responsividade utilizando TailwindCSS
* Controle de autenticação com sessões
* Organização de código em módulos
* Deploy utilizando Railway
* Utilização de conceitos básicos de Inteligência Artificial

Esse projeto representou uma etapa importante na consolidação dos conhecimentos adquiridos durante minha formação em Desenvolvimento Full Stack.

---

# Desenvolvedora

**Dhabia Ramos**

Projeto desenvolvido como parte dos estudos do curso de Desenvolvedor Full Stack do Senac, com o objetivo de aplicar conhecimentos de desenvolvimento web, banco de dados, experiência do usuário e integração de recursos de Inteligência Artificial.
