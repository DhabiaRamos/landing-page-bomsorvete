const formPedido = document.querySelector("#formularioPedido")

formPedido.addEventListener("submit", enviarFormPedido)

async function enviarFormPedido(e){

    e.preventDefault()

    const dados = {
        nome: document.querySelector("#nome").value,
        telefone: document.querySelector("#tel").value,
        pedido: document.querySelector("#pedido").value
    }

    const resposta = await fetch("/pedido", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })


    const resultado = await resposta.json()

    alert(resultado.mensagem)

    // Abre WhatsApp automaticamente
    if(resultado.whatsapp){

        window.open(resultado.whatsapp, "_blank")

    }

    formPedido.reset()
}