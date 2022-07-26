import random
from tokenize import String

# TODO:
# - πόσα γράμματα στο σακουλάκι(ΟΚ)
# - Jupyter
# - το σακουλάκι να αρχικοποιείται με την αρχή ενός νέου παιχνιδιού (μάλλον ΟΚ)
# - όνομα για τον παίκτη-άνθρωπο
# - περιορισμός στο amount των letters (πρέπει amount >= 0 για κάθε γράμμα),
#   γιατί όταν τελειώνουν τα γράμματα το παιχνίδι συνεχίζει με
#   αρνητικό αριθμό γραμμάτων!
# - στην αρχή για κάποιο λόγο βγάζει 28 γραμματα αντί για 14

# Θεωρούμε ότι όταν ο παίκτης παίζει λέξη από τα 
# διαθέσιμα γράμματα αλλά είναι μη αποδεκτή τότε 
# χάνει την σειρά του χωρίς να ανανεωθούν τα γράμματά του
# (δεν του αφαιρούνται τα γράμματα που έπαιξε με την λέξη αυτή)

class SakClass:
    def __init__(self, letters_weight:dict, letters_amount:dict):
        '''Initializes the sak.'''
        self.letters_weight = letters_weight
        self.letters_amount = letters_amount

        # Here we create an attrbute that is a copy of letters_amount dictionary,
        # so that we can store all the letters in letters_amount and 
        # change only the copy. In this way, we can "refill" the sak 
        # again when a new game starts.
        self.letters_amount_copy = {}
        for letter in self.letters_amount:
            self.letters_amount_copy.update({letter: self.letters_amount.get(letter)})

    def randomize_sak(self):
        '''Randomizes the sak, like shuffling the letters.'''

        letter_list = []
        for letter in self.letters_amount_copy:
            pair = [letter, self.letters_amount_copy.get(letter, "Exception: the letter does not exist in the dict")]
            letter_list.append(pair)

        # shuffle the letter list 
        random.shuffle(letter_list)

        # empty the dict, and put there the new order of letters
        self.letters_amount_copy = {}
        for pair in letter_list:
            self.letters_amount_copy[pair[0]] = pair[1]

    def getletters(self, N: int):
        '''Returns letters by removing them from the sak, 
        so that the player has always 7 letters.
        Returns None if there are no letters in the sak.'''

        letters_to_return = []
        for i in range(N):
            # αν δεν υπάρχει άλλο γράμμα στο σακουλάκι
            if (self.pop_letter(self.letters_amount_copy)) is None:
                return None
            else:
                # αλλιώς (αν υπάρχει) βγάλε το γράμμα από το σακουλάκι
                letters_to_return.append(self.pop_letter(self.letters_amount_copy))
        self.randomize_sak()
        return letters_to_return

    def putbackletters(self, letters:list):
        '''Puts the letters back to the sak.'''

        # for each letter in the given list,
        # find it in the dict letters_amount_copy and increment its amount
        for let in letters:
            self.letters_amount_copy[let] += 1
        
        return

    def pop_letter(self, letters_amount_copy: dict):
        ''' Takes a letter from the sak.
        Returns None if there are no letters in the sak.'''


        # while amount of letter = 0 (i.e. letter does not exist)
        # and we are within the boundaries of the dict,
        # go to "next" letter of sack

        # TODO: bug: index out of bound (probably fixed)
        i = 0
        while letters_amount_copy[list(letters_amount_copy.keys())[i]] <= 0 and i < len(letters_amount_copy) - 1:
            # print(len(letters_amount_copy))
            i += 1

        if letters_amount_copy[list(letters_amount_copy.keys())[i]] > 0 and i < len(letters_amount_copy):
            # found a letter
            letter = list(letters_amount_copy.keys())[i]  # takes a letter # we put list() so that we can have access
            letters_amount_copy[list(letters_amount_copy.keys())[i]] -= 1  # and reduces its frequency
            # here we print the amount of available remaining letters
            #print(letters_amount_copy[list(letters_amount_copy.keys())[i]])
            return letter
        else:
            print('There are no letters in the sak.')
            return None

class Player():
    def __init__(self):
        self.score = 0

    def __repr__(self):
        pass


