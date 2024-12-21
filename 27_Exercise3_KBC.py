# Display a welcome message for the game
print("Welcome to Kaun Banega Crorepati!\n")

# List of questions for the game, each represented as a dictionary
questions = [
    {
        "question": "What is the capital of India?",  # The question text
        "options": ["1: Mumbai", "2: Delhi", "3: Kolkata", "4: Chennai"],  # List of options
        "answer": 2,  # The correct option (2 = Delhi)
        "prize": 1000  # Prize money for answering this question correctly
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["1: Earth", "2: Mars", "3: Jupiter", "4: Saturn"],
        "answer": 3,  # The correct option (3 = Jupiter)
        "prize": 2000
    },
    {
        "question": "What is the square root of 64?",
        "options": ["1: 6", "2: 7", "3: 8", "4: 9"],
        "answer": 3,  # The correct option (3 = 8)
        "prize": 5000
    },
    {
        "question": "Who wrote the Mahabharata?",
        "options": ["1: Valmiki", "2: Ved Vyas", "3: Tulsidas", "4: Kalidas"],
        "answer": 2,  # The correct option (2 = Ved Vyas)
        "prize": 10000
    }
]

# Variable to keep track of the player's total prize money
total_prize = 0

# Variable to track the current question number (starts from 1)
question_number = 1

# Loop through each question in the `questions` list
for q in questions:
    # Display the current question number and the question text
    print(f"Question {question_number}: {q['question']}")
    
    # Display all the options for the current question
    for option in q["options"]:
        print(option)
    
    # Ask the player to enter their answer as a number (1-4) or type "quit" to exit
    user_input = input("Enter the option number (1-4) or type 'quit' to exit: ").strip().lower()
    
    # Check if the user wants to quit
    if user_input == 'quit':
        print(f"You've decided to quit the game. Your total prize is ₹{total_prize}.")
        break  # Exit the loop and end the game
    
    # Check if the input is valid (a number between 1 and 4)
    if not user_input.isdigit() or int(user_input) not in range(1, 5):
        # If the input is not valid, show an error message and end the game
        print("Invalid input! You lost the game.")
        break  # Exit the loop
    
    # Convert the user's input from a string to an integer
    user_answer = int(user_input)
    
    # Check if the player's answer is correct
    if user_answer == q["answer"]:
        # If correct, add the prize money for this question to the total
        total_prize += q["prize"]
        # Display a success message and the updated total prize money
        print(f"Correct! You've won ₹{q['prize']}. Total prize: ₹{total_prize}\n")
    else:
        # If the answer is wrong, show the correct answer
        print(f"Wrong answer! The correct answer was option {q['answer']}.")
        # Display the total prize money the player has won so far
        print(f"You are taking home ₹{total_prize}. Thank you for playing!")
        break  # Exit the loop and end the game
    
    # Increment the question number for the next question
    question_number += 1
else:
    # If the player answers all questions correctly, congratulate them
    print(f"Congratulations! You've answered all questions correctly. Your total prize is ₹{total_prize}.")

# Display a goodbye message at the end of the game
print("\nGame Over. Thank you for playing Kaun Banega Crorepati!")
