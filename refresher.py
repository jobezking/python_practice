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

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

to_celsius(75)
hrs, minutes, seconds = convert_seconds(3661)