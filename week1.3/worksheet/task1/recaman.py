# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0]
for number in range(1,L):
    last_number = sequence[-1]
    present_number = last_number - number 
    if present_number > 0 and present_number not in sequence:
        sequence.append(present_number)
    else:
        sequence.append(last_number + number)

print(sequence)



