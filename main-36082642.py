import classes

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

sak = classes.SakClass(letters_weight, letters_amount)
# print("letters_amount = ", letters_amount)

human = classes.Human()
computer = classes.Computer()
game = classes.Game(sak, human, computer)

game.setup()

