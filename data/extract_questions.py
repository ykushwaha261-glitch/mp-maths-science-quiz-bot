import fitz
import json

pdf = fitz.open("PSTET_2024.pdf")

questions = []

for page in pdf:
    text = page.get_text()

    questions.append({
        "page": page.number + 1,
        "text": text
    })

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Questions extracted successfully!")
