print("Jesus Christ is Lord")
outline = "Jesus Christ is the Son of God and Savior of humanity."
length = len(outline)
print("It is true that" + outline)
print(outline[:length//2])
print(outline[length//2:])

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

x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

def get_username():
    username = input("Enter your username: ")
    return username

def valid_username(username):
    return len(username) >= 5 and username.isalnum()

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

product = 1
for n in range(1,10):
  product = product * n

for n in range(2,64,2):
  product = product * n

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)

def to_celsius(x):
    return (x-32) * 5/9

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

to_celsius(75)
hrs, minutes, seconds = convert_seconds(3661)