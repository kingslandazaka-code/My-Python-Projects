# === Simple Quiz App ===

def ask_question(question, correct_answer):
    """Ask a question and return 1 if correct, else 0"""
    answer = input(question + "\nAnswer: ").lower()
    if answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print("Wrong.\n")
        return 0

def quiz():
    print("=== Simple Quiz ===")
    score = 0

    score += ask_question("1. What is the capital of France?", "paris")
    score += ask_question("2. What is 5 + 3?", "8")
    score += ask_question("3. Which gas do plants breathe in?", "carbon dioxide")

    print("You scored", score, "out of 3.")

quiz()
