for i in range(3):
    current_line = ""
    
    if i == 0:
        char = '*'
    elif i == 1:
        char = '#'
    elif i == 2:
        char = '$'
        
    for j in range(i + 2):
        current_line += char
        
    print(current_line)