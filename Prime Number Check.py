n = int(input("Enter a number: "))

if n < 2:
    print(f"{n} is Not Prime")

else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is Not Prime")
            break
    else:
        print(f"{n} is Prime")

