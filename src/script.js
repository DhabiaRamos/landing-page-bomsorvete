// Parte do formulario de contato

const formContato = document.querySelector("#formularioContato")
formContato.addEventListener('submit', enviarFormContato)

function enviarFormContato(e) {
    e.preventDefault()

    const usuarioContato = [
        nome.value,
        email.value,
        tel.value,
        info.value
    ]

    console.log(usuarioContato)
    formContato.reset()
}


// Parte do formulario de pedido 

const formPedido = document.querySelector("#formularioPedido")

formPedido.addEventListener('submit', enviarFormPedido)

function enviarFormPedido(e){
    e.preventDefault()

    const usuarioPedido = [
        nome.value,
        tel.value,
        formPedido.value
    ]

    console.log(usuarioPedido)
    formPedido.reset()
}


// Parte das perguntas frequentes

function aparecerResposta(){
    const caixaResposta = document.querySelector("#faq p")

    caixaResposta.style.display = "block"
}