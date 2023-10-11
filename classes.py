from copy import deepcopy
import random
from tokenize import String
from xmlrpc.client import boolean
from letters import lets as LETS
import itertools


def guidelines():
    '''
=====================================================================================

Η εργασία περιλαμβάνει τα εξής αρχεία:
    - classes.py, που περιέχει όλες τις κλάσεις του προγράμματος
    - main.ipynb, που είναι το κυρίως πρόγραμμα σε Jupyter Notebook
    - main.py
    - letters.py, που περιέχει την δομή LETS με τα γράμματα μαζί με την 
    πληθικότητα και τους πόντους τους
    - word_dict.json, που περιέχει το λεξικό με τις λέξεις του αρχείου greek7.txt
    - game_info.json, που περιέχει τις πληροφορίες για τις παρτίδες που παίχτηκαν

Τα δύο τελευταία αρχεία δημιουργούνται και αυτόματα από τον κώδικα του προγράμματος.

Το αρχείο main.py υπάρχει σε περίπτωση που υπάρξει πρόβλημα με την 
χρήση του main.ipynb.

Επιπλέον, στην εργασία συμπεριλαμβάνονται και οι φάκελοι __pycache__ και .ipynb_checkpoints, 
οι οποίοι επίσης δημιουργούνται αυτόματα.

Για να τρέξουμε το πρόγραμμα, αρχικά προσθέτουμε στον φάκελο όπου βρίσκονται τα 
αρχεία της εργασίας (PythonScrabble) το αρχείο greek7.txt. Στη συνέχεια, 
ανοίγουμε το αρχείο main.ipynb στο Jupyter Notebook και τρέχουμε τα κελιά.

Σε περίπτωση που στη διάρκεια της εκτέλεσης του προγράμματος προκύψει κάποιο exception 
και διακοπεί το πρόγραμμα, το ξανατρέχουμε. 

-------------------------------------------------------------------------
Θεωρούμε ότι όταν ο παίκτης παίζει λέξη από τα 
διαθέσιμα γράμματα αλλά είναι μη αποδεκτή τότε 
χάνει την σειρά του χωρίς να ανανεωθούν τα γράμματά του 
(δεν του αφαιρούνται τα γράμματα που έπαιξε με την λέξη αυτή).

-------------------------------------------------------------------------
Δομή (λίστα ή λεξικό-dictionary) με την οποία οργανώνουμε τις λέξεις της γλώσσας 
στη διάρκεια του παιχνιδιού:
Χρησιμοποιούμε λεξικό για να αποθηκεύσουμε τις λέξεις του greek7.txt,
επειδή όταν έχουμε πολλά δεδομένα η αναζήτηση στο λεξικό είναι πιο γρήγορη
από ότι στη λίστα.

-------------------------------------------------------------------------
Χρησιμοποιήσαμε μορφή .json για την αποθήκευση σε αρχεία, επειδή είναι πιο 
ασφαλής από την μορφή pickle.

-------------------------------------------------------------------------
 Ο παίκτης-άνθρωπος μπορεί να παίξει λέξη με ένα γράμμα και να είναι αποδεκτή
 (είναι αποδεκτές όλες οι λέξεις με ένα γράμμα εκτός από το Α), 
 ενώ ο Η/Υ παίζει# υποχρεωτικά λέξεις με 2 ή παραπάνω γράμματα.
Αυτό σημαίνει ότι ο άνθρωπος έχει ένα πλεονέκτημα έναντι του Η/Υ.

--------------------------------------------------------------------------
Οι πληροφορίες για τις παρτίδες είναι αποθηκευμένες στο αρχείο game_info.json
μόνο όσο τρέχει το πρόγραμμα. Όταν σταματήσει το πρόγραμμα και το τρέξουμε 
στη συνέχεια εκ νέου, χάνονται όλες οι προηγούμενες πληροφορίες και 
καταγράφονται μόνο οι νέες. Δηλαδή μπορούμε να δούμε το σκορ μόνο από 
τις παρτίδες που παίξαμε μέχρι να επιλέξουμε 'Έξοδος' από το κεντρικό μενού.

---------------------------------------------------------------------------

ΑΛΓΟΡΙΘΜΟΙ Η/Υ:
    Οι αλγόριθμοι Η/Υ που υλοποιήσαμε είναι ο αλγόριθμος στο Σενάριο 1 και 
    στο Σενάριο 5 και είναι οι εξής:

    - ΜΙΝ Letters: 
        Το πρόγραμμα δημιουργεί όλες τις δυνατές μεταθέσεις
        (permutations) των γραμμάτων που διαθέτει ο Η/Υ ξεκινώντας από 2 και
        ανεβαίνοντας μέχρι τα 7 γράμματα. Για κάθε μετάθεση ελέγχει αν είναι
        αποδεκτή λέξη και παίζει την πρώτη αποδεκτή λέξη που θα εντοπίσει.

    - ΜΑΧ Letters: 
        Όπως και στο MIN αλλά το πρόγραμμα ξεκινά από τις
        μεταθέσεις των γραμμάτων ανά 7 και κατεβαίνει προς το 2. Παίζει πάλι την
        πρώτη αποδεκτή λέξη αλλά τώρα αυτή με τα περισσότερα γράμματα.

    - SMART: 
        Όπως και στο MIN αλλά εξαντλεί όλες τις μεταθέσεις 2 ως και 7
        γραμμάτων χωρίς να σταματά. Βρίσκει τις αποδεκτές λέξεις και στο τέλος
        παίζει τη λέξη που δίνει τους περισσότερους βαθμούς.

    - SMART-TEACH:
        SMART: Ο αλγόριθμος όπως εξηγήθηκε παραπάνω.
        TEACH: Ο υπολογιστής «διδάσκει» τον παίκτη, δηλ. τον ενημερώνει ποια
        θα ήταν η καλύτερη λέξη να παίξει.
        Όταν είναι σειρά του παίκτη-ανθρώπου να παίξει, ο υπολογιστής εκτελεί
        επίσης τον αλγόριθμο SMART.
        Αφού παίξει ο παίκτη κάποια λέξη ο υπολογιστής ενημερώνει τον παίκτη
        αν η λέξη που έπαιξε είναι η καλύτερη δυνατή. Αν δεν είναι, τότε τον
        ενημερώνει ποια θα ήταν η καλύτερη ή και η 2η καλύτερη λέξη που θα
        μπορούσε να παίξει.


=====================================================================================
    Κλάση SakClass:
        Αναπαριστά το σακουλάκι με τα γράμματα. Έχει τις εξής μεθόδους: 

        __init__(): 
            Αρχικοποιεί το σακουλάκι.
            
        randomize_sak(): 
            Ανακατεύει το σακουλάκι. Χρησιμοποιήσαμε τον decorator @staticmethod.

        getletters(N: int):
            Επιστρέφει Ν γράμματα βγάζοντάς τα από το σακουλάκι.
            Επιστρέφει None αν δεν υπάρχουν γράμματα στο σακουλάκι.
            Χρησιμοποιήσαμε τον decorator @staticmethod.
    
        putbackletters(letters:list):
            Βάζει πίσω στο σακουλάκι τα γράμματα της 
            λίστας που παίρνει σαν παράμετρο.
            Χρησιμοποιήσαμε τον decorator @staticmethod.

        pop_letter(letters_dict: dict):
            Βγάζει ένα τυχαίο γράμμα από το σακουλάκι. 
            Επιστρέφει None αν δεν υπάρχουν γράμματα στο σακουλάκι.
            Χρησιμοποιήσαμε τον decorator @staticmethod.


    Κλάση Game:
        Αναπαριστά το πώς εξελίσσεται μια παρτίδα (game).
        Έχει τις εξής μεθόδους:

        __init__():
            Αρχικοποιεί το σακουλάκι.

        __repr__(self):
            Επιστρέφει πληροφορίες για το αντικείμενο που χρησιμεύουν στην αποσφαλμάτωση.

        setup(self):
            Εμφανίζει το κεντρικό μενού του παιχνιδιού και δέχεται είσοδο από τον χρήστη για
            την επιλογή. Στη συνέχεια, εκτελεί την αντίστοιχη επιλογή.
        
        run(self):
            Τρέχει το παιχνίδι. 

        end(self):
            Τερματίζει το παιχνίδι, εκτυπώνει τον νικητή και το τελικό σκορ.
        
        show_score_option(self):
            Εμφανίζει τον Πίνακα Σκορ.

        show_settings(self):
            Εμφανίζει τις ρυθμίσεις, από όπου ο χρήστης μπορεί να επιλέξει
            τον αλγόριθμο με τον οποίο θα παίζει ο Η/Υ.

        get_number_of_letters_in_sak() -> int:
            Επιστρέφει τον αριθμό των γραμμάτων που απέμειναν μέσα στο σακουλάκι.

        get_winner(self):
            Επιστρέφει τον νικητή.

    
    Κλάση Player:
        Αναπαριστά έναν παίκτη.

        __init__():
            Αρχικοποιεί το αντικείμενο.
        
        __repr__():
            Επιστρέφει πληροφορίες για το αντικείμενο οι οποίες χρησιμεύουν στην αποσφαλμάτωση.


    Κλάση Human:
        Αναπαριστά έναν παίκτη-άνθρωπο. Κληρονομεί από την κλάση Player.

        __init__():
            Αρχικοποιεί το αντικείμενο. Επεκτείνει την κλάση __init__() της κλάσης Player. 

        __repr__():
            Επιστρέφει πληροφορίες για το αντικείμενο οι οποίες χρησιμεύουν στην αποσφαλμάτωση.

        play():
            Εμφανίζει το μήνυμα 'Παίζεις:'.
            (Κανονικά θα έπρεπε να τρέχει τον αλγόριθμο του παίκτη,
            ο αλγόριθμος αυτός υλοποιείται στη μέθοδο run της Game.)

    Κλάση Computer:
        Αναπαριστά έναν παίκτη-υπολογιστή. Κληρονομεί από την κλάση Player.

        __init__():
            Αρχικοποιεί το αντικείμενο. Επεκτείνει την κλάση __init__() της κλάσης Player.

        __repr__():
            Επιστρέφει πληροφορίες για το αντικείμενο οι οποίες χρησιμεύουν στην αποσφαλμάτωση.

        play():
            Καλείται όταν είναι η σειρά του υπολογιστή να παίξει.
        
        min(self):
            Αυτός ο αλγόριθμος εξετάζει όλους τους συνδυασμούς των γραμμάτων 
            αρχίζοντας με λέξεις από 2 γράμματα, μετά από 3 κλπ.
            μέχρι να βρει την πρώτη αποδεκτή λέξη, οπότε σταματάει.
            Επιστρέφει exit code ίσο με 1 αν δεν υπάρχουν αρκετά γράμματα,
            αλλιώς δεν επιστρέφει τίποτα.

        max(self):
            Αυτός ο αλγόριθμος εξετάζει όλους τους συνδυασμούς των γραμμάτων 
            αρχίζοντας με λέξεις από 7 γράμματα, μετά από 6 κλπ.
            μέχρι να βρει την πρώτη αποδεκτή λέξη, οπότε σταματάει.
            Επιστρέφει exit code ίσο με 1 αν δεν υπάρχουν αρκετά γράμματα,
            αλλιώς δεν επιστρέφει τίποτα.  
        
        smart(self):
            Αυτός ο αλγόριθμος εμφανίζει την λέξη που δίνει τους περισσότερους
            πόντους/σκορ με βάση τα γράμματα του υπολογιστή.
            Επιστρέφει exit code ίσο με 1 αν χρειάζεται να τερματίσει το παιχνίδι.  
        
        smart_teach(self):
            Αυτός ο αλγόριθμος δέχεται την λέξη-απάντηση από τον παίκτη-άνθρωπο
            και ελέγχει αν έπαιξε την 1η ή 2η καλύτερη λέξη. Αν όχι, εμφανίζει τις
            δύο καλύτερες λέξεις (δηλαδή αυτές που δίνουν τους περισσότερους
            πόντους/σκορ).
            Στη συνέχεια παίζει ο υπολογιστής και βρίσκει την καλύτερη λέξη με
            βάση τα γράμματα του υπολογιστή.
            Επιστρέφει exit code ίσο με 1 αν χρειάζεται να τερματίσει το παιχνίδι.
        
        take_human_word(self, word: String):
            Καταχωρεί στην ιδιότητα human_word την 
            λέξη word που δίνεται σαν παράμετρος.

        take_human_letters(self, letters: list):
            Καταχωρεί στην ιδιότητα human_letters την 
            λίστα με γράμματα η οποία δίνεται σαν παράμετρος.

        find_two_best_words(self) -> list:
            Επιστρέφει μια λίστα με τις δύο λέξεις 
            με το μεγαλύτερο σκορ.


    # ΒΟΗΘΗΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ

    word_from_avail_letters(word, available_letters: list) -> boolean:
        Ελέγχει αν η λέξη word αποτελείται από τα διαθέσιμα 
        γράμματα. Αν ναι, επιστρέφει True, αλλιώς επιστρέφει False.

    word_in_dict(word):
        Ελέγχει αν η λέξη word βρίσκεται μέσα στο λεξικό με τις αποδεκτές λέξεις.

    create_available_letters_string(letters_of_player: String, letters_dict: dict) -> String:
        Επιστρέφει μια συμβολοσειρά που αποτελείται από τα διαθέσιμα 
        γράμματα (letters_of_player) μαζί με τους πόντους που προσφέρει το καθένα
        στην εξής μορφή:
        π.χ. A - 1, J - 4, 3 - 5, κλπ.

        Αν το letters_of_player είναι None, επιστρέφει None.
        Αν το letters_dict είναι None, επίσης επιστρέφει None.

    compute_word_score(word):
        Υπολογίζει το σκορ της λέξης word.    

    '''
    pass


