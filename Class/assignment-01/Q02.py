with open("sample.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)
print(f"Total number of lines: {total_lines}")

if total_lines >= 2:
    print(f"2nd Line: {lines[1].strip()}")
else:
    print("2nd Line: File has fewer than 2 lines.")
    
if total_lines >= 4:
    print(f"4th Line: {lines[3].strip()}")
else:
    print("4th Line: File has fewer than 4 lines.")