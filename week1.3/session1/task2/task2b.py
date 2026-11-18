# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 2b

print("This program will repeat everything you type.")
print("To exit the program type quit")

while True:
    user_input = input("Say something: ")

    # Added: if the user types 'quit', leave the loop with break
    # (checked before printing, so 'quit' itself is not echoed back)
    if user_input == "quit":
        break

    print(f"You said: {user_input}")

print("Goodbye!")
