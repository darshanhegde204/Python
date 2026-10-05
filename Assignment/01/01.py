#celcius to fahrenheit
def celsius_to_fahrenheit(c: float) -> float:
    # Write your solution here
    pass
    ans=(c*9/5)+32
    if ans.is_integer():
        return int(ans)
    else:
        return ans