def compare_strings(str1, str2):
    if str1 < str2:
        return f'"{str1}" comes before "{str2}"'
    elif str1 > str2:
        return f'"{str1}" comes after "{str2}"'
    else:
        return f'"{str1}" is equal to "{str2}"'

# Example usage
string1 = 'pear'
string2 = 'pear'
result = compare_strings(string1, string2)
print(result)
