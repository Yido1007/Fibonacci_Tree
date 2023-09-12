def fibonacci_list(max):
    Numbers=[]
    a,b=0,1

    while len(Numbers)< max:
        Numbers.append(b)
        a,b=b,a+b
    return Numbers

print(fibonacci_list(5))