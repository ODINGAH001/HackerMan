#python3
n=int(input())
for var in range(1,n+1):
    print(str(var).rjust(len(format(n,'b')),' ')+str(format(var,'o')).rjust(len(format(n,'b'))+1,' ')+str(format(var,'x')).upper().rjust(len(format(n,'b'))+1,' ')+str(format(var,'b')).rjust(len(format(n,'b'))+1,' '))
