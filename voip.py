import random

secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Твой вариант: "))
    attempts += 1

    if guess < secret_number:
        print("Слишком маленькое!")
    elif guess > secret_number:
        print("Слишком большое!")
    else:
        print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
        break