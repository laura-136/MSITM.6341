import random

class Hangman:
    #initialize and set max attempt
    def __init__(self, word_list, max_attempts=7):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.word_to_guess = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.correct_letters = set()
        self.attempts_left = max_attempts

    #display hidden words
    def display_word(self):
        return ' '.join(letter if letter in self.correct_letters else '_' for letter in self.word_to_guess)
    
    def has_won(self):
        return set(self.word_to_guess) == self.correct_letters #define winning condition
    
    #checking the guess and display message
    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters: #check if lettter was guessed before
            return "You've already guessed that letter."
        
        self.guessed_letters.add(letter)
        
        if letter in self.word_to_guess: #'correct guess
            self.correct_letters.add(letter)
            if self.has_won():
                return f"Congratulations! Word is correct: {self.word_to_guess}" 
            return "Correct guess!"
        else:
            self.attempts_left -= 1 #wrong guess deduct attempt
            if self.attempts_left == 0: #out of attempt end game
                return f"Game over! The correct word is: {self.word_to_guess}"
            return "Wrong guess. Try again."

    def is_game_over(self):
        return self.attempts_left == 0 or self.has_won() #define game is over when attempt left ==0 or won

    #define word list and display game prompt 
    def play_hangman():
        words = ["database", "polymorphism", "integer", "algorithm", "programming",'information', 'python']
        game = Hangman(words)
        
        while True: #start game
            game = Hangman(words)
            print("Welcome to Hangman!")
            while not game.is_game_over():
                print("\n" + game.display_word())
                print(f"Remaining Attempt: {game.attempts_left}") #display attempt left
                user_guess = input("Guess a letter: ").strip()
                if len(user_guess) != 1 or not user_guess.isalpha(): #check for valid input as a single letter from a-z
                    print("Please enter a single letter.")
                    continue
                print(game.guess_letter(user_guess))
        
            play_again = input("Do you want to play again? (y/n): ").strip().lower() #repeat game prompt
            if play_again != 'y':
                print ('Game ended!') 
                break
         
            
