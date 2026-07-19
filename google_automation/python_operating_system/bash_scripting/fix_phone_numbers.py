import re

with open("data/phones.csv", "r") as phones:

 for phone in phones:
   new_phone = re.sub(r"^\D*(\d{3})\D*(\d{3})\D*(\d{4})$", r"(\1) \2-\3", phone)
   print(new_phone)

