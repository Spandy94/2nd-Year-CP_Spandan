# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

chars = 256
def areAnagrams(s1, s2):
    # Your code goes here...
    count1 = [0]*chars
    count2 = [0]*chars

    for i in s1:
        count1[ord(i)] += 1

    for i in s2:
        count2[ord(i)] += 1

    if len(s1) != len(s2):
        return 0

    for i in range(chars):
        if count1[i] != count2[i]:
            return 0
    return 1




# write your test cases here...