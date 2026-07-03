days = {"sunday":1,"monday":2,"tuesday":3,"wednesday":4,"thursDay":5,"friday":6,"saturday":7}
while True:
    day = input('Enter Day : ')
    day =day.lower()
    if days.__contains__(day):
        print(f'{day} number is {days[day]}')
    else:
        print("Enter Proper Day")

