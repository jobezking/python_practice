print("Jesus Christ is Lord")
outline = "Jesus Christ is the Son of God and Savior of humanity."
length = len(outline)
print("It is true that" + outline)
print(outline[:length//2])
print(outline[length//2:])

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

coordinates = (40.7128, -74.0060)  # tuple representing latitude and longitude of New York City

x = ["Now", "we", "are", "cooking!"]
if "Today" not in x:
    print("Today is not in the list.")

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

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

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

multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

new_list = []
for thing in list_of_things:
   new_list.append(do_something(thing))

# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
numbers = [(1, 2, 3) for _ in range(5)]

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

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
file_counts["txt"]
"jpg" in file_counts
"html" in file_counts
file_counts["cfg"] = 8
file_counts["csv"] = 17
del file_counts["cfg"]

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys()
file_counts.values()

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values():
  print(value)

key = 'banana'
if key in myDictionary:
	print(f"The value of {key} is {myDictionary[key]}")
else:
	print(f"{key} is not found in the dictionary")

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")

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