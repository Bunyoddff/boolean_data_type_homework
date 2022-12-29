from math import sqrt
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """

    s=(sqrt(a))
    d=((s-int(s))==0)
    # Write your code here
    return d
print(main(121)) 