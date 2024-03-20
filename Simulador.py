def expressao_espaco(expressao):
    nova_expressao = ""
    for e in expressao:
        nova_expressao += e + " "
    return nova_expressao

def quantidade_letras(text):
    letras = set()
    for char in text:
        if char.isalpha():
            letras.add(char.lower())
    return len(letras), letras

def formacao_codigos(qntd):
    qntd_elevada = 2**qntd
    lista_codigos = []
    for i in range(qntd_elevada):
        codigo_binario = bin(i)[2:]
        codigo_binario = codigo_binario.zfill(qntd)
        lista_codigos.append(codigo_binario)
    return lista_codigos        

def formatacao_expressao0(expressao):
    expressao = expressao.replace("a", "True")
    expressao = expressao.replace("b", "False")
    expressao = expressao.replace("c", "True")
    print(expressao)
    return expressao

def formatacao_expressao(expressao):
    expressao = expressao.replace("~", "not")
    expressao = expressao.replace("+", "or")
    expressao = expressao.replace("*", "and")

    return expressao

def eval_expressao(expressao, expressao_codigos, letras):
    for codigos in expressao_codigos:
        for i,l in enumerate(letras):
            expressao.replace(codigos[i], l)
        print(expressao)
        print(eval(expressao))

expressao = "a*(b*c)+a*~b*~(~a*~c)"
expressao = expressao_espaco(expressao)

qntd_letras, letras = quantidade_letras(expressao)
expressao_codigos = formacao_codigos(qntd_letras)

expressao = formatacao_expressao0(expressao)
expressao = formatacao_expressao(expressao)
print(eval_expressao(expressao, expressao_codigos, letras))