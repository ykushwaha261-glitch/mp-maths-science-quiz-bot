import json

questions = [
    {
        "subject": "Science",
        "question": "पानी का रासायनिक सूत्र क्या है?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O"
    },
    {
        "subject": "Maths",
        "question": "12 × 8 = ?",
        "options": ["84", "96", "88", "108"],
        "answer": "96"
    }
]

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)

print("Questions saved successfully!")
