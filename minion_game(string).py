def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    # Loop through each character in the string
    for i in range(length):
        # Number of substrings starting at index i = (length - i)
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    # Determine and print the winner
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)