class Human(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        pass

    def play(self):
        print('Human is playing')


class Computer(Player):
    def __init__(self):
        pass

    def __repr__(self):
        pass
    
    def play(self):
        print('Computer is playing')


class Game:
    '''
    Represents the game.
    '''

    def __init__(self, sak: SakClass, player1:Player, player2:Player):
        '''Initializes the sak.
         sak is a SakClass object.
         player1 and player2 are Player objects.
        '''
        self.sak = sak
        self.current_player = None
        self.player1 = player1    # for extendability, we do not write human and computer
        self.player2 = player2

    def __repr__(self):
        pass

    def setup(self):
        print("***** SCRABBLE *****")
        while True:
            print('--------------------')
            print('1: Σκορ')
            print('2: Ρυθμίσεις')
            print('3: Παιχνίδι')
            print('q: Έξοδος')
            print('--------------------')
            ans = input('Επίλεξε από το μενού: ')

            if ans == '1':
                # show score
                print('ΣΚΟΡ')
                self.show_score_option()
                break
            elif ans == '2':
                # show settings
                print('ΡΥΘΜΙΣΕΙΣ')
                self.show_settings()
                break
            elif ans == '3':
                # start Scrabble game
                print('ΠΑΙΧΝΙΔΙ')
                self.run()
                break
            elif ans == 'q':
                # exit
                print('ΕΞΟΔΟΣ')
                exit()
                break

            print('Επίλεξε ξανά: ')
            

    def run(self):
        '''This class runs the game.'''

        # fill the sak again by taking letters amount
        # from letters_amount attribute
        for letter in self.sak.letters_amount:
            self.sak.letters_amount_copy.update({letter: self.sak.letters_amount.get(letter)})

        # randomize the sak & initialize players
        self.sak.randomize_sak()
        human = Human()
        computer = Computer()

        # παίζει πρώτα ο παίκτης-άνθρωπος
        self.current_player = human

        # εμφανίζουμε πόσα γράμματα είναι στην αρχή στο σακουλάκι 
        print(f'Στο σακουλάκι: {self.get_number_of_letters_in_sak()} γράμματα')
        print("Μοιράζουμε από 7 γράμματα σε κάθε παίκτη.")

        # κληρώνουμε για τους παίκτες 7 γράμματα για την πρώτη φορά που παίζουν
        letters_for_human = self.sak.getletters(7)
        letters_for_computer = self.sak.getletters(7)

        while self.end_of_game() == False:
            # self.current_player.play()
            # switch_turn

            if self.current_player == human:
                # human plays
                human.play()

                # create the available letters string (Κ,3 - Ε,3 - etc.)
                avail_let_string = create_available_letters_string(letters_for_human, self.sak.letters_weight)
                
                print(f'Στο σακουλάκι: {self.get_number_of_letters_in_sak()} γράμματα')
                print(f'Διαθέσιμα γράμματα: {avail_let_string}')
                word = input('ΛΕΞΗ: ')

                # if the player wants to stop the game
                if word == 'q':
                    self.end()


                # έλεγχος αν η λέξη αποτελείται από γράμματα 
                # που όντως διαθέτει ο παίκτης
                while not word_from_avail_letters(word, letters_for_human):
                    print(letters_for_human)
                    if word == 'p':
                        # όταν ο χρήστης δώσει 'p', τότε του κληρώνονται νέα γράμματα (εφόσον υπάρχουν),
                        # μετά επιστρέφονται τα προηγούμενα γράμματά του στο «σακουλάκι»
                        
                        if (self.sak.getletters(7) is None):
                            # if there are not 7 letters in the sak
                            # then end the game
                            self.end()
                        else:
                            letters_to_put_back = letters_for_human
                            letters_for_human = self.sak.getletters(7)
                            self.sak.putbackletters(letters_to_put_back)

                        # και χάνει την σειρά του
                        self.current_player = computer
                        break

                    print('Η λέξη δεν αποτελείται από τα διαθέσιμα γράμματα.')
                    word = input('ΛΕΞΗ: ')

                    # if the player wants to stop the game
                    if word == 'q':
                        self.end()

                
                if self.current_player == computer:
                    continue

                # έλεγχος αν η λέξη που δόθηκε περιλαμβάνεται 
                # στον κατάλογο αποδεκτών λέξεων
                
                file = 'greek7.txt'
                if (word != 'p'):
                    if word_in_file(word, file):
                        # αποδεκτή λέξη

                        # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
                        used_letters = []
                        for let in word:
                            used_letters.append(let)

                        # υπολογισμός και εμφάνιση σκορ
                        word_score = self.compute_word_score(word)
                        human.score += word_score
                        print(f'Αποδεκτή λέξη - Βαθμοί: {word_score} - Σκορ: {human.score}')
                        inp = input('Enter για Συνέχεια')

                        # if the player wants to stop the game
                        if word == 'q':
                            self.end()

                        if inp == '':   # or inp == 'p'
                            # βγάζουμε τα γράμματα που χρησιμοποιήθηκαν
                            print(letters_for_human)
                            for let in used_letters:
                                letters_for_human.remove(let)
                            
                            
                            # if the sak does not have the number of letters we need
                            # then end the game
                            if (self.sak.getletters(len(used_letters)) is None):
                                self.end()
                            else:
                                # else
                                # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι
                                # (τόσα όσα βγάλαμε)
                                for let in self.sak.getletters(len(used_letters)):
                                    letters_for_human.append(let)
                        
                            self.current_player = computer
                            #self.switch_turn()
                            continue

                    else:
                        print('Μη αποδεκτή λέξη')
                        self.current_player = computer
                        continue
                else:
                    # if word == 'p'
                    # if the sak does not have the number of letters we need
                    # then it's the turn of computer
                    if (self.sak.getletters(len(used_letters)) is None):
                        pass
                    else:            
                        letters_to_put_back = letters_for_human
                        letters_for_human = self.sak.getletters(7)
                        self.sak.putbackletters(letters_to_put_back)

                    # it's the turn of computer
                    self.current_player = computer
                    continue


            else:
                # computer plays
                computer.play()

                avail_let_string = create_available_letters_string(letters_for_computer, self.sak.letters_weight)
                
                print(f'Στο σακουλάκι: {self.get_number_of_letters_in_sak()} γράμματα')
                print(f'Διαθέσιμα γράμματα: {avail_let_string}')

                self.current_player = human
                continue


    def end(self):
        '''Ends the game, prints the winner and the final score.'''

        print('END OF GAME')

        # show this info of the current game that just ended
        print("Winner:")

        # save the game info

        # show the intro menu
        self.setup()


    def show_score_option(self):
        pass

    def show_settings(self):
        pass

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def end_of_game(self):
        '''If there are no letters remaining in the sak
        and no-one can make a valid word
        or if one player
        '''

        return False
    
    def compute_word_score(self, word):
        '''Computes the score of the word.'''
        score = 0
        for let in word:
            score += self.sak.letters_weight[let]
        return score

    def get_number_of_letters_in_sak(self) -> int:
        ''' Returns the number of letters remaining in the sak.'''
        count = 0
        print(self.sak.letters_amount_copy)
        for let in self.sak.letters_amount_copy:
            count += int(self.sak.letters_amount_copy.get(let))
        return count

# ΒΟΗΘΗΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ

def word_from_avail_letters(word, available_letters: list):
    ''' Checks whether the word consists 
    of the available letters'''

    # make a copy of available_letters list,
    # else it changes the list
    available_letters_copy = []
    for x in available_letters:
        available_letters_copy.append(x)

    for let in word:
        if let not in available_letters_copy:
            return False
        available_letters_copy.remove(let)
    return True

def word_in_file(word, file):
    '''Checks whether the word is in the given file.'''
    with open(file, 'r', encoding='utf8') as f:
        accepted_words = f.readlines()
        if word + '\n' in accepted_words:
            return True
        else:
            return False

def create_available_letters_string(letters_for_human: String, letters_weight: dict) -> String:
    avail_let_string = ''
    i = 1
    for let in letters_for_human:
        avail_let_string += f'{let},{letters_weight.get(let)}'
        if i < len(letters_for_human):
            avail_let_string += ' - '
        i += 1
    
    return avail_let_string



