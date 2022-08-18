import itertools
import random
from tokenize import String

# -------------------------------------------------------------------------
# - DONE
# - πόσα γράμματα στο σακουλάκι(ΟΚ)
# - το σακουλάκι να αρχικοποιείται με την αρχή ενός νέου παιχνιδιού (μάλλον ΟΚ)
# - στην αρχή για κάποιο λόγο βγάζει 28 γραμματα αντί για 14 (OK)
# - αφαιρεί 3 γράμματα ανά γράμμα (1 + 2 παραπάνω) που παίχτηκε, όταν πατάμε 'p' αφαιρεί 7 γράμματα (OK)
# - περιορισμός στο amount των letters (πρέπει amount >= 0 για κάθε γράμμα),
#   γιατί όταν τελειώνουν τα γράμματα το παιχνίδι συνεχίζει με
#   αρνητικό αριθμό γραμμάτων! (περίπου ΟΚ, γίνεται κάτι προς το τέλος)
# - 
# ---------------------------------------------------------------------------
# TODO:
# - μεταφορά στο Jupyter
# - dict for storing words from the file ('dict or list')
# - dictionary lets = {'A':[12, 1], 'B':[2, 5], etc.}
# - όνομα για τον παίκτη-άνθρωπο (προαιρετικά)
# - την τελευταία φορά, που ο άνθρωπος έχει 6 γράμματα, τον αφίνει 
#   να παίξει (μετά βέβαια σταματάει κανονικά) 
# - όταν τελειώνουν τα γράμματα, βγάζει error (for let in SakClass.getletters(len(used_letters)):
#   TypeError: 'NoneType' object is not iterable) 
# - smart-teach (δεν βρήκε την 2η καλύτερη λέξη), γενικά να την δουλέψουμε
# - 

# =====================================================================================
#                   ΥΠΟΘΕΣΕΙΣ
#
# Θεωρούμε ότι όταν ο παίκτης παίζει λέξη από τα 
# διαθέσιμα γράμματα αλλά είναι μη αποδεκτή τότε 
# χάνει την σειρά του χωρίς να ανανεωθούν τα γράμματά του
# (δεν του αφαιρούνται τα γράμματα που έπαιξε με την λέξη αυτή)
#
# =====================================================================================


FILE_GREEK = 'greek7.txt'

