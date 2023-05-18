import random


def draw_cards(deck, num_cards):
    return random.sample(deck, num_cards)


def calculate_probability(cards, deck_size):
    return 1 / (deck_size * (deck_size - 1) * (deck_size - 2))


def calculate_probabilities(deck):
    deck_size = len(deck)
    # а) Независимо от порядка извлечения карт без возвращения
    probability_a = calculate_probability(deck, deck_size)
    # б) В указанном порядке при извлечении карт без возвращения
    probability_b = 1 / deck_size * 1 / (deck_size - 1) * 1 / (deck_size - 2)
    # в) В указанном порядке с возвращением каждой карты в колоду
    probability_c = calculate_probability(deck, deck_size)
    return probability_a, probability_b, probability_c


# Создаем колоду карт
deck = ['Тройка', 'Туз', 'Семерка'] + [str(i) for i in range(2, 11)] + ['Валет', 'Дама', 'Король'] * 4

# Проводим серию экспериментов
num_experiments = 100000
count_a = count_b = count_c = 0

for _ in range(num_experiments):
    # Извлекаем три карты
    drawn_cards = draw_cards(deck, 3)
    # Проверяем условия
    if 'Тройка' in drawn_cards and 'Туз' in drawn_cards and 'Семерка' in drawn_cards:
        count_a += 1
    if drawn_cards == ['Тройка', 'Семерка', 'Туз']:
        count_b += 1
    if set(drawn_cards) == set(['Тройка', 'Семерка', 'Туз']):
        count_c += 1

# Рассчитываем вероятности
probability_a = count_a / num_experiments
probability_b = count_b / num_experiments
probability_c = count_c / num_experiments

# Выводим результаты
print("Вероятность (а):", probability_a)
print("Вероятность (б):", probability_b)
print("Вероятность (в):", probability_c)
