import random

class SakClass:
    def __init__(self, letters_weight, letters_amount):
        self.letters_weight = letters_weight
        self.letters_amount = letters_amount

    def randomize_sak(self):
        letter_list = []
        for letter in self.letters_amount:
            pair = [letter, self.letters_amount[letter]]
            letter_list.append(pair)

        # shuffle the letters_amount dict
        random.shuffle(letter_list)

        # empty the dict, and put there the new order of letters
        self.letters_amount = {}
        for pair in letter_list:
            self.letters_amount[pair[0]] = pair[1]

    def getletters(self, N):
        '''Returns N letters by removing them from the sak.'''

        letters_to_return = []
        for i in range(N):
            letters_to_return.append(self.pop_letter(self.letters_amount))
            self.randomize_sak()
        return letters_to_return

    def putbackletters(self, letters):
        '''Puts the letters back to the sak.'''

        pass

    def pop_letter(self, letters_amount):
        # where letters_amount is a dictionary

        # while amount of letter = 0 (i.e. letter does not exist)
        # and we are within the boundaries of the dict,
        # go to "next" letter of sack

        # TODO: bug: index out of bound
        i = 0
        while letters_amount[list(letters_amount.keys())[i]] <= 0 and i <= len(letters_amount):
            # print(len(letters_amount))
            i += 1

        if i <= len(letters_amount):
            # found a letter
            letter = list(letters_amount.keys())[i]  # takes a letter # we put list() so that we can have access
            letters_amount[list(letters_amount.keys())[i]] -= 1  # and reduces its frequency
            print(letters_amount[list(letters_amount.keys())[i]])
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
        pass


class Computer(Player):
    def __init__(self):
        pass

    def __repr__(self):
        pass
    
    def play(self):
        print('Computer is playing')
        pass



class Game:
    '''
    Represents the game.
    '''

    def __init__(self, sak: SakClass, player1, player2):
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

        self.sak.randomize_sak()
        # self.current_player = self.player1

        human = Human()
        computer = Computer()

        while self.end_of_game() == False:
            # κληρώνουμε για τους παίκτες 7 γράμματα

            letters_for_human = self.sak.getletters(7)
            letters_for_computer = self.sak.getletters(7)

            print('Διαθέσιμα γράμματα: ')
            print(letters_for_human)
            word = input('ΛΕΞΗ: ')

            # έλεγχος αν η λέξη αποτελείται από γράμματα 
            # που όντως διαθέτει ο παίκτης
            while not word_from_avail_letters(word, letters_for_human):
                print('Η λέξη δεν αποτελείται από τα διαθέσιμα γράμματα.')
                word = input('ΛΕΞΗ: ')

            # έλεγχος αν η λέξη που δόθηκε περιλαμβάνεται 
            # στον κατάλογο αποδεκτών λέξεων
            
            file = 'greek7.txt'
            if (word != 'p'):
                if word_in_file(word, file):
                    # αποδεκτή λέξη
                    word_score = self.compute_word_score(word)
                    human.score += word_score
                    print(f'Αποδεκτή λέξη - Βαθμοί: {word_score} - Σκορ: {human.score}')
                    inp = input('Enter για Συνέχεια')

                    if inp == 'Enter' or inp == 'p':
                        letters_for_human = self.sak.getletters(7)
                        continue
                else:
                    print('Μη αποδεκτή λέξη')
            else:
                previous_letters = letters_for_human
                letters_for_human = self.sak.getletters(7)
                self.sak.putbackletters(previous_letters)
                continue


            # self.current_player.play()
            # self.switch_turn()


    def end(self):
        '''Ends the game, prints the winner and the final score.'''
        print('END OF GAME')


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


# ΒΟΗΘΗΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ

def word_from_avail_letters(word, available_letters):
    ''' Checks whether the word consists 
    of the available letters'''

    for let in word:
        if let not in available_letters:
            return False
    return True

def word_in_file(word, file):
    '''Checks whether the word is in the given file.'''
    with open(file, 'r', encoding='utf8') as f:
        accepted_words = f.readlines()
        if word + '\n' in accepted_words:
            return True
        else:
            return False

