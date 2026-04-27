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

    formContato.reset()
}