# δημιούργησε ένα λεξικό με τις πληροφορίες των παιχνιδιών
info_dict = {}
import json
with open('game_info.json', 'w', encoding='utf-8') as f:
    json.dump(info_dict, f)

# διάβασε το αρχείο greek7.txt και αποθήκευσε τις λέξεις που 
# έχει στο λεξικό wdict
wdict = {}
with open('greek7.txt', 'r', encoding='utf-8') as f7:
    words = f7.readlines()
    for index, i in enumerate(words):
        wdict.update({i.strip('\n'): index})

# αποθήκευσε το wdict σε αρχείο .json
import json
with open('word_dict.json', 'w', encoding='utf-8') as f:
    json.dump(wdict, f)

# κάνε import το λεξικό με τις λέξεις από το αρχείο .json
with open('word_dict.json', 'r') as f:
    word_dict = json.load(f)

class SakClass:
    letters = {}

    def __init__(self):
        for letter in LETS:
            SakClass.letters.update({letter: LETS.get(letter)})
 
    @staticmethod
    def randomize_sak():
        letter_list = []
        for letter in SakClass.letters:
            pair = [letter, SakClass.letters.get(letter, "Exception: the letter does not exist in the dict")]
            letter_list.append(pair)

        # ανακάτευσε τη λίστα με τα γράμματα  
        random.shuffle(letter_list)

        # άδειασε το λεξικό και βάλε μέσα σ' αυτό τη νέα σειρά των γραμμάτων
        SakClass.letters = {}
        for pair in letter_list:
            SakClass.letters.update({pair[0]: pair[1]})

    @staticmethod
    def getletters(N: int):
        # δημιούργησε ένα αντίγραφο του λεξικού, έτσι ώστε σε περίπτωση 
        # αποτυχίας (όταν δηλαδή δεν υπάρχουν αρκετά γράμματα στο σακουλάκι)
        # τα γράμματα να μην αφαιρεθούν από το πραγματικό σακουλάκι
        temp_letter_dict = deepcopy(SakClass.letters)

        letters_to_return = []
        for i in range(N):
            # αν δεν υπάρχει άλλο γράμμα στο σακουλάκι
            let = SakClass.pop_letter(temp_letter_dict)
            if let is None:
                # βάλε πίσω τα γράμματα που βγάλαμε από το πραγματικό σακπυλάκι
                SakClass.putbackletters(letters_to_return)
                return None
            else:
                # αλλιώς (δηλαδή αν υπάρχει) βγάλε το γράμμα από το πραγματικό σακουλάκι
                let = SakClass.pop_letter(SakClass.letters)
                letters_to_return.append(let)
                SakClass.randomize_sak()
        return letters_to_return

    @staticmethod
    def putbackletters(letters:list):
        if (letters is None) or (letters == []):            
            return
        
        if SakClass.letters is None:            
            return

        # για κάθε γράμμα της δοσμένης λίστας,
        # βρες το μέσα στο λεξικό letters και αύξησε το πλήθος του (amount)
        for let in letters:
            amount = SakClass.letters.get(let, 'Exception: the letter does not exist in the dict')[0]
            if isinstance(amount, int):
                SakClass.letters.update({let: [amount + 1, SakClass.letters.get(let)[1]]})
            else:
                return
        return

    @staticmethod
    def pop_letter(letters_dict: dict):
        # όσο το γράμμα δεν υπάρχει (δηλαδή amount = 0)
        # και είμαστε μέσα στα όρια του λεξικού,
        # πήγαινε στο "επόμενο" γράμμα του σάκου
        i = 0
        while letters_dict.get(list(letters_dict.keys())[i])[0] <= 0 and i < len(letters_dict) - 1:
            i += 1

        if letters_dict.get(list(letters_dict.keys())[i])[0] > 0 and i < len(letters_dict):
            # βρέθηκε ένα γράμμα
            # πάρε ένα γράμμα (χρησιμοποιούμε τη συνάρτηση list() ώστε να έχουμε πρόσβαση)
            letter = list(letters_dict.keys())[i]
            # και μείωσε το πλήθος του (amount)
            letters_dict[list(letters_dict.keys())[i]][0] -= 1
            return letter
        else:
            print('Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι.')
            return None