class SakClass:

    letters_weight = { 
        # letter: weight (the score the letter gives)

        "Α": 1,
        "Β": 8,
        "Γ": 4,
        "Δ": 4,
        "Ε": 1,
        "Ζ": 10,
        "Η": 1,
        "Θ": 10,
        "Ι": 1,
        "Κ": 2,
        "Λ": 3,
        "Μ": 3,
        "Ν": 1,
        "Ξ": 10,
        "Ο": 1,
        "Π": 2,
        "Ρ": 2,
        "Σ": 1,
        "Τ": 1,
        "Υ": 2,
        "Φ": 8,
        "Χ": 8,
        "Ψ": 10,
        "Ω": 3
    }

    letters_amount = {
        # letter: amount (number of letters remaining)

        "Α": 12,
        "Β": 1,
        "Γ": 2,
        "Δ": 2,
        "Ε": 8,
        "Ζ": 1,
        "Η": 7,
        "Θ": 1,
        "Ι": 8,
        "Κ": 4,
        "Λ": 3,
        "Μ": 3,
        "Ν": 6,
        "Ξ": 1,
        "Ο": 9,
        "Π": 4,
        "Ρ": 5,
        "Σ": 7,
        "Τ": 8,
        "Υ": 4,
        "Φ": 1,
        "Χ": 1,
        "Ψ": 1,
        "Ω": 3
    }

    letters_amount_copy = {}

    def __init__(self):   #, letters_weight:dict, letters_amount:dict):
        '''Initializes the sak.'''
        # self.letters_weight = letters_weight
        # self.letters_amount = letters_amount

        #letters

        # Here we create an attrbute that is a copy of letters_amount dictionary,
        # so that we can store all the letters in letters_amount and 
        # change only the copy. In this way, we can "refill" the sak 
        # again when a new game starts.
        letters_amount_copy = {}
        for letter in SakClass.letters_amount:
            letters_amount_copy.update({letter: SakClass.letters_amount.get(letter)})

    @staticmethod
    def randomize_sak():
        '''Randomizes the sak, like shuffling the letters.'''

        letter_list = []
        for letter in SakClass.letters_amount_copy:
            pair = [letter, SakClass.letters_amount_copy.get(letter, "Exception: the letter does not exist in the dict")]
            letter_list.append(pair)

        # shuffle the letter list 
        random.shuffle(letter_list)

        # empty the dict, and put there the new order of letters
        SakClass.letters_amount_copy = {}
        for pair in letter_list:
            SakClass.letters_amount_copy[pair[0]] = pair[1]

    @staticmethod
    def getletters(N: int):
        '''Returns letters by removing them from the sak, 
        so that the player has always 7 letters.
        Returns None if there are no letters in the sak.'''

        # create a copy of the dict, so that in case 
        # of failure (if there are not enough letters) the
        # letters would not be popped from the sak
        temp_letter_dict = {}
        for letter in SakClass.letters_amount_copy:
            temp_letter_dict.update({letter: SakClass.letters_amount_copy.get(letter)})

        letters_to_return = []
        for i in range(N):
            # print('DEBUG: getletters: i = ', i)
            # αν δεν υπάρχει άλλο γράμμα στο σακουλάκι

            let = SakClass.pop_letter(temp_letter_dict)
            if let is None:
                print('getletters: Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι.')
                # put back the letters we have taken from the real sak
                SakClass.putbackletters(letters_to_return)
                return None
            else:
                # αλλιώς (αν υπάρχει) βγάλε το γράμμα από το πραγματικό σακουλάκι
                let = SakClass.pop_letter(SakClass.letters_amount_copy)
                letters_to_return.append(let)
                SakClass.randomize_sak()
        return letters_to_return

    @staticmethod
    def putbackletters(letters:list):
        '''Puts the letters back to the sak.'''

        # for each letter in the given list,
        # find it in the dict letters_amount_copy and increment its amount
        for let in letters:
            # self.letters_amount_copy[let] += 1
            amount = SakClass.letters_amount_copy.get(let)
            SakClass.letters_amount_copy.update({let: amount + 1})
        
        return

    @staticmethod
    def pop_letter(letters_amount_copy: dict):
        ''' Takes a random letter from the sak.
        Returns None if there are no letters in the sak.'''

        # while amount of letter = 0 (i.e. letter does not exist)
        # and we are within the boundaries of the dict,
        # go to "next" letter of sack

        # TODO: bug: index out of bound (probably fixed)
        i = 0
        while letters_amount_copy.get(list(letters_amount_copy.keys())[i]) <= 0 and i < len(letters_amount_copy) - 1:
            # print(len(letters_amount_copy))
            # print('Debug: pop_letter: i = ', i)
            i += 1

        if letters_amount_copy.get(list(letters_amount_copy.keys())[i]) > 0 and i < len(letters_amount_copy):
            # found a letter
            letter = list(letters_amount_copy.keys())[i]  # takes a letter # we put list() so that we can have access
            # print('Debug: pop_letter: letter = ', letter)
            letters_amount_copy[list(letters_amount_copy.keys())[i]] -= 1  # and reduces its frequency-amount
            # print('Debug: pop_letter: letters_amount_copy[list(letters_amount_copy.keys())[i]] = ',
                                    #   letters_amount_copy[list(letters_amount_copy.keys())[i]])
            # here we print the amount of available remaining letters
            return letter
        else:
            print('Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι.')
            return None


