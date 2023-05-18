import random


def simulate_experiment(probability, num_experiments):
    event_count = 0
    for _ in range(num_experiments):
        if random.random() < probability:
            event_count += 1
    return event_count


def calculate_probability(num_simulations, probability, num_experiments):
    event_occurrences = 0
    for _ in range(num_simulations):
        if simulate_experiment(probability, num_experiments) >= 3:
            event_occurrences += 1
    return event_occurrences / num_simulations


num_simulations = 10000
probability = 0.2
num_experiments = 18

result = calculate_probability(num_simulations, probability, num_experiments)
print(f"Вероятность появления события по крайней мере три раза: {result}")
