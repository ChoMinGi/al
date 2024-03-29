def sliding_window():
    n = int(input())
    chemical = list(map(int, input().split()))
    chemical = sorted(chemical)

    res = []
    total = 2*int(1e9)
    left = 0
    right = n-1

    while(left<right):
        td = chemical[left]+chemical[right]
        if td>=0:
            if total>td:
                total = td
                res = [chemical[left],chemical[right]]
            right-=1
        else:
            if total>-td:
                total = -td
                res = [chemical[left],chemical[right]]
            left+=1

    if len(chemical)==2:
        print(chemical[0],chemical[1])
    else:
        print(res[0],res[1])



def binary_search():
    n = int(input())
    chemical = list(map(int, input().split()))
    chemical = sorted(chemical)

    res = []
    total = 2*int(1e9)
    for i in range(n-1):
        left=i+1
        right = n-1
        while(left<=right):
            mid = (right+left)//2
            td = chemical[i]+chemical[mid]
            if td>=0:
                if total>td:
                    total = td
                    res = [chemical[i],chemical[mid]]
                right = mid-1
            else:   
                if total>-td:
                    total = -td
                    res = [chemical[i],chemical[mid]]
                left = mid+1


    if len(chemical)==2:
        print(chemical[0],chemical[1])
    else:
        print(res[0],res[1])