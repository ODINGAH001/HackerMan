#python3

is_pangram = lambda s: not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
if is_pangram(input()):
    print("pangram")
else:
    print("not pangram")
