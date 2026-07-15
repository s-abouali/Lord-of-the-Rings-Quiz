score = 0

questions = [
    {
        "question": "Who is the Ring-bearer?",
        "answer": "Frodo Baggins",
        "options": ["Bilbo Baggins", "Frodo Baggins", "Samwise Gamgee", "Merry Brandybuck"]
    },
    {
        "question": "What is the name of the wizard known as the Grey?",
        "answer": "Gandalf",
        "options": ["Saruman", "Radagast", "Gandalf", "Elrond"]
    },
    {
        "question": "Who forged the One Ring?",
        "answer": "Sauron",
        "options": ["Saruman", "Sauron", "Celebrimbor", "Smaug"]
    },
    {
        "question": "What creature is obsessed with the One Ring?",
        "answer": "Gollum",
        "options": ["Legolas", "Gollum", "Gimli", "Boromir"]
    },
    {
        "question": "What is the capital city of Gondor?",
        "answer": "Minas Tirith",
        "options": ["Edoras", "Helm's Deep", "Minas Tirith", "Bree"]
    },
    {
        "question": "Who says, 'You shall not pass!'?",
        "answer": "Gandalf",
        "options": ["Aragorn", "Gandalf", "Legolas", "Boromir"]
    },
    {
        "question": "What race is Legolas?",
        "answer": "Elf",
        "options": ["Human", "Dwarf", "Elf", "Hobbit"]
    },
    {
        "question": "Who becomes King of Gondor?",
        "answer": "Aragorn",
        "options": ["Boromir", "Faramir", "Aragorn", "Theoden"]
    },
    {
        "question": "What mountain must the One Ring be destroyed in?",
        "answer": "Mount Doom",
        "options": ["Lonely Mountain", "Mount Doom", "Mount Gundabad", "Caradhras"]
    },
    {
        "question": "What is the name of Frodo's loyal best friend?",
        "answer": "Samwise Gamgee",
        "options": ["Pippin Took", "Merry Brandybuck", "Samwise Gamgee", "Bilbo Baggins"]
    }
]

print("🧝 ===== LORD OF THE RINGS QUIZ ===== 🧙\n")

for i, q in enumerate(questions, start=1):
    print(f"Question {i}")
    print(q["question"])
    print()

    for j, option in enumerate(q["options"], start=1):
        print(f"{j}. {option}")

    while True:
        try:
            choice = int(input("\nEnter your answer (1-4): "))
            if 1 <= choice <= 4:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

    if q["options"][choice - 1] == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print("🏆 ===== QUIZ COMPLETE =====")
print(f"⭐ Your Score: {score}/{len(questions)}")

if score == 10:
    print("👑 You are the true Lord of the Rings champion!")
elif score >= 8:
    print("🧝 Excellent! You're a master of Middle-earth.")
elif score >= 5:
    print("⚔️ Good job! You know your way around Middle-earth.")
else:
    print("📖 Time to rewatch the trilogy and try again!")