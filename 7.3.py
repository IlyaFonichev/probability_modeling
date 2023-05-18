P_A = 0.96
P_B_given_A = 0.98
P_B_given_not_A = 0.05

# Вычисление P(B)
P_not_A = 1 - P_A
P_B = P_B_given_A * P_A + P_B_given_not_A * P_not_A

# Вычисление P(A|B)
P_A_given_B = (P_B_given_A * P_A) / P_B

print(f"Вероятность: {P_A_given_B:.6f}")
