def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        return any(McNuggets(n - x) for x in [20, 9, 6])
