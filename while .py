"""
i=0
while(True):
    print(i)
    if i==44:
      break
    i=i+1
"""
num = [1,2,3,4,5,-1,-2]
sum_positive = 0
for nums in num:
    if nums>0:
        continue
    sum_positive +=nums
print(f"sum of the positive number {sum_positive}")    