class Game:
    '''
    Represents the game.
    '''

    def __init__(self):   #, sak: SakClass):
        '''Initializes the sak.
        '''
        self.sak = SakClass()
        self.ph = Human()
        self.pc = Computer()
        self.current_player = None
        self.computer_algorithm = 1 # MIN is default

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
        # because the sak has changed from the previous game
        for letter in self.sak.letters_amount:
            self.sak.letters_amount_copy.update({letter: self.sak.letters_amount.get(letter)})

        # randomize the sak & initialize players
        SakClass.randomize_sak()
        # human = Human(self.sak)
        # computer = Computer(self.sak)

        # παίζει πρώτα ο παίκτης-άνθρωπος
        self.current_player = self.ph

        # εμφανίζουμε πόσα γράμματα είναι στην αρχή στο σακουλάκι 
        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
        print("Μοιράζουμε από 7 γράμματα σε κάθε παίκτη.")

        print()

        # κληρώνουμε για τους παίκτες 7 γράμματα για την πρώτη φορά που παίζουν
        self.ph.letters = SakClass.getletters(7)
        self.pc.letters = SakClass.getletters(7)

        while self.end_of_game() == False:
            # self.current_player.play()
            # switch_turn

            if self.current_player == self.ph:
                # human plays
                self.ph.play()

                if create_available_letters_string(self.ph.letters, self.sak.letters_weight) is None:
                    self.end()
                # else    
                # create the available letters string (Κ,3 - Ε,3 - etc.)
                avail_let_string = create_available_letters_string(self.ph.letters, self.sak.letters_weight)
                
                print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
                print(f'Διαθέσιμα γράμματα: {avail_let_string}')
                word = input('ΛΕΞΗ: ')

                # smart-teach
                if self.computer_algorithm == 4:
                    self.pc.take_human_word(word)
                    self.pc.take_human_letters(self.ph.letters)

                # if the player wants to stop the game
                if word == 'q':
                    print('==============================================')
                    self.end()


                # έλεγχος αν η λέξη αποτελείται από γράμματα 
                # που όντως διαθέτει ο παίκτης
                while not word_from_avail_letters(word, self.ph.letters):
                    print(self.ph.letters)
                    if word == 'p':
                        # όταν ο χρήστης δώσει 'p', τότε του κληρώνονται νέα γράμματα (εφόσον υπάρχουν),
                        # μετά επιστρέφονται τα προηγούμενα γράμματά του στο «σακουλάκι»
                        
                        human_letters = SakClass.getletters(7)
                        if human_letters is None:
                            # if there are not 7 letters in the sak
                            # then end the game
                            self.end()
                        else:
                            letters_to_put_back = self.ph.letters
                            self.ph.letters = human_letters
                            self.sak.putbackletters(letters_to_put_back)

                        # και χάνει την σειρά του
                        self.current_player = self.pc
                        break

                    print('Η λέξη δεν αποτελείται από τα διαθέσιμα γράμματα.')
                    word = input('ΛΕΞΗ: ')

                    # if the player wants to stop the game
                    if word == 'q':
                        print('==============================================')
                        self.end()

                
                if self.current_player == self.pc:
                    continue

                # έλεγχος αν η λέξη που δόθηκε περιλαμβάνεται 
                # στον κατάλογο αποδεκτών λέξεων
                
                if word != 'p':
                    if word_in_file(word, FILE_GREEK):
                        # αποδεκτή λέξη

                        # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
                        used_letters = []
                        for let in word:
                            used_letters.append(let)

                        # υπολογισμός και εμφάνιση σκορ
                        word_score = compute_word_score(word)
                        self.ph.score += word_score
                        print(f'Αποδεκτή λέξη - Βαθμοί: {word_score} - Σκορ: {self.ph.score}')
                        inp = input('Enter για Συνέχεια')
                        print('==============================================')

                        # if the player wants to stop the game
                        if word == 'q':
                            print('==============================================')
                            self.end()

                        if inp == '':   # or inp == 'p'
                            # βγάζουμε τα γράμματα που χρησιμοποιήθηκαν
                            print('DEBUG: ', self.ph.letters)
                            for let in used_letters:
                                self.ph.letters.remove(let)
                            
                            
                            human_letters = SakClass.getletters(len(used_letters))
                            # if the sak does not have the number of letters we need
                            # then end the game
                            if human_letters is None:
                                self.end()
                            else:
                                # else
                                # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι
                                # (τόσα όσα βγάλαμε)
                                # if (SakClass.getletters(len(used_letters)) is not None):                                
                                for let in human_letters:
                                    self.ph.letters.append(let)
                        
                            self.current_player = self.pc
                            #self.switch_turn()
                            continue

                    else:
                        print('Μη αποδεκτή λέξη')
                        print('==============================================')
                        self.current_player = self.pc
                        continue
                else:
                    # if word == 'p'
                    # if the sak does not have the number of letters we need
                    # then it's the turn of computer
                    human_letters = SakClass.getletters(7)
                    if human_letters is None:
                        pass
                    else:            
                        letters_to_put_back = self.ph.letters
                        self.ph.letters = human_letters
                        self.sak.putbackletters(letters_to_put_back)

                    # it's the turn of computer
                    self.current_player = self.pc
                    continue


            else:
                # computer plays
                self.pc.play(self.computer_algorithm)
                print('==============================================')

                self.current_player = self.ph
                continue

    def end(self):
        '''Ends the game, prints the winner and the final score.'''

        print('END OF GAME')

        print()
        # show this info of the current game that just ended
        print("Winner:")

        # save the game info

        # show the intro menu
        self.setup()

    def show_score_option(self):
        pass

    def show_settings(self):
        print("Επίλεξε τον αλγόριθμο:")

        while True:
            print('--------------------')
            print('1: MIN (default)')
            print('2: MAX')
            print('3: SMART')
            print('4: SMART-TEACH')
            print('q: Έξοδος από Ρυθμίσεις')
            print('--------------------')
            ans = input('Επίλεξε από το μενού: ')

            if ans == '1':               
                print('MIN')
                self.computer_algorithm = 1
                self.setup()
            elif ans == '2':
                print('MAX')
                self.computer_algorithm = 2
                self.setup()
            elif ans == '3':
                print('SMART')
                self.computer_algorithm = 3
                self.setup()
            elif ans == '4':
                print('SMART-TEACH')
                self.computer_algorithm = 4
                self.setup()
            elif ans == 'q':
                # exit from settings
                print('Εξοδος από Ρυθμίσεις')
                self.setup()
                break
            else:
                print('Μη έγκυρη επιλογή.')

            print('Επίλεξε ξανά: ')

    def switch_turn(self):
        if self.current_player == self.ph:
            self.current_player = self.pc
        else:
            self.current_player = self.ph

    def end_of_game(self):
        '''If there are no letters remaining in the sak
        and no-one can make a valid word
        or if one player
        '''

        return False
    
    def get_number_of_letters_in_sak() -> int:
        ''' Returns the number of letters remaining in the sak.'''
        count = 0
        #print(self.sak.letters_amount_copy)
        for let in SakClass.letters_amount_copy:
            count += int(SakClass.letters_amount_copy.get(let))
        return count

    def get_ph(self):
        return self.ph
