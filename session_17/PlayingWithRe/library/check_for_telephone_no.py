import re

# Verify that the user input a valid phone number (10 digits, starts with 07)
# based on the first 3 digits, determine if the phone no. is an Orange, Vodafone ro Digi phone no.
# if not recognized, call the cops.

def get_user_input(message_to_user):
    return input(message_to_user)

def check_if_phone_no_len_is_valid():
    """
    Description: Function will check the phone number for correct len.
    :return:
    """
    expected_len = 10
    phone_no = get_user_input("Please tell me your phone no.: ")
    if expected_len == len(phone_no):
        return True, phone_no
    else:
        return False

def check_if_phone_no_is_an_orange_phone_no(phone_no):
    # pattern = r"^07[^0356789]\d{7}"
    pattern = r"^07[^021356789]\d{7}"
    if re.findall(pattern, phone_no):
        print("Orange")
    else:
        print("mumu")


if __name__ == "__main__":
    try:
        _,var1 = check_if_phone_no_len_is_valid()
        check_if_phone_no_is_an_orange_phone_no(var1)
    except:
        print("len NOK")