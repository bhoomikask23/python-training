"""
"r" : read file
"w" :write file











f = open("demo.txt")
content = f.read()
print(content)
f.close()

f = open("demo.txt")
content = f.read(3)
print(content)
content1=f.read(3)
print(content)
f.close()

f = open("demp.txt")
content = f.readlines()
print(content)

f= open("demo.txt","r+")
a = f.write("python\n")
print(a)
f.close

f = open("demo.txt")
print(f.readline())
print(f.readline())
f.seek(1)
print(f.readline())
f.close()


l=10 #global variable
def function(n):
    #1 = 5# local variable
    l=l+20
    print(l)
    print(f"this is the number {n}")
function("")
print(l)   

"""
#lamda
def minus(a,b):
    return (a-b)
c=minus(10,5)
print(c)

minus=lambda x,y :x-y
print(minus(10,5))


