# frequency of a word in a string
def freq_word(n):
    out_str1 = {}
    n = n.split(" ")
    for i in n:
        if i in out_str1:
            out_str1[i] += 1
        else:
            out_str1 = 1
    return out_str1

def main():
    n = "book notebook book book"
    result = freq_word(n)
    print("frequency of word is: {}".format(result))

if __name__ == "__main__":
    main()

# n = "book notebook book book"
# out_str1 = {}
# n = n.split(" ")
# for i in n:
#     if i in out_str1:
#         out_str1[i] += 1
#     else:
#         out_str1[i] = 1
# print(out_str1)

