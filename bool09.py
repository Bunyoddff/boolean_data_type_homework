def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    s=(a>=1 and a<=9 and a*1.0==int(a))
    # Write your code here
    return s
print(main(7)) 
