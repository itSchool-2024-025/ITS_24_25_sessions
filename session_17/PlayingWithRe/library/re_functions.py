import re
# Take a look at https://regexr.com/

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    input_string = "I love PyCharmPyCharm"
    pattern = r"PyCharm"
    print(re.search(pattern, input_string))
    input_string = "Str. OnePiece, Nr. 13"
    pattern = r"Str. (\w+)"
    match = re.search(pattern, input_string)
    input_string = match.group()
    pattern = r"[^Str. ](\w+)"
    print(re.search(pattern, input_string))

def find_all_with_re():
    pattern = r"Py"
    input_string = "I love PyPyPyCharmuma muma muma"
    match = re.findall(pattern, input_string)
    print(re.findall(pattern, input_string))

def split_using_re():
    pattern = r"\n Test Procedure"
    input_string = "Test Precondition: abhvfgliuawervbiluaewr \n Test Procedure: avbiawbv"
    match = re.split(pattern, input_string)
    pattern = r"Test Precondition: "
    input_string = match[0]
    match = re.split(pattern, input_string)
    print(match)

def replace_using_re():
    pattern = r"Test"
    replace_with = r"sleep"
    input_string = "Test Precondition: abhvfgliuawervbiluaewr \n Test Procedure: avbiawbv"
    match  = re.sub(pattern, replace_with, input_string)
    print(match)
