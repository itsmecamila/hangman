import random

MUSICS = {
	'pop': [
        "Shape of You",
        "Sorry",
        "Sugar",
        "Uptown Funk",
        "Cant Stop the Feeling",
        "Roar",
        "Counting Stars",
        "I Want It That Way",
        "Good as Hell",
        "New Rules"
    ],
	'rock': [
        'The Death of Love',
        'Paint It Black',
        'Painkiller',
        'Master of Puppets',
        'Quero Ver o Oco',
        'Bate o Sino Metalino'
    ],
	'alternativa':[
        "Paranoid Android",
        "Bohemian Rhapsody",
        "Stairway to Heaven",
        "Sweet Child O Mine",
        "Hotel California",    
        "Lithium",    
        "Black Hole Sun",    
        "Come as You Are",    
        "Today",    
        "Jeremy"
    ]
}

musicName = None
lives = 6
guessedLetters = []

def resetGame():
    global musicName, lives, guessedLetters

    musicName = None
    lives = 6
    guessedLetters = []

def playerHasWon():
    for letter in musicName:
        if letter not in guessedLetters:
            return False
    
    return True

def displayCurrentWordState():
    for letter in musicName:
        if letter == " ":
            print(' ')
            continue

        if letter.lower() in guessedLetters:
            print(letter, end=' ')
        else:
            print("_", end=' ')    
    
def playGame():
    global lives

    while lives > 0 and not playerHasWon():
        print(f'Lives: {lives}\n')
        displayCurrentWordState()
        
        guessLetter = input("\nDigite uma letra: ")   
        guessedLetters.append(guessLetter.lower())

        if guessLetter not in musicName:
            lives -= 1 
    
    if lives == 0:
        print("Game over!")            
    else:
        print("You win")
    
    input('Precione ENTER para continuar')

def chooseMusicByGender(gender: str):
    allMusicNamesOfGender = MUSICS[gender]

    randomIndex = random.randint(0, len(allMusicNamesOfGender) - 1)
    return allMusicNamesOfGender[randomIndex]

def menu():
    global musicName

    print("Jogo da Forca de Música")
    print("-----------------------")
    print("Escolha um gênero musical:")
    print("[1] Pop")
    print("[2] Rock")
    print("[3] Alternativa")
    
    op = 0
    while op < 1 or op > 3:
        op = int(input("> "))

    if op == 1:
        musicName = chooseMusicByGender('pop')

    elif op == 2:
        musicName = chooseMusicByGender('rock')
        
    elif op == 3:
        musicName = chooseMusicByGender('alternativa')
    
    input('Precione ENTER para continuar')

def main():
    while True:
        menu()
        playGame()

main()
