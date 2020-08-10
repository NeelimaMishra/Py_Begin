# frequency of a character in a string

def freq_char(n):
    output_string = {}
    print("type of out_str is {}".format(type(output_string)))
    for i in n:
        if i in output_string:
            output_string[i] += 1
        else:
            output_string = 1
    return output_string

def main():
    n = "aabbcdbeefeg"
    print("type of n is {}".format(type(n)))
    result = freq_char(n)
    print("frequency of a character in a string is: {}".format(result))

if __name__ == "__main__":
    main()

# str1 = "aabbcdbeefeg"
# out_str1 = {}
# for i in str1:
#     if i in out_str1:
#         out_str1[i] += 1
#     else:
#         out_str1[i] = 1
# print(out_str1) # {'a': 2, 'b': 3, 'c': 1, 'd': 1, 'e': 3, 'f': 1, 'g': 1}