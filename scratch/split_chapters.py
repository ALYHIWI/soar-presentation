with open('full_project_doc.txt', 'r', encoding='utf-8') as f:
    text = f.read()

ch1_start = text.find('Chapter 1:\n\nIntroduction and Problem Statement')
ch2_start = text.find('Chapter 2\n\nBackground and Literature Review', ch1_start)
ch3_start = text.find('Chapter 3:\n\nProposed System Architecture', ch2_start)
ref_start = text.find('References\n\nAgrawal', ch3_start)

print(f"Ch1: {ch1_start} to {ch2_start} ({ch2_start - ch1_start} chars)")
print(f"Ch2: {ch2_start} to {ch3_start} ({ch3_start - ch2_start} chars)")
print(f"Ch3: {ch3_start} to {ref_start} ({ref_start - ch3_start} chars)")
print(f"Ref: {ref_start} to {len(text)} ({len(text) - ref_start} chars)")

with open('scratch/ch1_full.txt', 'w', encoding='utf-8') as f:
    f.write(text[ch1_start:ch2_start])

with open('scratch/ch2_full.txt', 'w', encoding='utf-8') as f:
    f.write(text[ch2_start:ch3_start])

with open('scratch/ch3_full.txt', 'w', encoding='utf-8') as f:
    f.write(text[ch3_start:ref_start])

with open('scratch/references_full.txt', 'w', encoding='utf-8') as f:
    f.write(text[ref_start:])

print("Successfully wrote ch1_full.txt, ch2_full.txt, ch3_full.txt, references_full.txt")
