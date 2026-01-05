name = "Aleksandr"
surname = "piskarev"
age = 29
print("Hello " + name + " " + surname + "! My age is: " + str(age))
formated_string = "Hello {2} {0}! My age is: {1}".format(surname, age, name)
print(formated_string)
print(f"Hello {name.upper()} {surname.capitalize()}! My age is: {age}")

x = 5
y = 10
result = x + y
print(f"{x = }, {y = }, {result = }")

total = 1000000000000
print(f"{total:,}")

pi = 3.1443435435
print(f"{pi:.2f}")

print(f"{name:*^21}")
print(f"{surname:*^21}")

BASE_URL = "https://www.reqres.in"
CASES_API = f"{BASE_URL}/cases"
USERS_API = f"{BASE_URL}/users"
USER_API = f"{USERS_API}/{name}"
print(f"{USER_API = }")