#7. Write a Python program to accept a filename from the user and print the extension of that.
#Sample filename : abc.java
#Output : java
be = str(input("Input the Filename: "))
print(be.split('.')[1])
