str = int(input())
for i in range(str):
    Test1 = input()
    Test2 = input()
    if(Test1 in Test2) or \
            (Test1[::-1] in Test2):
        print("YES")
    else:
        print("NO")

print("\U0001F49A")

'''
Sample Input
3
hack
indiahacks
code
eddy
coder
iamredoc'''