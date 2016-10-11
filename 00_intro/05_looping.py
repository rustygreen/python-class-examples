# http://www.programiz.com/python-programming/built-in-function
# loop through each line in the text file and print it out
for line in open("assets/hello.txt"):
    print line

i = 0
while i < 5:
    print(i)
    i += 1  # Comment me out, and I'll loop forever :(
