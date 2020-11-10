a = [3,2,0,1,2,0,5]
# in this question we can move fordward in array at max the number on which we are. ex from index 0 ele. 3 
# we can move max of 3 position fordward and the goal is to reach the end of the array...
fr = 0
for i in range(len(a)):
    fr = max(fr,a[i]+i)
    if i >= fr :
        print('Not Possible to reach to end of array')
        break
if i < fr :
    print('Yes Its possible!!')
