
print("Learning progress tracker")

while True:
    input_string = input()

    if input_string.strip() == "":
        print("No input.")
    elif input_string == "exit":
        print("Bye!")
        break
    else:
        print("Error: unknown command!")