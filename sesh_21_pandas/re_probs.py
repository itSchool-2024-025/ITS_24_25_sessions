def count_substring(string, sub_string):
    n = 0
    temp_string = string
    while 1:
        if sub_string in temp_string:
            n+=1
            try:
                temp_string = temp_string[temp_string.index(sub_string)+1:]
                print(temp_string)
            except ValueError as e:
                print(e)
                break
        else:
            break
    return n

def count_substring_2(string, sub_string):
    return len(string.split(sub_string))

def count_substring_3(string, sub_string):
    import re
    return len(re.split(sub_string, string))

if __name__ == '__main__':
    # string1 = input("String: ").strip()
    # sub_string1 = input("Sub_String: ").strip()

    count = count_substring("ABCDCDCDC", "CDC")
    print(count)