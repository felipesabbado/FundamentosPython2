# 2.3.25   LAB   Your own split
def mysplit(strng, sep = ' '):
    result = list()
    sub_strng = ''

    for c in strng:
        if c != sep:
            sub_strng += c
        if c == sep:
            if len(sub_strng) > 0:
                result.append(sub_strng)
                sub_strng = ''
    if len(sub_strng) > 0:
        result.append(sub_strng)

    return result



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
