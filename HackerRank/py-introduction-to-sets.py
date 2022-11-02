#!usr/bin/python3






def average(arr):
    s = 0
    for item in set(arr):
        s += item
    return s/len(set(arr))
	

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result  = average(arr)
    print(result)
         
