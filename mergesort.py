    
    
    #Merge sort
   
    #To sort a user input list of numbers
    
    #By DemonicAj 
   
def merge(arr,l,m,h):
    n1=m-l+1
    n2=h-m
    t=[0] * (n1)
    s=[0] * (n2)
    for i in range(0,n1):
        t[i]=arr[l+i]

    for j in range(0,n2):
        s[j]=arr[m+1+j]

    i=0
    j=0
    k=l #initial index of new array will be low (l)
    while i<n1 and j<n2:
        if t[i] <= s[j]:
            arr[k]=t[i]
            i+=1
        else:
            arr[k]=s[j]
            j+=1
        k+=1
        
    while i<n1:
        arr[k]=t[i]
        i+=1    
        k+=1
    while j<n2:
        arr[k]=s[j]
        j+=1
        k+=1
    

def mergeSort(arr,l,h):
    if l<h:
        m=(l+(h-1))//2
        
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,h)
        merge(arr,l,m,h)

if __name__=="__main__":
        
    n=int(input("Enter the no. of elements you want to sort :"))
    arr=[0]*n
    print("Enter the list you want to sort :")
    for i in range(0,n):
        arr[i]=int(input())
    #arr=[3,6,8,32,5,1] # test case
    #n=len(arr)
    print ("Given array is :")
    print(arr)
    print ("Sorted array is :")
    mergeSort(arr,0,n-1)
    print(arr)
