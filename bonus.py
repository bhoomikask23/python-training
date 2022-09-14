print('enter salary')

salary = int(input())

print('enter number of years working in company')

years=int(input())

if years>=10:

    bonus = (15*salary)/100

    final = salary+ bonus

    print(final)

elif years>=5 and years<10:

    bonus = (10*salary)/100

    final = salary+ bonus

    print(final)

elif years>=3 and years<5:

    bonus = (5*salary)/100

    final = salary+ bonus

    print(final)

else:

    print('not eligible')