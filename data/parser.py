import fitz

pdf = fitz.open("MSTST_PSTST_2024.pdf")

print("Total Pages:", len(pdf))
