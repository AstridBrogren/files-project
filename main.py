with open("new_file.txt", "a") as file:
    file.write("text.\n")

with open("new_file.txt", "r") as file:
    for line in file:
        print(line[1])

with open("new_file.txt", "r") as file:
    for line in file:
        if len(line) > 7:
            print(line.strip())

new_line = input("24")
with open("new_file.txt", "a") as file:
    file.write(new_line + "\n")