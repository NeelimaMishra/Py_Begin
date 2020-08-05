#l1 = [5,5,3,4,1,2]
#expected_output = [4,2,2,0,0]
def magic_array(array_len,array):
    result = []
    for index,element in enumerate(array):
        sliced_array = array[index+1:]
        count = 0
        for ele in sliced_array:
            if element > ele:
                count += 1
        result.append(count)

        print("result {}".format(result))
    return result
res = magic_array(5,[5,3,4,1,2])
print(res)





