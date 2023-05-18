def calculate_ticket_probability():
    total_tickets = 0
    successful_tickets = 0

    for ticket_number in range(1000000):
        ticket_digits_sum = sum(int(digit) for digit in str(ticket_number))

        if ticket_digits_sum == 21:
            successful_tickets += 1

        total_tickets += 1

    probability = successful_tickets / total_tickets
    return probability


result = calculate_ticket_probability()
print("Вероятность получения билета с суммой цифр равной 21:", result)
