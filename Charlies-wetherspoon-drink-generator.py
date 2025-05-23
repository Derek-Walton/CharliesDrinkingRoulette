from random import choice
from os import system as os_system
from platform import system as platform_system

SPACE = ' '
MAX_CATEGORY_LENGTH: int = len("Pre-mixed drinks")

DRINKS = {
    "Beer (draught)": [
        "1664 Biere", "Poretti", "Bud Light", "Carlsberg", "Carling", "Coors",
        "Budweiser", "Corona Extra", "Stella Artois", "Leffe Blonde",
        "Worthington's Creamflow", "Guinness"
    ],
    "Beer (craft)": [
        "Shipyard", "Brewdog Punk IPA", "Wold Beer Everstone",
        "Burning Sky Arise", "Siren Flex", "Camden Pale Ale", "Camden Hells",
        "BrewDog Elvis Juice", "BrewDog Hazy Jane"
    ],
    "Beer (bottle)": [
        "Madri", "Budweiser", "Corona Extra", "Modelo Especial", "Pacifico",
        "Estrella Garcia", "Desperados", "Birra Moretti",
        "Newcastle Brown Ale", "Asahi", "Efes", "Heineken", "Peroni",
        "Strapramen", "Stella Artois Unfiltered", "Tyskie Gronie", "Tyskie",
        "Erdinger", "Beck's", "Sol"
    ],
    "Real Ale": [
        "Doom Bar", "Green King Abbot Ale", "Bowman Meon Valley Bitter",
        "Bowman Wollops Wood", "Bowman Black Drop", "Ramsgate Godds' No. 3"
    ],  # Might need to make ones that change often more dynamic
    "Cider": [
        "Stowford Press Apple Cider", "Strongbow", "Strongbow Dark Fruits",
        "Bulmers Original", "Angry Orchard", "Aspall Cyder",
        "Bulmers Crushed Red Berries & Lime", "Kopparberg Mixed Fruit",
        "Kopparberg Light Passionfruit", "Kopparberg Strawberry & Lime",
        "Kopparberg Sweet Vintage Pear", "Thatchers Blood Orange"
    ],
    "Pre-mixed drinks": ["Hooch", "WKD Blue", "Smirnoff Ice"],
    "Wine": [
        "Coldwater Creek Chardonnay", "Coldwater Creek Pino Grigio",
        "Willa Maria Private Bin Sauvingnon Blanc", "Bolla Pino Grigio",
        "Cune White Rioja", "Coldwater Creek Merlot", "Zana Pinot Noir",
        "Trivento Malbec", "Grant Burge Barossa Ink Shiraz",
        "Gallo Family Vineyards White Zinfandel", "Coldwater Creek Rose",
        "The Pale", "Villa Maria Blush Sauvingon", "Bolla Pino Grigio Blush",
        "Teresa Rizzi Procecco", "Broadwoods Folly", "Teresa Rizzi Prosecco",
        "Teresa Rizzi Sparkling Rose"
    ],
    "Cocktails": [
        "Purple Rain", "Strawberry Porn Star Martini", "Sex on the Beach",
        "Candy Rosa", "Porn Star Martini", "Blue Lagoon", "Mango Monster Mash",
        "Woo Woo", "Tropical Smash", "Bumbu Colada", "Hawaiian Pipeline Punch",
        "Zombie", "The Godfather", "Classic Pimm's", "Amaretto Sour", "Paloma",
        "Mango Picante", "Strawberry Daiquiri", "Espresso Martini",
        "Tommy's Margarita", "Hugo Spritz", "Mango & Passionfruit Spritz",
        "Classic Aperol Spritz", "Peach Blush Spritz", "Limoncello Spritz"
    ],
    "Vodka": [
        "Smirnoff", "Smirnoff Mango & Passionfruit Twist",
        "Smirnoff Raspberry Crush", "XIX Gumball Orange",
        "XIX Vodka Mixed Berry", "XIX Vodka Tropical Ice",
        "Au Vodka Bubblegum", "Au Vodka Blue Raspberry",
        "Au Vodka Black Grape", "Au Vodka Pineapple Crush",
        "Au Vodka Pink Lemonade", "Au Vodka Strawberry Burst",
        "Flavar Blueberry & Lemon", "Flavar Salted Caramel",
        "Flavar Strawberry & Lime", "Absolut Vanilla", "Absolut", "Grey Goose"
    ],
    "Gin": [
        "Beefeater London Blood Orange", "Hendrick's Gin", "Bombay Sapphire",
        "Gordon's", "Tanqueray No. Ten",
        "Edinburgh Gin Rhubarb & Ginger Liqueur", "GinTing Passionfruit",
        "Gordon's Pink", "Whitley Neil Rasberry Gin",
        "Zymurgorium Realm of the Unicorn Gin Liqueur",
        "Zymurgorium Sweet Violet Gin Liqueur"
    ],
    "Rum": [
        "The Kraken Black Spiced Rum Black Cherry & Madagascan Vanilla",
        "Dead Man's Finger Pineapple Rum",
        "Captain Morgan Original Spiced Gold", "Captain Morgan Tiki",
        "Captain Morgan White", "Malibu", "The Kraken Black Spiced Rum",
        "Bacardi Carta Blanca", "Bumbu"
    ],
    "Whiskey": [
        "Bell's", "The Famouse Grouse", "Jameson", "Jack Daniels", "Jim Beam",
        "Glenfiddich 12-year-old"
    ],
    "Tequila":
    ["El Sueno NODA Pineapple Tequila", "Jose Cuervo Especial Silver"],
    "Liqueurs": [
        "Disaronno Amaretto", "Southern Comfort", "Strika", "Kahlua",
        "Cambord Black Raspberry Liqueur", "Jack Daniel's Tennessee Apple",
        "Sheep Dog Penut Butter Whiskey", "Fireball Cinnamon Whisky",
        "Archers Peach Schnapps", "Baileys", "Tia Maria",
        "Courvoisier VS Congnac", "E & J"
    ],
    "Shots and Bombs": [
        "Baby Guiness", "Strawberries and Cream", "Jammy Dodger", "Strikabomb",
        "Flavarbomb", "SoCoLocobomb", "Skittlebomb", "Raspberrybomb"
        "Fireballbomb", "Smirnoff Vodka and Monster",
        "Jose Cuervo Especial Silver", "Tequilla Rose", "Limoncello",
        "Pontoon Spicy Mango", "Antica Sambuca", "Antica Sambuca Raspberry",
        "Antica Sambuca Black", "Mozart White Chocolate Cream Liqueur",
        "SOURZ Apple", "SOURZ Cherry", "CORKY'S Blueberry", "CORKY's Mango",
        "CORKY'S Sour Apple", "CORKY'S Sour Cherry"
    ]
}

