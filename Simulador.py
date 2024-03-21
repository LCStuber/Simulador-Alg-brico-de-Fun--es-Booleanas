import sys

def validador():
    caracteresVálidos = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z","A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z", "~", "+", "*",]
    exp = str(input())
    for letra in exp:
        if letra not in caracteresVálidos:
            sys.tracebacklimit=0
            raise TypeError(f'''ERRO! A expressão algébrica digitada está incorreta, pois contém o caractere não válido "{letra}"!
Os caracteres válidos para o uso do programa são:
- Qualquer letra maiúscula e/ou minúscula dentro do alfabeto americano;
- "~" usado antes de uma letra (como "~A") para indicar negação ("não A");
- "+" usado para a operação "ou";
- "*" usado para a operação "e".''')

    return exp


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

def montagem_expressoes(expressao, lista_codigos, letras):
    lista_expressoes = []
    for codigos in lista_codigos:
        expressao_temp = expressao  
        for i,l in enumerate(letras):
            expressao_temp = expressao_temp.replace(l, str(codigos[i]))
        expressao_temp = expressao_temp.replace("0", "False")
        expressao_temp = expressao_temp.replace("1", "True")
        lista_expressoes.append(expressao_temp)
    return lista_expressoes


def formatacao_expressao(lista_expressoes):
    i = 0
    while i < len(lista_expressoes):
        lista_expressoes[i] = lista_expressoes[i].replace("~", "not")
        lista_expressoes[i] = lista_expressoes[i].replace("+", "or")
        lista_expressoes[i] = lista_expressoes[i].replace("*", "and")

        i += 1

    return lista_expressoes

def montagem_tabela(lista_expressoes):
    for i, expressao in enumerate(lista_expressoes):
        print("Expressão:", i+1)
        print(expressao)
        print(eval(expressao))
        print("\n")


if __name__ == "__main__":
    print("-"*30)
    print("Simulador de Expressões Lógicas")
    print("-"*30)
    print("Digite a expressão lógica:")

    expressao = validador()

    expressao = expressao_espaco(expressao)

    qntd_letras, letras = quantidade_letras(expressao)
    lista_codigos = formacao_codigos(qntd_letras)

    lista_expressoes = montagem_expressoes(expressao, lista_codigos, letras)
    lista_expressoes = formatacao_expressao(lista_expressoes)

    montagem_tabela(lista_expressoes)
