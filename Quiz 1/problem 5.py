def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    shorter, longer = sorted([s1, s2], key=len)
    output = []
    for i in range(len(shorter)):
        output.append(s1[i])
        output.append(s2[i])
    output += longer[len(shorter):]
    return "".join(output)