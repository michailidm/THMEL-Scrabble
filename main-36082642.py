import classes

letters = {
    # a dict like this: 
    # letter: [cost, frequency]

    "Α":[1, 13],
    "Β":[3, 9],
    "Γ":[12, 11],
    "Δ":[5, 14]
}

sak = classes.SakClass(letters)
game = classes.Game(sak)
game.setup()


