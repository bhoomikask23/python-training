def message(name,roll_number):
    print(f"this is my name {name} and roll number {roll_number}")
message("bhoomi",22)    

def hra(salary):
    hra = round(salary*60/100)
    print(hra)
    return hra  #
a=hra(70000)
print(a)    

def odd_number(n):
    if n % 2==0:
        print("this is even number")
    else:
        print("odd number")

odd_number(17)

#builtin funaction

#print("randint"(10000,2000))