
# ==========================================
# PYTHON WEEK 8 FINAL PROJECT
# MY PYTHON TOOLKIT
# ==========================================


# TOOL 1: SIMPLE CALCULATOR
# This tool performs basic mathematical operations.

def calculator():

    print("\n--- SIMPLE CALCULATOR ---")

    try:
        first_number = float(input("Enter the first number: "))

        operator = input("Choose an operation (+, -, *, /): ")

        second_number = float(input("Enter the second number: "))

        if operator == "+":
            answer = first_number + second_number

        elif operator == "-":
            answer = first_number - second_number

        elif operator == "*":
            answer = first_number * second_number

        elif operator == "/":

            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return

            answer = first_number / second_number

        else:
            print("Invalid operation.")
            return

        print(f"Result: {first_number:g} {operator} {second_number:g} = {answer:g}")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: TO-DO LIST
# This tool allows users to add, view and remove tasks.

def todo_list():

    tasks = []

    while True:

        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":

            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":

            if len(tasks) == 0:
                print("Your to-do list is empty.")

            else:
                print("\nYour tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":

            if len(tasks) == 0:
                print("There are no tasks to remove.")

            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):

                        removed_task = tasks.pop(task_number - 1)

                        print(f"Removed task: {removed_task}")

                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a whole number.")

        elif choice == "4":

            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please choose 1-4.")


# TOOL 3: NUMBER GUESSING GAME
# This tool asks the user to guess a secret number.

def number_guessing_game():

    secret_number = 7
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("Guess a number between 1 and 10!")

    while True:

        try:
            guess = int(input("Enter your guess: "))

            attempts += 1

            if guess < 1 or guess > 10:

                print("Choose a number between 1 and 10.")

            elif guess < secret_number:

                print("Too low! Try a higher number.")

            elif guess > secret_number:

                print("Too high! Try a lower number.")

            else:

                print(f"Congratulations! You guessed correctly in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a whole number.")


# MAIN PROGRAM
# This menu keeps running until the user chooses Quit.

def main():

    print("Welcome! Thanks for using my Python Toolkit.")

    while True:

        print("\n========================================")
        print("       WELCOME TO MY PYTHON TOOLKIT")
        print("========================================")

        print("Please choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":

            calculator()

        elif choice == "2":

            todo_list()

        elif choice == "3":

            number_guessing_game()

        elif choice == "4":

            print("Thank you for using my Python Toolkit. Goodbye!")
            break

        else:

            print(f"Sorry, '{choice}' is not a valid choice. Please try again.")


# Start the program.

if __name__ == "__main__":
    main()
