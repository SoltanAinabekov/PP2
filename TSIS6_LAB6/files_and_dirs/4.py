# Write a Python program to count the number of lines in a text file.
def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)

file_path = r"SoltanAinabekov/PP2/TSIS6_LAB6/files_and_dirs/test.txt"
print(f"Number of lines: {count_lines(file_path)}")
