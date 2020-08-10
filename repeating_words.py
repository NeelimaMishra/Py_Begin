# find a repeated word in a string

def repeat_word(str1):
    count = 0
    word = "geeks"
    str1 = str1.split(" ")
    print("str1 after split is {}".format(str1))
    for i in range(len(str1)-1):
        if str1[i] == word:
            count += 1
    return count

def main():
    str1 = "Geeksfor geeks A computer science portal for geeks"
    result = repeat_word(str1)
    print("word count is: {}".format(result))

if __name__ == '__main__':
    main()