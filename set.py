
#unordered and unindex update is not directly possible
s=set(())
print(s)

s.add(1) #duplicates values are not allowed in set
s.add(2)
s1 = set({10,20,30})
print(s)
print(s1)

s2= s.union({1,2,3})
print(s2)
s3=s.intersection({1,5,6})
print(s3)

print(s.isdisjoint(s1))






