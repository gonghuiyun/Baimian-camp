arr= [1,3,5,4,2,6,9,7,0,8]
def heapInsert(arr,i):
    while i>0:
        if arr[i]>arr[int(i-1)/2]