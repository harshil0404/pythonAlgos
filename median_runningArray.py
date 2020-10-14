import math

def sort(arr):
    for j in range(len(arr)-1): 
        for i in range (len(arr)-1):
            if(arr[i+1] < arr[i]):
                temp = arr[i] 
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def intake_Print_Median():
    arr = []
    x = 0
    while(x != -1):
        x = int(input("Enter a number : "))
        arr.append(x)
        arr = sort(arr)
        if(len(arr)%2 == 0):
            med = int((arr[int((len(arr)/2)-1)]+arr[int(len(arr)/2)])/2)
        else:
            med = arr[math.floor(len(arr)/2)]
        print("Median : ",med)

intake_Print_Median()


#https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/