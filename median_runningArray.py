import math

def intake_Print_Median():
    arr = []
    x = 0
    while(x != -1):
        x = int(input("Enter a number : "))
        arr.append(x)
        arr = sorted(arr)
        if(len(arr)%2 == 0):
            med = int((arr[int((len(arr)/2)-1)]+arr[int(len(arr)/2)])/2)
        else:
            med = arr[math.floor(len(arr)/2)]
        print("Median : ",med)

intake_Print_Median()


#https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