class Player():
    def __init__(self):   #, sak: SakClass, game: Game):
        self.score = 0
        self.letters = []
        # self.sak = sak
        # self.game = game

    def __repr__(self):
        pass


class Human(Player):
    def __init__(self):   #, sak: SakClass, game: Game):
        super().__init__()

    def __repr__(self):
        pass

    def play(self):
        print('Παίζεις:')


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.human_word = ""
        self.human_letters = ""

    def __repr__(self):
        pass
    
    def play(self, algorithm_number: int):
        print('Παίζει ο Η/Υ:')
        
        if create_available_letters_string(self.letters, SakClass.letters_weight) is None:
            self.end()
        # else    
        # create the available letters string (Κ,3 - Ε,3 - etc.)
        avail_let_string = create_available_letters_string(self.letters, SakClass.letters_weight)
        
        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
        print(f'Διαθέσιμα γράμματα: {avail_let_string}')


        if algorithm_number == 1:
            # play MIN
            self.min()
        elif algorithm_number == 2:
            # play MAX
            self.max()
        elif algorithm_number == 3:
            # play SMART
            self.smart()
        elif algorithm_number == 4:
            # play SMART-TEACH
            self.smart_teach()
        else:
            print('Error: Invalid algorithm_number')
    
    def min(self):
        for i in range(2, 8):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:
                    # print('DEBUG: let = ', let)
                    word = word + let
                print('DEBUG: MIN: word = ', word)

                if word_in_file(word, FILE_GREEK):
                    print('DEBUG: Accepted ', word)

                    # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
                    used_letters = []
                    for let in word:
                        used_letters.append(let)

                    # play the word
                    word_score = compute_word_score(word)
                    self.score += word_score
                    print(f'Λέξη Η/Υ: {word} - Βαθμοί: {word_score} - Σκορ: {self.score}')

                    print('DEBUG: ', self.letters)
                    for let in used_letters:
                        self.letters.remove(let)
                    
                    
                    # if the sak does not have the number of letters we need
                    # then end the game

                    computer_letters = SakClass.getletters(len(used_letters))
                    if computer_letters is None:
                        return 1    # end-the-game code 
                    else:
                        # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)
                        # if SakClass.getletters(len(used_letters)) is not None:                                
                        for let in computer_letters:
                            self.letters.append(let)

                    return

        # could not find a valid word
        # play pass

        # if the sak does not have the number of letters we need
        # then the computer looses its turn
        lets = SakClass.getletters(7)
        if lets is None:
            pass
        else:            
            letters_to_put_back = self.letters
            self.letters = lets
            SakClass.putbackletters(letters_to_put_back)
        
        return

    def max(self):
        print('Παρακαλώ περίμενε λίγο.')
        for i in range(7, 1, -1):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:
                    # print('DEBUG: let = ', let)
                    word = word + let
                print('DEBUG: MAX: word = ', word)

                if word_in_file(word, FILE_GREEK):
                    print('DEBUG: Accepted ', word)

                    # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
                    used_letters = []
                    for let in word:
                        used_letters.append(let)

                    # play the word
                    word_score = compute_word_score(word)
                    self.score += word_score
                    print(f'Λέξη Η/Υ: {word} - Βαθμοί: {word_score} - Σκορ: {self.score}')

                    print('DEBUG: ', self.letters)
                    for let in used_letters:
                        self.letters.remove(let)
                    
                    
                    # if the sak does not have the number of letters we need
                    # then end the game
                    lets = SakClass.getletters(len(used_letters))
                    if lets is None:
                        return 1    # end-the-game code 
                    else:
                        # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)
                        # if SakClass.getletters(len(used_letters)) is not None:                                
                        for let in lets:
                            self.letters.append(let)

                    return

        # could not find a valid word
        # play pass

        # if the sak does not have the number of letters we need
        # then the computer loses its turn

        lets = SakClass.getletters(7)
        if lets is None:
            pass
        else:            
            letters_to_put_back = self.letters
            self.letters = lets
            SakClass.putbackletters(letters_to_put_back)
        
        return

    def smart(self):
        print('Παρακαλώ περίμενε λίγο.')
        accepted_words = {}
        for i in range(2, 8):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:
                    # print('DEBUG: let = ', let)
                    word = word + let
                # print('DEBUG: SMART: word = ', word)

                if word_in_file(word, FILE_GREEK):
                    print('DEBUG: Accepted ', word)
                    word_score = compute_word_score(word)

                    # αποθήκευσε τη λέξη με το σκορ της στο λεξικό
                    accepted_words.update({word: word_score})

                    
        if len(accepted_words) != 0: 
            # dict is not empty
            # find the word with the maximum score
            max_score = 0
            for w in accepted_words.keys():
                temp_score = compute_word_score(w)
                
                if temp_score > max_score:
                    max_score = temp_score
                    word_with_max_score = w

                print(f'DEBUG: w, max_score = {w}, {max_score}')

            # play the word
            print(f'DEBUG: accepted_words = {accepted_words}')
            self.score += max_score
            print(f'Λέξη Η/Υ: {word_with_max_score} - Βαθμοί: {max_score} - Σκορ: {self.score}')

            # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
            used_letters = []
            for let in word_with_max_score:
                used_letters.append(let)

            print('DEBUG: ', self.letters)
            for let in used_letters:
                self.letters.remove(let)
            
            # if the sak does not have the number of letters we need
            # then end the game
            lets = SakClass.getletters(len(used_letters))
            if lets is None:
                return 1    # end-the-game code 
            else:
                # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)
                # if SakClass.getletters(len(used_letters)) is not None:                                
                for let in lets:
                    self.letters.append(let)
        else:
            # dict is empty, i.e. could not find a valid word
            # play pass
            print('Could not find the word.')

            # if the sak does not have the number of letters we need
            # then the game ends 
            lets = SakClass.getletters(7)
            if lets is None:
                return 1   # return exit code 1 = end-of-game
            else:            
                letters_to_put_back = self.letters
                self.letters = lets
                SakClass.putbackletters(letters_to_put_back)
            
        return

    def smart_teach(self):
        # human plays
        two_best_words = self.find_two_best_words()
        if self.human_word == two_best_words[0]:
            print('Συγχαρητήρια! Έπαιξες την καλύτερη δυνατή λέξη!')
        elif self.human_word == two_best_words[1]:
            print('Συγχαρητήρια! Έπαιξες την 2η καλύτερη δυνατή λέξη!')
        else:
            print('Η λέξη που έπαιξες δεν είναι η καλύτερη δυνατή.')
            print('Θα μπορούσες να παίξεις τις εξής:')
            print(f'1η καλύτερη: {two_best_words[0]}')
            print(f'2η καλύτερη: {two_best_words[1]}')

        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
    
        # computer plays
        self.smart()


    def take_human_word(self, word: String):
        self.human_word = word        

    def take_human_letters(self, letters: list):
        self.human_letters = letters

    def find_two_best_words(self) -> list:
        print('Παρακαλώ περίμενε λίγο.')
        accepted_words = {}
        for i in range(2, 8):
            for perm in itertools.permutations(self.human_letters, i):
                word = ''
                for let in perm:
                    # print('DEBUG: let = ', let)
                    word = word + let
                # print('DEBUG: find_two_best_words: word = ', word)

                if word_in_file(word, FILE_GREEK):
                    print('DEBUG: Accepted ', word)
                    word_score = compute_word_score(word)

                    # αποθήκευσε τη λέξη με το σκορ της στο λεξικό
                    accepted_words.update({word: word_score})

                    
        if len(accepted_words) != 0: 
            # dict is not empty
            # find the word with the maximum score
            max_score1 = 0
            max_score2 = 0
            word_with_max_score1 = ""
            word_with_max_score2 = ""
            for w in accepted_words.keys():
                temp_score = compute_word_score(w)
                
                if temp_score > max_score1:
                    max_score2 = max_score1
                    max_score1 = temp_score
                    word_with_max_score2 = word_with_max_score1
                    word_with_max_score1 = w

                print(f'DEBUG: w, max_score1, max_score2 = {w}, {max_score1}, {max_score2}')

            # play the word
            print(f'DEBUG: accepted_words = {accepted_words}')
            best_word = word_with_max_score1
            second_best_word = word_with_max_score2
        else:
            # dict is empty, i.e. could not find a valid word
            # play pass
            print('Could not find the word.')
            return None

        return [best_word, second_best_word]

    
        print('Παρακαλώ περίμενε λίγο.')
        accepted_words = {}
        for i in range(2, 8):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:
                    # print('DEBUG: let = ', let)
                    word = word + let
                #print('DEBUG: find_best_word: word = ', word)

                if word_in_file(word, FILE_GREEK):
                    print('DEBUG: Accepted ', word)
                    word_score = compute_word_score(word)

                    # αποθήκευσε τη λέξη με το σκορ της στο λεξικό
                    accepted_words.update({word: word_score})

           
        if len(accepted_words) != 0: 
            # dict is not empty
            # find the word with the maximum score
            max_score = 0
            for w in accepted_words.keys():
                temp_score = compute_word_score(w)
                
                if temp_score > max_score and w != self.find_best_word():
                    max_score = temp_score
                    word_with_max_score = w

                print(f'DEBUG: w, max_score = {w}, {max_score}')

            # play the word
            print(f'DEBUG: accepted_words = {accepted_words}')
            second_best_word = word_with_max_score
        else:
            # dict is empty, i.e. could not find a valid word
            # play pass
            print('Could not find the word.')
            return None

        return second_best_word



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

def create_available_letters_string(letters_of_player: String, letters_weight: dict) -> String:
    if letters_of_player is None:
        print('create_available_letters_string: letters_of_player is None')
        return None

    avail_let_string = ''
    i = 1
    for let in letters_of_player:
        avail_let_string += f'{let},{letters_weight.get(let)}'
        if i < len(letters_of_player):
            avail_let_string += ' - '
        i += 1
    
    return avail_let_string

def compute_word_score(word):
    '''Computes the score of the word.'''

    score = 0
    for let in word:
        score += SakClass.letters_weight[let]
    return score