import random


def simulate_experiment():
    first_batch = ['нормальное'] * 11 + ['бракованное']
    second_batch = ['нормальное'] * 10 + ['бракованное']
    chosen_item = random.choice(first_batch)
    second_batch.append(chosen_item)
    chosen_item = random.choice(second_batch)
    if chosen_item == 'бракованное':
        return 1
    else:
        return 0


def calculate_probability(num_experiments):
    num_successes = 0
    for _ in range(num_experiments):
        result = simulate_experiment()
        num_successes += result
    probability = num_successes / num_experiments
    return probability


probability = calculate_probability(100000)
print(f'Вероятность: {probability:.4f}')
