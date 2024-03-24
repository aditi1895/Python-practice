def longestPalindrome(s: str) -> str:
    dp_array = [[0 for i in range(len(s))] for j in range(len(s))]
    print(dp_array)
    for i in range(len(s)):
        for j in range(len(s)-1,-1,-1):
            print(i,j)
            if i==j:
                print("if")
                print(i,j, dp_array[i][j])
                dp_array[i][j] = 1
            elif s[i] == s[j]:
                print("elif")
                # pass
                dp_array[i][j] = dp_array[i-1][j] * 1
            else:
                print("else")

    print(dp_array)

longestPalindrome("abba")