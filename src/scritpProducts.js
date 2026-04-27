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
    
    formPedido.reset()
}