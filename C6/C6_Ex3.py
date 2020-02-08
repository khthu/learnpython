def is_power(a,b):
    if a%b!=0:
        return False
    if a%b==0:
        return is_power(a/b,b)

print(is_power(8,2))
        


