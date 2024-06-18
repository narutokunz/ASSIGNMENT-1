def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

is_present = check_substring(main_string, substring)

if is_present:
    print(f"The substring '{substring}' is present in the main string '{main_string}'.")
else:
    print(f"The substring '{substring}' is NOT present in the main string '{main_string}'.")

