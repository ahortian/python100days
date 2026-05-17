questions = [
    ("What is 2 + 3? ", 5),
    ("What is 4 * 2? ", 8),
    ("What is 10 - 6? ", 4),
    ("What is 9 // 3? ", 3),
    ("What is 7 + 5? ", 12),
]

for prompt, correct_answer in questions:
    try:
        user_input = input(prompt)
        answer = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        break

    if answer == correct_answer:
        print("Correct! Great job!")
    else:
        print("That is not correct. Goodbye.")
        break
