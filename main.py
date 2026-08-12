'''
-1 = number < mid
0 = number == mid
1 = number > mid
'''

print("Guess a number 1 to 100\nThen I can get the number less then 7 question.")

mini = 0
max = 100

print("Are you ready(press enter to start): ")
input()

while mini < max:
    mid = int((max+mini)/2)
    
    n = int(input(f"Is your number less, equal or large(-1,0,1) then {mid}: "))

    if(n == -1):
        max = mid

    elif(n == 1):
        mini = mid

    else:
        print("The number is: ",mid)
        break