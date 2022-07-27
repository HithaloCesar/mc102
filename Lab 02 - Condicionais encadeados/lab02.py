# Pede a idade do usuário, que deve ser um número inteiro.
idade = int(input())
 
# Realiza a parte do teste destinada a usuários de menos de 25 anos.
if idade < 25:
    segundos = input()
    print("*Que página de meme do Instagram você é?*")
    print("Qual a sua idade?")
    print(idade)
    if idade < 0:
        print("Erro: entrada inválida")
    else:
        print("Quantos segundos são necessários para saber se um vídeo é bom?")
        print(segundos)
        segundos = int(segundos)
        if segundos < 0:
            print("Erro: entrada inválida")
        elif segundos <= 5:
            print("RESULTADO")
            print("Você deveria estar no TikTok")
        else:
            print("RESULTADO")
            print("Sua página de memes é: @meltmemes")
 
# Realiza a parte do teste destinada a usuários de 25 a 40 anos.
elif idade <= 40:
    banda = input()
    if banda == "C" or banda == "D":
        capivaras = input()
    print("*Que página de meme do Instagram você é?*")
    print("Qual a sua idade?")
    print(idade)
    print("Qual banda você gosta mais?")
    if banda == "A":
        print("A) Matanza")
    elif banda == "B":
        print("B) Iron Maiden")
    elif banda == "C":
        print("C) Imagine Dragons")
    elif banda == "D":
        print("D) BlackPink")
    else:
        print(banda)
        print("Erro: entrada inválida")
    if banda == "A" or banda == "B":
        print("RESULTADO")
        print("Sua página de memes é: @badrockistamemes")
    elif banda == "C" or banda == "D":
        print("São as capivaras os melhores animais da Terra?")
        print(capivaras)
        if capivaras == "Sim":
            print("RESULTADO")
            print("Sua página de memes é: @genteboamemes")
        elif capivaras == "Não":
            print("RESULTADO")
            print("Sua página de memes é: @wrongchoicememes")
        else:
            print("Erro: entrada inválida")
 
# Realiza a parte do teste destinada a usuários de 41 a 125 anos.
else:
    bom_dia = input()
    print("*Que página de meme do Instagram você é?*")
    print("Qual a sua idade?")
    print(idade)
    if idade > 125:
        print("Erro: entrada inválida")
    else:
        print("Que imagem de bom dia você manda no grupo da família?")
        if bom_dia == "A":
            print("A) Bebê em roupa de flor")
            print("RESULTADO")
            print("Sua página de memes é: @bomdiabebe")
        elif bom_dia == "B":
            print("B) Gato")
            print("RESULTADO")
            print("Sua página de memes é: @kittykatmsgs")
        elif bom_dia == "C":
            print("C) Coração e rosas")
            print("RESULTADO")
            print("Sua página de memes é: @bomdiaflordodia")
        else:
            print(bom_dia)
            print("Erro: entrada inválida")