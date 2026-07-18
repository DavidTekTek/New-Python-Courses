def run_quiz():
    questions = [
        {
            "question": "What color do you get when you mix red and blue?",
            "choices": ["A. Green", "B. Purple", "C. Orange"],
            "answer": "B"
        },
        {
            "question": "How many legs does a spider have?",
            "choices": ["A. 6", "B. 8", "C. 10"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 3?",
            "choices": ["A. 7", "B. 8", "C. 9"],
            "answer": "B"
        },
        {
            "question": "Which animal says 'meow'?",
            "choices": ["A. Dog", "B. Cat", "C. Cow"],
            "answer": "B"
        },
        {
            "question": "What planet do we live on?",
            "choices": ["A. Mars", "B. Earth", "C. Venus"],
            "answer": "B"
        }
    ]

    score = 0

    print("Welcome to the Kids Quiz!")
    print("Answer each question by typing A, B, or C.")
    print()

    for idx, item in enumerate(questions, 1):
        print(f"Question {idx}: {item['question']}")
        for choice in item["choices"]:
            print(choice)

        answer = input("Your answer: ").strip().upper()
        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_choice = next(c for c in item["choices"] if c.startswith(item["answer"]))
            print(f"Nice try. The right answer is {correct_choice}.\n")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")


if __name__ == "__main__":
    run_quiz()