def test():
    s1 = {1, 2, 3}
    s2 = {1, 3}
    s3 = s1 - s2
    print(s1 | s2)
    print(s1 & s2)
    print(s3)
# print(__name__)
# print(__name__ == '集合.py')

if __name__ == '__main__':
    test()


# test()