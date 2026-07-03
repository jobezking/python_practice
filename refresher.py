print("Jesus Christ is Lord")
outline = "Jesus Christ is the Son of God and Savior of humanity."
print("It is true that" + outline)

for i in range(5):
    print(f"Iteration {i + 1}: Remember to follow the teachings of Jesus Christ.")

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

def to_celsius(x):
    return (x-32) * 5/9

to_celsius(75)