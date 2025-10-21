def create_file_and_count_occurrences():
    file_name = input("Enter the file name to create: ")
    with open(file_name, 'w') as file:
        print("Enter the contents of the file (press Enter to finish):")
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')
    print("\nContents of the file:")
    with open(file_name, 'r') as file:
        print(file.read())
    letter = input("\nEnter the letter to count occurrences: ")
    with open(file_name, 'r') as file:
        content = file.read()
        count = content.count(letter)
        print(f"\nThe letter '{letter}' occurs {count} times in the file.")
create_file_and_count_occurrences()
