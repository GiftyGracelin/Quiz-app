import json

def load_questions(file):
    with open(file,"r") as f:
        return json.load(f)

def start_quiz():
    questions = load_questions("questions.json")
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🎯 Quiz Over! Your final score: {score}/{len(questions)}")

start_quiz()