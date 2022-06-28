내가 짠 코드...



```python
def solution(arr):
    answer = 0
    tmp = 1
    start = 2
   
    while start <= max(arr):
        cnt = 0
        for i in range(len(arr)):
            
            if cnt > 1:
                break
            if arr[i] % start == 0:
                cnt += 1

        if cnt > 1:
            tmp *= start
            
            for j in range(len(arr)):
                if arr[j] % start == 0:
                    arr[j] = arr[j] // start
            print(arr)
            start = 2
        else:
            start += 1

    for k in range(len(arr)):
        tmp *= arr[k]
    answer = tmp
  
    return answer
```



다른 사람 코드

```python
def solution(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        while a%b:
            r = a%b
            a = b
            b = r
        arr[i+1] = (arr[i]*arr[i+1])/b
    return arr[-1]
```

