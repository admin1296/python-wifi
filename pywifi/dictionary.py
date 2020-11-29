import itertools as its
words = "1234568790"
r =its.product(words,repeat=9)
dic = open("pass.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
