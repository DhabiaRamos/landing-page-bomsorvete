const formContato = document.querySelector("#formularioContato")

formContato.addEventListener("submit", enviarContato)

async function enviarContato(e){

    e.preventDefault()

    const dados = {
        nome: document.querySelector("#nome").value,
        email: document.querySelector("#email").value,
        telefone: document.querySelector("#tel").value,
        mensagem: document.querySelector("#info").value
    }

    try {

        const resposta = await fetch("/contato", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        })

        const resultado = await resposta.json()

        alert(resultado.mensagem)

        formContato.reset()

    } catch (erro) {

        console.log(erro)

        alert("Erro ao enviar contato")

    }
}