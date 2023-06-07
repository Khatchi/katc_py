#!/usr/bin/python3
katc_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("How enthusiatic(1-10): "))
a = 0
while a < len(word):
    char = word[a]
    if char in katc_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    a += 1
print("What does that spell?")
for a in range(times):
    print(word, "!!!")
