fileObject = open("rosalind_fibo.txt", "r")
data = int(fileObject.read())


def return_fibo(data):
    if data == 1:
        return data
    elif data == 0:
        return data
    elif data > 1:
        number = return_fibo(data-1) + return_fibo(data-2)
        return number


print(return_fibo(data))