class Game:
    game_index = 0

    def __init__(self):
        self.sak = SakClass()
        self.ph = Human()
        self.pc = Computer()
        self.current_player = None
        self.computer_algorithm = 1 # ο MIN είναι default

    def __repr__(self):
        return f'Class: {self.__class__}, player_human: {self.ph}, player_computer: {self.pc}, current_player: {self.current_player}, computer_algorithm_number: {self.computer_algorithm}'

    def setup(self):
        print()
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
                # εμφάνισε τον πίνακα σκορ
                self.show_score_option()
                break
            elif ans == '2':
                # εμφάνισε τις ρυθμίσεις
                self.show_settings()
                break
            elif ans == '3':
                # ξεκίνα το παίχνίδι Scrabble
                self.run()
                break
            elif ans == 'q':
                # έξοδος
                print('ΕΞΟΔΟΣ')
                exit()
                break

            print('Επίλεξε ξανά: ')
            
    def run(self):
        print()
        print('ΠΑΙΧΝΙΔΙ')
        print()

        # επειδή το σακουλάκι έχει αλλάξει από το προηγούμνο παιχνίδι,
        # γέμισε το πάλι παίρνοντας γράμματα από
        # το λεξικό LETS
        for letter in LETS:        
            SakClass.letters.update({letter: [LETS.get(letter)[0], LETS.get(letter)[1]]})

        # ανακάτεψε το σακουλάκι
        SakClass.randomize_sak()

        # παίζει πρώτα ο παίκτης-άνθρωπος
        self.current_player = self.ph

        # μηδένισε τα σκορ των παικτών
        self.ph.score = 0
        self.pc.score = 0

        # εμφανίζουμε πόσα γράμματα είναι στην αρχή στο σακουλάκι 
        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
        print("Μοιράζουμε από 7 γράμματα σε κάθε παίκτη.")
        print()

        # κληρώνουμε για τους παίκτες 7 γράμματα για την πρώτη φορά που παίζουν
        self.ph.letters = SakClass.getletters(7)
        self.pc.letters = SakClass.getletters(7)

        while True:
            if self.current_player == self.ph:
                # παίζει ο άνθρωπος
                if create_available_letters_string(self.ph.letters, self.sak.letters) is None:
                    self.end()

                # αλλιώς    
                # δημιούργησε την συμβολοσειρά με τα διαθέσιμα γράμματα (Κ,3 - Ε,3 - κλπ.)
                avail_let_string = create_available_letters_string(self.ph.letters, self.sak.letters)
                print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
                print(f'Διαθέσιμα γράμματα: {avail_let_string}')
                self.ph.play()
                word = input('ΛΕΞΗ: ')

                # smart-teach
                if self.computer_algorithm == 4:
                    self.pc.take_human_word(word)
                    temp_lets = self.ph.letters
                    self.pc.take_human_letters(temp_lets)                    

                # αν ο παίκτης θέλει να σταματήσει το παιχνίδι
                if word == 'q':                    
                    self.end()

                # έλεγχος αν η λέξη αποτελείται από γράμματα 
                # που όντως διαθέτει ο παίκτης
                while not word_from_avail_letters(word, self.ph.letters):                    
                    if word == 'p':
                        # όταν ο χρήστης δώσει 'p', τότε του κληρώνονται νέα γράμματα (εφόσον υπάρχουν),
                        # μετά επιστρέφονται τα προηγούμενα γράμματά του στο «σακουλάκι»

                        human_letters = SakClass.getletters(7)
                        if human_letters is None:
                            # αν δεν υπάρχουν 7 γράμματα μέσα στο σακουλάκι
                            # τότε τερμάτισε το παιχνίδι
                            self.end()
                        else:
                            letters_to_put_back = self.ph.letters
                            self.ph.letters = human_letters
                            SakClass.putbackletters(letters_to_put_back)

                        # και ο χρήστης χάνει την σειρά του
                        print('=============================================================')
                        self.current_player = self.pc
                        break

                    print('Η λέξη δεν αποτελείται από τα διαθέσιμα γράμματα.')
                    word = input('ΛΕΞΗ: ')

                    # αν ο παίκτης θέλει να σταματήσει το παιχνίδι
                    if word == 'q':
                        print('=============================================================')
                        self.end()
                
                if self.current_player == self.pc:
                    continue

                # έλεγχος αν η λέξη που δόθηκε περιλαμβάνεται 
                # στον κατάλογο αποδεκτών λέξεων
                if word != 'p':
                    if word_in_dict(word):
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
                        print('=============================================================')

                        # αν ο παίκτης θέλει να σταματήσει το παιχνίδι
                        if word == 'q':
                            print('=============================================================')
                            self.end()

                        if inp == '':
                            # βγάζουμε τα γράμματα που χρησιμοποιήθηκαν                            
                            for let in used_letters:
                                self.ph.letters.remove(let)
                            
                            # αν το σακουλάκι δεν έχει τα γράμματα που χρειαζόμαστε
                            # τότε τερματίζει το παιχνίδι
                            human_letters = SakClass.getletters(len(used_letters))
                            if human_letters is None:
                                self.end()
                            else:                        
                                # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι
                                # (τόσα όσα βγάλαμε)      
                                for let in human_letters:
                                    self.ph.letters.append(let)
                        
                            self.current_player = self.pc
                            continue
                    else:
                        print('Μη αποδεκτή λέξη')
                        print('=============================================================')
                        self.current_player = self.pc
                        continue
                else:
                    # αν word == 'p'
                    # αν το σακουλάκι δεν έχει τα γράμματα που χρειαζόμαστε

                    human_letters = SakClass.getletters(7)
                    if human_letters is None:
                        pass
                    else:            
                        letters_to_put_back = self.ph.letters
                        self.ph.letters = human_letters
                        SakClass.putbackletters(letters_to_put_back)
                    
                    print('=============================================================')
                    # τότε είναι η σειρά του υπολογιστή
                    self.current_player = self.pc
                    continue

            else:
                # πάιζει ο υπολογιστής
                exit_code = self.pc.play(self.computer_algorithm)
                print('=============================================================')
                # αν ο αλγόριθμος του υπολογιστή επιστρέφει exit code 1,
                # τότε τερμάτισε το παιχνίδι
                if exit_code == 1:
                    self.end()

                self.current_player = self.ph
                continue

    def end(self):
        print('=============================================================')
        print('ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ')
        print()
        # εμφάνισε τις πληροφορίες του παιχνιδιού που μόλις τελείωσε (Νικητής, Σκορ κλπ.)
        print('Το σκορ σου: ', self.ph.score)
        print('Η/Υ - Σκορ: ', self.pc.score)
        print(f'Νικητής: {self.get_winner()}')

        # αύξησε τον αριθμό του παιχνιδιού κατά 1 
        Game.game_index += 1
        # αποθήκευσε τις πληροφορίες του παιχνιδιού σε αρχείο .json
        info_dict.update({Game.game_index: ['Άνθρωπος', self.ph.score, 'Η/Υ', self.pc.score]})
        with open('game_info.json', 'w', encoding='utf-8') as f:
            json.dump(info_dict, f) 

        # εμφάνισε το αρχικό μενού
        self.setup()

    def show_score_option(self):
        with open('game_info.json', 'r') as f:
            game_info = json.load(f)

        print()
        print('ΣΚΟΡ')
        print()
        for element in game_info:
            print(f'Παιχνίδι Νο {element}: {game_info.get(element)[0]} - {game_info.get(element)[1]}, {game_info.get(element)[2]} - {game_info.get(element)[3]}')

        print('--------------------')

        while True:
            ans = input('Επίλεξε q για έξοδο από τον Πίνακα Σκορ: ')
            if ans == 'q':               
                self.setup()


    def show_settings(self):
        print()
        print('ΡΥΘΜΙΣΕΙΣ')
        print()
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
                print('Εξοδος από Ρυθμίσεις')
                self.setup()
                break
            else:
                print('Μη έγκυρη επιλογή.')

            print('Επίλεξε ξανά: ')
    
    def get_number_of_letters_in_sak() -> int:
        count = 0        
        for let in SakClass.letters:
            count += int(SakClass.letters.get(let)[0])
        return count

    def get_winner(self):
        if self.ph.score > self.pc.score:
            return 'Εσύ'
        elif self.ph.score < self.pc.score:
            return 'Η/Υ'
        else:
            return 'Ισοπαλία'

