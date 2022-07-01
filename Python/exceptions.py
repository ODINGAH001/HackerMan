#python3
for _ in range(int(input())):
    try:
        a,b=input().split()
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
