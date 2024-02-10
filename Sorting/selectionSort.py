def selectionSort(arr,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index],arr[i]

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    selectionSort(arr,n)
    for i in range(n):
        print(arr[i],end=' ')
    print()

if __name__== '__main__':
    main()