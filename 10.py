#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
n = input("An integer: \n")
print(int(n)+int(n+n)+int(n+n+n))