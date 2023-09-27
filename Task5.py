# Load Quiz Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
        "answer": "Vatican City"
    }
]

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("You will be presented with multiple-choice or fill-in-the-blank questions on a specific topic.")
print("Select an answer for each question. Your score will be calculated at the end of the quiz.")
print()

# Present Quiz Questions
score = 0
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"{j+1}. {option}")
    user_answer = input("Enter your answer: ")
    
    # Evaluate the User's Answer
    if user_answer.lower() == question['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")
    
    print()

# Calculate the Final Score
final_score = (score / len(questions)) * 100

# Display Final Results
print(f"Your final score is {final_score:.2f}%.")
if final_score >= 70:
    print("Congratulations! You passed the quiz.")
else:
    print("Sorry, you did not pass the quiz. Better luck next time!")
