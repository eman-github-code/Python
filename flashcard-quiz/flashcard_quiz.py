import json

def load_flashcards(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Flashcard file not found.")
        return []

def run_quiz(flashcards):
    score = 0
    total = len(flashcards)

    for i, card in enumerate(flashcards, start=1):
        print(f"\nQuestion {i}: {card['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == card['answer'].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {card['answer']}")

    print(f"\n🎯 Quiz complete! You scored {score}/{total}.")

def main():
    flashcards = load_flashcards("flashcards.json")
    if flashcards:
        run_quiz(flashcards)

if __name__ == "__main__":
    main()
