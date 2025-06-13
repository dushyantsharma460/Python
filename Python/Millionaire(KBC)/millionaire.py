questions = [
    ["Who is Shah Rukh Khan?", "Actor", "Plumber", "Electrician", "Labour", 1],
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote the Indian national anthem?", "Rabindranath Tagore", "Mahatma Gandhi", "Subhas Chandra Bose", "Jawaharlal Nehru", 1],
    ["Which is the largest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
    ["What is H2O commonly known as?", "Salt", "Water", "Oxygen", "Hydrogen", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 3],
    ["What is the currency of Japan?", "Yuan", "Rupee", "Won", "Yen", 4],
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["Who discovered gravity?", "Newton", "Einstein", "Galileo", "Tesla", 1]
]

# Define prizes in millions
prizes = [
    "1 Million", "2 Million", "3 Million", "5 Million", "10 Million",
    "20 Million", "40 Million", "80 Million", "90 Million", "100 Million"
]

i = 0

for question in questions:
    print("\n" + question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    try:
        a = int(input("Enter your answer (1-4): "))

        if a < 1 or a > 4:
            print("Invalid choice. Please select between 1 and 4.")
            break

        if question[5] == a:
            print("✅ Correct Answer!")
            print(f"You won {prizes[i]}")
            i += 1
        else:
            correct_option = question[5]
            print(f"❌ Incorrect. The correct answer was {correct_option}. {question[correct_option]}")
            print("Better luck next time!")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a number from 1 to 4.")
        break
