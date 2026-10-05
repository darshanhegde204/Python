#Perfect Number
def checkPerfectNumber(num: int) -> bool:
    # Write your solution here
    total=1
    for i in range (2,int(num//2)+1):
        if num%i==0 and i<=num//2:
            total+=i
    if num==1:
        return False
    elif total==num:
        return True
    else:
        return False