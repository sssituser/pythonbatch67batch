temp = int(input('Enter Temp Deg : '))

if temp>22: # 24>22-T
    if temp<26: #24<26-T
        print('Room Temprature or Normal condition')
    else:
        print('Hot weather')
else:
    print("cold weather")