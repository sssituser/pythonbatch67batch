num = int(input('Enter num : ')) # num = 2,6
if num==0: # 0==0 True 1==0 F 2==0-F 3==0F
    print('ZERO') # ZERO
elif num==1: # 1 == 1 -T  2 == 1 - F 3==1 F
    print('ONE') # ONE
elif num==2: # 2==2 - T  3 == 2 -F
    print('TWO')
elif num == 3: # 3==3 T
    print('THREE') # THREE
else:
    print('Entered Numer is other than 0,1,2,3')