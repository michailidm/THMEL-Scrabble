import random


def showScore():
    pass


def showSettings():
    pass


class Game:

    # sak is of type SakClass
    def __init__(self, sak):
        self.sak = sak

    def __repr__(self):
        pass

    def setup(self):
        print("***** Scrabble *****")
        while True:
            print('-------------------')
            print('1: Σκορ')
            print('2: Ρυθμίσεις')
            print('3: Παιχνίδι')
            print('q: Έξοδος')
            print('-------------------')
            ans = input('Επίλεξε από το μενού: ')

            if ans == '1':
                print('Σκορ')
                break
            elif ans == '2':
                print('Ρυθμίσεις')
                break
            elif ans == '3':
                print('Παιχνίδι')
                break
            elif ans == 'q':
                print('Έξοδος')
                break

            print('Επίλεξε ξανά: ')


        if ans == '1':
            # show score
            showScore()
        elif ans == '2':
            # show settings
            showSettings()
        elif ans == '3':
            # start Scrabble game
            self.run()
        elif ans == 'q':
            # exit
            exit()

    def run(self):
        """
        menu = {}
        menu['1'] = "Σκορ"
        menu['2'] = "Ρυθμίσεις"
        menu['3'] = "Παιχνίδι"
        menu['q'] = "Έξοδος"


        while True:
            options = menu.keys()
            for entry in options:
                print(entry, ":", menu[entry])

            selection = input("Please Select:")
            if selection == '1':
                pass
                #print "add"
            elif selection == '2':
                pass
                #print "delete"
            elif selection == '3':
                pass
                #print "find"
            elif selection == 'q':
                pass
                #break
            else:
                pass
                #print "Unknown Option Selected!"

        """

        print("Running Scrabble")
        self.sak.randomize_sak()
        available_letters = self.sak.getletters(7)
        # print(self.sak.getletters(2))
        print('Διαθέσιμα γράμματα: ')
        print(available_letters)

    def end(self):
        pass


class SakClass():
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

        self.letters_amount = {}
        for pair in letter_list:
            self.letters_amount[pair[0]] = pair[1]



    def getletters(self, N):
        '''Returns N letters by removing them from the sak.'''
        letters_to_return = []
        for i in range(N):
            letters_to_return.append(pop_letter(self.letters_amount))
            self.randomize_sak()

        return letters_to_return

    def putbackletters(self):
        pass

def pop_letter(letters_amount):
    # where letters_amount is a dictionary
    letter = list(letters_amount.keys())[0]  # takes a letter # we put list() so that we can have access
    letters_amount[list(letters_amount.keys())[0]] -= 1  # and reduces its frequency
    # TODO: when freq=0
    print(letters_amount[list(letters_amount.keys())[0]])
    return letter

class Player():
    def __init__(self):
        pass

    def __repr__(self):
        pass



class Human(Player):
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def play(self):
        pass


class Computer(Player):
    def __init__(self):
        pass

    def __repr__(self):
        pass
    
    def play(self):
        pass

