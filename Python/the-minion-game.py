game = input()

vowels = 'AEIOU'

kevin = 0
stuart = 0
for i in range(len(game)):
    if game[i] in vowels:
        kevin += (len(game)-i)
    else:
        stuart += (len(game)-i)

if kevin > stuart:
    print("Kevin", kevin)
elif kevin < stuart:
    print("Stuart", stuart)
else:
    print("Draw")

