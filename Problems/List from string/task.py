def isPalindrome(input):
    for x in range(0, int(len(input) / 2)):
        if input[x] != input[len(input) - 1 - x]:
            print("False")


print("True")

isPalindrome("maxam")
