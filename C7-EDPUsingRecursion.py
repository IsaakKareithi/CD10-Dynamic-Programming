# EDP using recursion
def editDistance(str1, str2, m, n):

    # if first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m == 0:
        return n
    
    # if second string is empty, the only option is to 
    # remove all characters of first string 
    if n == 0:
        return m 
    
    # if last characters of two string are same, nothing 
    # much to do. Ignore last caracters and get count 
    # for the remaining strings
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    
    # If last characters are not same, consider all three
    # operatinos on last character of first string, recursively
    # compute minimum cost for all three operations and take 
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n-1),
                   editDistance(str1, str2, m-1, n),
                   editDistance(str1, str2, m-1, n-1)
                   )

# driver code
str1 = input("Enter the first string for comparison: ")
str2 = input("Enter the second string for comparison: ")

print(editDistance(str1, str2, len(str1), len(str2)))