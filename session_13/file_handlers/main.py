import os.path


def read_from_textfile(filepath):
    print(filepath)
    print(os.path.isfile(filepath))
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        # print(file.readline())
        print(file.readlines())
        file.close()
    else:
        print("damn it!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    absolutefilepath = ("/Users/danienasescu/Documents/IT School/"
                        "pythonProjects/ITS_24_25_session_9/ITS_24_25_sessions/"
                        "session_13/file_handlers/newtxt1.txt")
    relativefilepath = "newtxt.txt"
    relativefilepath2 = "databases/newtxt1.txt"

    read_from_textfile(relativefilepath2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
