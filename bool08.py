def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    s=(a>0  or a>=0 and a*1.0==int(a))
    # Write your code here
    return s
print(main(-1)) 
