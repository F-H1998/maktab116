def get_name_and_age():
  name = input("What is your name? ")
  age = int(input("How old are you? "))
  return name, age

def add_to_age(name, age, amount):
  new_age = age + amount
  print(f"{name}, your new age is {new_age}.")

def half_the_age(name, age):
  new_age = age / 2
  print(f"{name}, your new age is {new_age}.")

if __name__ == "__main__":
  name, age = get_name_and_age()
  add_to_age(name, age, amount=int(input("add to your age ...")))
  half_the_age(name, age)