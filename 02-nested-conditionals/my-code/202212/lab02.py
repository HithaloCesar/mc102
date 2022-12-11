def meme_video() -> None:
	seconds = int(input(
		"Quantos segundos são necessários para saber se um vídeo é bom?\n"
	))
	print(seconds)
	if seconds < 0:
		print("Erro: entrada inválida")
		exit()
	print("RESULTADO")
	if seconds <= 5:
		print("Você deveria estar no TikTok")
	else:
		print("Sua página de memes é: @meltmemes")


def capybaras() -> None:
	capybaras = input("São as capivaras os melhores animais da Terra?\n")
	print(capybaras)
	if capybaras == "Sim":
		print("RESULTADO")
		print("Sua página de memes é: @genteboamemes")
	elif capybaras == "Não":
		print("RESULTADO")
		print("Sua página de memes é: @wrongchoicememes")
	else:
		print("Erro: entrada inválida")


def best_band() -> None:
	band = input("Qual banda você gosta mais?\n")
	match band:
		case "A":
			print("A) Matanza")
		case "B":
			print("B) Iron Maiden")
		case "C":
			print("C) Imagine Dragons")
		case "D":
			print("D) BlackPink")
		case _:
			print(band)
			print("Erro: entrada inválida")
			exit()
	if band == "A" or band == "B":
		print("RESULTADO")
		print("Sua página de memes é: @badrockistamemes")
	elif band == "C" or band == "D":
		capybaras()


def family_group() -> None:
	good_morning = input(
		"Que imagem de bom dia você manda no grupo da família?\n"
	)
	match good_morning:
		case "A":
			print("A) Bebê em roupa de flor")
			print("RESULTADO")
			print("Sua página de memes é: @bomdiabebe")
		case "B":
			print("B) Gato")
			print("RESULTADO")
			print("Sua página de memes é: @kittykatmsgs")
		case "C":
			print("C) Coração e rosas")
			print("RESULTADO")
			print("Sua página de memes é: @bomdiaflordodia")
		case _:
			print(good_morning)
			print("Erro: entrada inválida")


def main() -> None:
	print("*Que página de meme do Instagram você é?*")
	print("Qual a sua idade?")
	age = int(input())
	print(age)
	if age < 0 or age > 125:
		print("Erro: entrada inválida")
		exit()
	if age < 25:
		meme_video()
	elif age < 41:
		best_band()
	else:
		family_group()


if __name__ == "__main__":
	main()
