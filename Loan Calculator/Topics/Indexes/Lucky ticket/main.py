# Save the input in this variable
ticket = input()
half1 = 0
half2 = 0
for i in range(3):
    half1 += int(ticket[i])
    half2 += int(ticket[-i-1])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
