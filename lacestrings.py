def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here

    laced = ''
    space = 0
    while len(s1) > 1 and len(s2) > 1:
        laced += s1[0]+s2[0]
        s1 = s1[1:]
        s2 = s2[1:]
    
    if len(s1) < len(s2):
        laced += s1
        laced += s2
    elif len(s2) < len(s1):
        laced += s1[0]
        laced += s2
        laced += s1[1:]
    else:
        laced += s1
        laced += s2
    
    return laced