class Player():
    def __init__(self):
        self.score = 0
        self.letters = []

    def __repr__(self):
        return f'Class: {self.__class__}, score: {self.score}, letters: {self.letters}'

class Human(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Class: {self.__class__}, score: {self.score}, letters: {self.letters}'

    def play(self):
        print('Παίζεις:')


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.human_word = ""
        self.human_letters = ""

    def __repr__(self):
        return f'Class: {self.__class__}, score: {self.score}, letters: {self.letters}, human_word: {self.human_word}, human_letters: {self.human_letters}'
    
    def play(self, algorithm_number: int):
        print('Παίζει ο Η/Υ:')
        if create_available_letters_string(self.letters, SakClass.letters) is None:
            self.end()
        # αλλιώς    
        # δημμιούργησε την συμβολοσειρά με τα διαθέσιμα γράμματα (Κ,3 - Ε,3 - κλπ.)
        avail_let_string = create_available_letters_string(self.letters, SakClass.letters)

        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')
        print(f'Γράμματα Η/Υ: {avail_let_string}')

        if algorithm_number == 1:
            # παίξε τον MIN
            exit_code = self.min()
            if exit_code == 1:
                return 1
        elif algorithm_number == 2:
            # παίξε τον MAX
            exit_code = self.max()
            if exit_code == 1:
                return 1
        elif algorithm_number == 3:
            # παίξε τον SMART
            exit_code = self.smart()
            if exit_code == 1:
                return 1
        elif algorithm_number == 4:
            # παίξε τον SMART-TEACH
            exit_code = self.smart_teach()
            if exit_code == 1:
                return 1
        else:
            print('Error: Invalid algorithm_number')
    
    def min(self):
        for i in range(2, len(self.letters) + 1):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:                    
                    word = word + let                

                if word_in_dict(word):                    
                    # αποθήκευσε τα γράμματα που χρησιμοποιήθηκαν
                    used_letters = []
                    for let in word:
                        used_letters.append(let)

                    # παίξε τη λέξη
                    word_score = compute_word_score(word)
                    self.score += word_score
                    print(f'Λέξη Η/Υ: {word} - Βαθμοί: {word_score} - Σκορ Η/Υ: {self.score}')

                    for let in used_letters:
                        self.letters.remove(let)
                    
                    # αν το σακουλάκι δεν έχει τον απαιτούμενο αριθμό γραμμάτων        
                    # τότε το παιχνίδι τερματίζει
                    computer_letters = SakClass.getletters(len(used_letters))
                    if computer_letters is None:                        
                        return 1    # end-the-game code 
                    else:
                        # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)                                                    
                        for let in computer_letters:
                            self.letters.append(let)
                    return

        # δεν βρέθηκε κάποια αποδεκτή λέξη
        print('Δεν βρέθηκε κάποια αποδεκτή λέξη.')
        print('Ο Η/Υ παίζει pass.')

        # ο Η/Υ πάιζει pass και χάνει την σειρά του
        lets = SakClass.getletters(7)
        if lets is None:
            pass
        else:            
            letters_to_put_back = self.letters
            self.letters = lets
            SakClass.putbackletters(letters_to_put_back)
        return

    def max(self):
        for i in range(len(self.letters), 1, -1):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:
                    word = word + let

                if word_in_dict(word):
                    # αποθήκευσε τα γράμματα που χρησιμοποιήθηκαν
                    used_letters = []
                    for let in word:
                        used_letters.append(let)

                    # πάιξε την λέξη
                    word_score = compute_word_score(word)
                    self.score += word_score
                    print(f'Λέξη Η/Υ: {word} - Βαθμοί: {word_score} - Σκορ Η/Υ: {self.score}')

                    for let in used_letters:
                        self.letters.remove(let)
                    
                    # αν το σακουλάκι δεν έχει τον απαιτούμενο αριθμό γραμμάτων        
                    # τότε το παιχνίδι τερματίζει
                    lets = SakClass.getletters(len(used_letters))
                    if lets is None:
                        return 1    # end-the-game code 
                    else:
                        # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)                                                  
                        for let in lets:
                            self.letters.append(let)
                    return

        # δεν βρέθηκε κάποια αποδεκτή λέξη
        # παίξε pass
        lets = SakClass.getletters(7)

        # αν το σακουλάκι δεν έχει τον απαιτούμενο αριθμό γραμμάτων
        # τότε ο Η/Υ χάνει την σειρά του
        if lets is None:
            pass
        else:            
            letters_to_put_back = self.letters
            self.letters = lets
            SakClass.putbackletters(letters_to_put_back)   
        return

    def smart(self):
        accepted_words = {}
        for i in range(2, len(self.letters) + 1):
            for perm in itertools.permutations(self.letters, i):
                word = ''
                for let in perm:            
                    word = word + let                

                if word_in_dict(word):                
                    word_score = compute_word_score(word)
                    # αποθήκευσε τη λέξη με το σκορ της στο λεξικό
                    accepted_words.update({word: word_score})
                    
        if len(accepted_words) != 0: 
            # το λεξικό δεν είναι άδειο
            # βρες την λέξη με το μέγιστο σκορ
            max_score = 0
            for w in accepted_words.keys():
                temp_score = compute_word_score(w)               
                if temp_score > max_score:
                    max_score = temp_score
                    word_with_max_score = w

            # πάιξε την λέξη          
            self.score += max_score
            print(f'Λέξη Η/Υ: {word_with_max_score} - Βαθμοί: {max_score} - Σκορ Η/Υ: {self.score}')

            # αποθήκευση των γραμμάτων που χρησιμοποιήθηκαν
            used_letters = []
            for let in word_with_max_score:
                used_letters.append(let)
           
            for let in used_letters:
                self.letters.remove(let)
            
            # αν το σακουλάκι δεν έχει τον απαιτούμενο αριθμό γραμμάτων        
            # τότε το παιχνίδι τερματίζει
            lets = SakClass.getletters(len(used_letters))
            if lets is None:
                return 1    # end-the-game code 
            else:
                # και συμπληρώνουμε με νέα γράμματα από το σακουλάκι (τόσα όσα βγάλαμε)                            
                for let in lets:
                    self.letters.append(let)
        else:
            # το λεξικό είναι άδειο, δηλαδή δεν βρέθηκε κάποια αποδεκτή λέξη
            print('Δεν βρέθηκε κάποια αποδεκτή λέξη.')

            # παίξε pass
            lets = SakClass.getletters(7)

            # αν το σακουλάκι δεν έχει τον απαιτούμενο αριθμό γραμμάτων
            # τότε το παιχνίδι τερματίζει 
            if lets is None:
                return 1   # return exit code 1 = end-of-game
            else:            
                letters_to_put_back = self.letters
                self.letters = lets
                SakClass.putbackletters(letters_to_put_back)
            
        return

    def smart_teach(self):   
        # παίζει ο άνθρωπος
        two_best_words = self.find_two_best_words()
        # αν υπάρχει αποδεκτή λέξη
        if two_best_words is not None:           
            if self.human_word == two_best_words[0]:
                print('Συγχαρητήρια! Έπαιξες την καλύτερη δυνατή λέξη!')
                print()
            elif self.human_word == two_best_words[1]:
                print('Συγχαρητήρια! Έπαιξες την 2η καλύτερη δυνατή λέξη!')
                print('Θα μπορούσες να παίξεις και την εξής:')
                print(f'{two_best_words[0]}')
                print()
            else:
                print('Θα μπορούσες να παίξεις τις εξής:')
                print(f'1η καλύτερη: {two_best_words[0]}')
                print(f'2η καλύτερη: {two_best_words[1]}')
                print()
        else:
            # αν δεν υπάρχει αποδεκτή λέξη
            print('Δεν υπάρχει αποδεκτή λέξη με τα γράμματά σου.')
            print()
        
        # παίζει ο υπολογιστής
        print(f'Στο σακουλάκι: {Game.get_number_of_letters_in_sak()} γράμματα')   
        self.smart()

    def take_human_word(self, word: String):
        self.human_word = word        

    def take_human_letters(self, letters: list):
        self.human_letters = ''.join(map(str, letters))

    def find_two_best_words(self) -> list:
        # δημιουργούμε λεξικό με όλες τις αποδεκτές λέξεις
        accepted_words = {}
        for i in range(2, len(self.human_letters) + 1):
            for perm in itertools.permutations(self.human_letters, i):
                word = ''
                for let in perm:
                    word = word + let

                if word_in_dict(word):
                    word_score = compute_word_score(word)
                    # αποθήκευσε τη λέξη με το σκορ της στο λεξικό
                    accepted_words.update({word: word_score})

        # βρίσκουμε τις δύο καλύτερες λέξεις
        if len(accepted_words) != 0: 
            # το λεξικό δεν είναι άδειο
            # βρες την λέξη με το μέγιστο σκορ
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
                elif temp_score > max_score2:
                    max_score2 = temp_score
                    word_with_max_score2 = w

            # παίξε την λέξη
            best_word = word_with_max_score1
            second_best_word = word_with_max_score2
        else:
            # το λεξικό είναι άδειο, δηλαδή δεν βρέθηκε κάποια αποδεκτή λέξη
            # παίξε pass
            return None

        return [best_word, second_best_word]


# ΒΟΗΘΗΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ

def word_from_avail_letters(word, available_letters: list) -> boolean:
    # δημιούργησε ένα αντίγραφο της λίστας available_letters,
    # αλλιώς θα αλλάξει η λίστα και θα χάσουμε τα γράμματα σε
    # μελλοντική χρήση
    available_letters_copy = []
    for x in available_letters:
        available_letters_copy.append(x)

    for let in word:
        if let not in available_letters_copy:
            return False
        available_letters_copy.remove(let)
    return True

def word_in_dict(word):
    if word in word_dict:
        return True
    return False

def create_available_letters_string(letters_of_player: String, letters_dict: dict) -> String:
    if letters_of_player is None:
        return None
    
    if letters_dict is None:
        return None

    avail_let_string = ''
    i = 1
    for let in letters_of_player:
        if let is None:
            continue
        avail_let_string += f'{let},{letters_dict.get(let, "Exception: the letter does not exist in the dict")[1]}'
        if i < len(letters_of_player):
            avail_let_string += ' - '
        i += 1
    
    return avail_let_string

def compute_word_score(word):
    score = 0
    for let in word:
        score += SakClass.letters.get(let)[1]
    return score