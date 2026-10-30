def texto_obligatorio(valor, campo):
    valor = str(valor).strip()
    if not valor:
        raise ValueError(f"El campo {campo} es obligatorio")
    return valor

def numero_positivo(valor, campo):
    numero = int(valor)
    if numero <= 0:
        raise ValueError(f"El campo {campo} debe ser mayor que cero")
    return numero
