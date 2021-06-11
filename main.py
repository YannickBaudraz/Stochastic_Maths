import locale
import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# region Functions


def get_capital() -> int:
    """
    Convert the input from user to a capital
    :return: The capital converted or 10 if cannot convert the input.
    """
    try:
        user_input = input('Entrez votre capital de départ (nombre entier) : ')
        return int(user_input)
    except ValueError:
        return 10


def get_win_probability() -> float:
    """
    Convert the input from user to a probability of win.
    :return: The probability of win converted or 0.5 if cannot convert the input.
    """
    try:
        user_input = input('Entrez votre probabilité "p" de gagner '
                           '(0.5 = 50% de chance de gagner, utilisez des points comme virgule) '
                           ': ')
        return float(user_input)
    except ValueError:
        return 0.5


def get_trials_number() -> int:
    """
    Convert the input from user to a maximum number of trials.
    :return: The maximum number of trials converted or 50 if cannot convert the input.
    """
    try:
        user_input = input('Entrez le nombre d\'essai maximum : ')
        return int(user_input)
    except ValueError:
        return 50


def round05(number) -> float:
    """
    Round a number to x.05
    :param number: The number to round.
    :return: The rounded number.
    """
    return round(number * 20) / 20


# endregion

# region Variables

# Get user input and stock into variables
capital: int = get_capital()
win_probability: float = get_win_probability()
trials_number: int = get_trials_number()

min_capital_possible: float = 0.05

# Add the start capital to an array that will contain all capitals variations in the program
capital_variations: list[int] = [capital]

# endregion

# region Stochastic process

for i in range(trials_number - 1):
    if capital < 0.05:
        break

    rand: int = random.randrange(100)
    returned: float = capital * win_probability

    if rand / 100 < win_probability:
        capital += returned
    else:
        capital -= returned

    capital_variations.append(capital)

capital = 0 if capital < 0.05 else capital

# endregion

# region Displays

print(capital_variations)

plt.plot(np.arange(0, len(capital_variations)), np.array(capital_variations))

# Format to currency
locale.setlocale(locale.LC_ALL, '')
start_capital = locale.currency(capital_variations[0], grouping=True)
actual_capital = locale.currency(round05(capital), grouping=True)
max_money = locale.currency(round05(np.max(capital_variations)), grouping=True)

plt.title(f'Mise de départ : {start_capital}\n'
          f'Probabilité de chance de gagner {win_probability * 100}%\n'
          f'Votre capital est maintenant de {actual_capital}\n'
          f'Votre capital a réussi à atteindre {max_money}')
plt.ylabel('Gains en CHF')
plt.xlabel('Jeu n°')

# To not use scientific notation when big number
plt.ticklabel_format(style="plain")
# To not cut of labels of Y axis when big number
plt.gcf().subplots_adjust(left=0.2, top=0.8)
# Display Y axis with thousands separator
plt.gca().yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()

# endregion
