from random import choice

first_names = [
    "Bingo", "Chunky", "Fuzzy", "Scooter", "Wobbles", "Fluffy", "Boinky", "Snickers", "Goober", "Pickles",
    "Zippy", "Sprinkles", "Muffin", "Doodles", "Jazz", "Skippy", "Cheesy", "Bubba", "Twiggy", "Sparky",
    "Booger", "Snuffy", "Squishy", "Jumpy", "Whiskers", "Nacho", "Crumbs", "Banjo", "Spud", "Waffles",
    "Mana",
]

last_names = [
    "McSnort", "Wobblebottom", "O'Toole", "Bananahammock", "Von Dinkle", "Fizzlebottom", "Snugglepuff",
    "Fiddlefaddle", "McFluffernutter", "Gloopersnoop", "Twiddlywink", "Froghopper", "Gigglepants",
    "Puddingworth", "Jigglesby", "Snufflekins", "Pickleberry", "Bumblebutton", "Wagglesworth",
    "Wigglesnort", "McJingles", "Flufferdoodle", "Bumblesnatch", "Wafflestomp", "Gigglesniff",
    "Squishmire", "Wobblesnatch", "Crumblybum", "Floppinstock", "Sprinkletoes", "Muffincheeks",
    "Manushyan",
]

while True:
    first_name = choice(first_names)
    last_name = choice(last_names)

    print(f"\n{first_name} {last_name}\n")

    run_again = input("\nDo you want to generate another name? (Press y/n): ").lower()
    if run_again == 'n':
        print("\nHave a nice day!")
        break
