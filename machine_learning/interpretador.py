import re
from rapidfuzz import process

def corrigir_palavra(palavra, lista):

    resultado = process.extractOne(
        palavra,
        lista
    )

    if resultado:

        palavra_corrigida = resultado[0]
        similaridade = resultado[1]

        if similaridade >= 80:
            return palavra_corrigida

    return None

def normalizar_texto(texto):

    texto = texto.lower()

    texto = texto.replace(
        "litros",
        "l"
    )

    numeros = {
        "um": "1",
        "uma": "1",
        "dois": "2",
        "duas": "2",
        "três": "3",
        "tres": "3",
        "quatro": "4",
        "cinco": "5",
        "seis": "6",
        "sete": "7",
        "oito": "8",
        "nove": "9",
        "dez": "10"
    }

    palavras = texto.split()

    resultado = []

    for palavra in palavras:
        resultado.append(
            numeros.get(palavra, palavra)
        )

    return " ".join(resultado)

def interpretar_pedido(texto):

    texto = normalizar_texto(texto.lower())

    partes = re.split(r"\s+e\s+|\n", texto)

    itens = []

    categorias = [
        "sorvete",
        "milkshake",
        "acai",
        "açaí",
        "açai",
        "acai",
        "sundae"
    ]

    sabores = [
        "chocolate",
        "morango",
        "baunilha",
        "uva",
        "ovomaltine"
    ]

    for parte in partes:

        categoria = None
        sabor = None
        quantidade = 1

        palavras = parte.split()

        for palavra in palavras:

            encontrada = corrigir_palavra(
                palavra,
                categorias
            )

            if encontrada:
                categoria = encontrada
                break

        for palavra in palavras:

            encontrado = corrigir_palavra(
                palavra,
                sabores
            )

            if encontrado:
                sabor = encontrado
                break
        
        quantidade = 1
        volume = None

        numero_match = re.search(
            r"^(\d+)",
            parte
        )

        if numero_match:
            quantidade = int(
                numero_match.group(1)
            )

        volume_match = re.search(
            r"(\d+)\s*(ml|l)",
            parte
        )

        if volume_match:

            volume = int(
                volume_match.group(1)
            )

        itens.append({

            "categoria": categoria,
            "sabor": sabor,
            "quantidade": quantidade,
            "volume": volume

        })

    return itens