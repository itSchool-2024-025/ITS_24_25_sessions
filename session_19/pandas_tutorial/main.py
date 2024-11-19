import pandas as pd

def first_pandas_function():
  mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
  }

  myvar = pd.DataFrame(mydataset)

  print(myvar)

def second_pandas_function():
  a = [1, 7, 2]

  myvar = pd.Series(a, index=["x", "y", "z"])

  print(myvar)
  print(myvar["y"])

def third_pandas_function():
  calories = {"day3": 420, "day2": 380, "day1": 390}

  myvar = pd.Series(calories, index=["day1", "day2"])

  print(myvar)

def forth_pandas_function():
  data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
  }

  myvar = pd.DataFrame(data, index=["day0", "day1", "day2"])

  print(myvar.loc[["day0", "day1"]])

if __name__ == '__main__':
  # first_pandas_function()
  # second_pandas_function()
  # third_pandas_function()
  forth_pandas_function()