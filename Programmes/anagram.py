# Check if both the strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters in another word or phrase.

s1 = input("enter first word-  ")
s2 = input("enter second word-  ")
if sorted(s1) == sorted(s2):
    print("The strings are anagrams")
else:
    print("The strings aren't anagrams")