CATEGORY_CODES = {
    'bed': 'Beer (draught)',
    'bec': 'Beer (craft)',
    'beb': 'Beer (bottle)',
    'rea': 'Real Ale',
    'cid': 'Cider',
    'pmd': 'Pre-mixed drinks',
    'win': 'Wine',
    'coc': 'Cocktails',
    'vod': 'Vodka',
    'gin': 'Gin',
    'rum': 'Rum',
    'wis': 'Whiskey',
    'teq': 'Tequila',
    'liq': 'Liqueurs',
    'snb': 'Shots and Bombs'
}

MIXER_CATEGORIES = ["Vodka", "Gin", "Rum", "Whisky", "Tequila", "Liqueurs"]

MIXERS = [
    "No mixer", "Britvic tonic", "Britvic diet tonic",
    "Britvic elderflower tonic", "Pepsi Max cherry", "Pepsi Max", "Pepsi",
    "Diet Pepsi", "R White's lemonade", "R White's raspberry lemonade",
    "Lemonade & lime", "Sanpellegrino lemon", "Sanpellegrino blood orange",
    "Apple juice", "Cranberry Juice", "Orange Juice", "Soda water",
    "Soda & lime", "Lime Cordial", "Blackcurrent cordial", "Orange cordial",
    "Britvic ginger ale", "Britvic bitter lemon", "Britvic pineapple juice",
    "Monster Energy Ultra Peachy Keen", "Monster Mango Loco",
    "Monster Pipeline Punch", "Monster Energy", "Monster Energy Ultra",
    "Monster Energy Ultra Rosa", "Old Jamaica ginger beer",
    "Remedy kombucha raspberry lemonade", "Irn Bru", "Irn Bru Diet",
    "Pineapple Juice", "Dash Lemonade & Black", "Soda & Black",
    "Grapefruit Juice", "San Pellegrino Grapefruit", "San Pellegrino Orange",
    "Dash Pepsi Cherry Max", "Dash Pepsi Max", "Dash Diet Pepsi", "Dash Pepsi",
    "Dash Lime Cordial", "Dash Blackcurrent Cordial", "Ginger Beer",
    "Dash Orange Cordial"
]


def display_start_message() -> None:
    os_system('cls' if platform_system() == 'Windows' else 'clear')
    print("🍺🍺🍺 Welcome to the Wetherspoons Random Drink Picker App! 🍺🍺🍺\n")
    print(
        "Please note that this is not 100% accurate because spoons change their menu often"
    )
    print("If your choice is impossible, just roll again. \n\n\n\n")
    print(
        "Enter to pick a drink or enter a command ('q' to quit) ('s' for settings):"
    )


def main() -> None:
    display_start_message()
    while True:
        inp: str = input()
        match inp:
            case 'q':
                quit()
            case 's':
                run_settings()
                display_start_message()
            case _:
                display_drink(select_random_drink())


def display_drink(drink: str) -> None:
    category = derive_drink_category(drink)
    gap_size = MAX_CATEGORY_LENGTH - len(category) + 2
    print(
        f"{category} -> {SPACE * gap_size} {drink} {f'   (mixer: {choice(MIXERS)})'if category in MIXER_CATEGORIES else ''}"
    )


def select_random_drink() -> str:
    valid_drinks = generate_valid_drinks()
    drink: str = choice(valid_drinks)
    return drink


def generate_valid_drinks() -> list[str]:
    valid_drinks = []
    for key in valid_categories:
        valid_drinks += DRINKS[key]
    return valid_drinks


def derive_drink_category(drink: str) -> str:
    for key, value in DRINKS.items():
        if drink in value:
            return key
    return "ERROR"


def run_settings() -> None:
    while True:
        os_system('clear')
        os_system('cls' if platform_system() == 'Windows' else 'clear')
        display_categories_table()
        inp: str = input("\nToggle category with code or q to quit: ")

        if inp == 'q':
            return
        try:
            valid_categories.remove(CATEGORY_CODES[inp])
        except Exception as e:
            print(f"Error: '{inp}' is not a valid code.")


def toggle_category(category: str) -> None:
    if category in valid_categories:
        valid_categories.remove(category)
    else:
        valid_categories.append(category)


def display_categories_table() -> None:
    for code, cat in CATEGORY_CODES.items():
        gap_size = MAX_CATEGORY_LENGTH - len(cat)
        print(
            f"{cat} {SPACE * gap_size} : ['{code}'] - {('O' if platform_system() == 'Windows' else '✔️') if cat in valid_categories else ('X' if platform_system() == 'Windows' else '❌')}"
        )


if __name__ == '__main__':
    valid_categories = list(DRINKS.keys())
    main()
