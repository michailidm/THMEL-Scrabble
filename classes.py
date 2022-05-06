class Game():
    
    def __init__(self, sak):
        self.sak = SakClass(sak)
        pass

    def __repr__(self):
        pass

    def setup(self):
        print("***** Scrable *****")
        while True:
            print("-------------------")
            print("1: Σκορ\n2: Ρυθμίσεις\n3: Παιχνίδι\nq: Έξοδος")
            print("-------------------")
            ans = input("Επίλεξε από το μενού: ")

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
        pass

        if ans == 1:
            pass
        elif ans == 2:
            pass
        elif ans == 3:
            # start Scrabble
            self.run()
            pass
        elif ans == 'q':
            # exit
            pass

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

        self.sak.randomize_sak()

        available_letters = self.sak.getletters(7)

        print('Διαθέσιμα γράμματα: ' + available_letters)        

    def end(self):
        pass


class SakClass():
    def __init__(self, sak):
        self.sak = sak
        
        
    def randomize_sak(self):
        print('The sak was randomized.')

    def getletters(self, N):
        '''Returns N letters by removing them from the sak.'''
        letters_to_return = []
        for i in range(N):
            letters_to_return.append(pop_letter(self.sak))

        return letters_to_return

    def putbackletters(self):
        pass

def pop_letter(self, sak):
    # where sak is a dictionary
    letter = sak.keys()[0]  # takes a letter
    sak[sak.keys()[0]][1] -= 1  # and reduces its frequency
    # TODO: when freq=0

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

