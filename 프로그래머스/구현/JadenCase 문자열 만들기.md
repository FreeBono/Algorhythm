```python
def solution(s):
    answer = ''

    s = s.split(' ')
    for i in s:
        tmp = list(i.lower())
        if tmp:
            tmp[0] = tmp[0].upper()
            tmp = ''.join(tmp)
            answer += tmp +' '
            
        else:
            answer += ' '
        
    
    answer = answer[:-1]
    
    return answer
```

