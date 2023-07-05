var = 15

fizz = var % 3
buzz = var % 5

if fizz == 0 and buzz == 0:
  print("FizzBuzz")
elif fizz == 0:
  print("Fizz")
elif buzz == 0:
  print("Buzz")
else:
  print(var)