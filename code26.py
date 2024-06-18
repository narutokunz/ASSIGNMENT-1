def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)

    return starts_with_prefix, ends_with_suffix

input_string = "Hello, World!"
prefix = "Hello"
suffix = "World!"


starts_with, ends_with = check_prefix_suffix(input_string, prefix, suffix)


print(f"The string '{input_string}'")
print(f"Starts with '{prefix}': {starts_with}")
print(f"Ends with '{suffix}': {ends_with}")
