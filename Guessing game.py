num = 9
count = 0
while count < 3:
    guess = int(input("Enter number: "))
    count += 1
    if guess == num:
        print("This guess value is correct")
        break
else:
    print("failed")
