# prefix suffix product is the solution for all
def productExceptSelf(arr):
        n = len(arr)
        output = [1] * n
        # prefix product
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= arr[i]
        # suffix product
        suffix = 1
        for i in reversed(range(n)):
            output[i] *= suffix
            suffix *= arr[i]
        return output

arr = [1,2,4,6]
print(productExceptSelf(arr))



# below logic results in error
# if 0 in arr
# if constraints forbid division
'''def products(arr):
    product = 1
    for num in arr:
        product *= num

    result = []
    for i in range(len(arr)):
        res = product//arr[i] 
        result.append(res)
    return result'''