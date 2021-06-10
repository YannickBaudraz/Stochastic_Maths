import locale
import random

import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np


# region Functions


def get_capital_input() -> int:
    try:
        user_input = input("Entrez votre capital (nombre entier) : ")
        return int(user_input)
    except ValueError:
        return 10


def get_probability_win_input() -> float:
    try:
        user_input = input(
            'Entrez votre probabilité "p" de gagner ' +
            '(0.5 = 50% de chance de gagner, utilisez des points comme virgule ' +
            ': ')
        return float(user_input)
    except ValueError:
        return 0.5


def get_trials_number_input() -> int:
    try:
        user_input = input('Entrez votre nombre d\'essais maximum : ')
        return int(user_input)
    except ValueError:
        return 50


def round05(number):
    return round(number * 20 / 20)


# endregion

# region Variables

capital = get_capital_input()
probability_win = get_probability_win_input()
trials_number = get_trials_number_input()
moneys = [capital]

i = 0

# endregion

# region Process stochastic

while 0.05 < capital and i < trials_number:
    i += 1
    rand = random.randrange(100)
    returned = capital * probability_win

    if probability_win >= rand / 100:
        capital += returned
    else:
        capital -= returned

    moneys.append(capital)

# endregion

# region Displays

locale.setlocale(locale.LC_ALL, '')
capital_formatted = locale.currency(round05(capital), grouping=True)
max_money_formatted = locale.currency(round05(np.max(moneys)), grouping=True)

print(moneys)
plt.plot(0, len(moneys), moneys, color="blue")
plt.title(
    f'Votre capital est maintenant de {capital_formatted}\n'
    f'et votre maximum a été de {max_money_formatted}'
)
plt.ylabel('Gains en CHF')
plt.xlabel('Jeu n°')
plt.ticklabel_format(style="plain")
plt.gcf().subplots_adjust(left=0.25)
plt.gca().yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.show()

# endregion
