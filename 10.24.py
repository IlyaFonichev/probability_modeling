import random


def simulate_defective_products(num_iterations, num_products):
    num_defective = 0
    for _ in range(num_iterations):
        defective_count = 0
        for _ in range(num_products):
            if random.random() <= 0.01:
                defective_count += 1
        if defective_count > 3:
            num_defective += 1
    probability = num_defective / num_iterations
    return probability


num_iterations = 100000
num_products = 200

probability = simulate_defective_products(num_iterations, num_products)
print("Вероятность получить более трех дефектных изделий:", probability)
