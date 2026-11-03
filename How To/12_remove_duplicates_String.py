def removeDuplicate(text):
    s = set(text)
    s = "".join(s)
    print("Without Order:", s)

    t = ""
    for i in text:
        if i in t:
            pass
        else:
            t = t + i

    print("With Order:", t)


test = "this is the testing program"
removeDuplicate(test)