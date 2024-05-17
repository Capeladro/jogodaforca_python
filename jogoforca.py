import random

def choose_word():
    palavras = ["pedro", "batata", "celular", "forca", "backend", "marcelo", "desenvolvimento", "sistemas"]
    return random.choice(palavras)

def display_word(palavra, letras_encontradas):
    display = ""
    for letra in palavra:
        if letra in letras_encontradas:
            display += letra
        else:
            display += "_"
    return display

def play_game():

    palavra = choose_word()
    letras_encontradas = []
    tentativas = 6
    
    print("Jogo da forca")
    print(display_word(palavra, letras_encontradas))
    
    while True:
        guess = input("Chute uma letra: ").lower()
        
        if guess in letras_encontradas:
            print("Essa letra já foi usada. Tente outra.")
        else:
            letras_encontradas.append(guess)
            if guess not in palavra:
                tentativas -= 1
                print("Letra não encontrada. Você tem {} tentativas restantes.".format(tentativas))
                if tentativas == 0:
                    print("Você perdeu! A palavra era '{}'.".format(palavra))
                    break
            else:
                print("Letra encontrada!")
                
        display = display_word(palavra, letras_encontradas)
        print(display)
        
        if "_" not in display:
            print("Você acertou a palavra")
            break

play_game()