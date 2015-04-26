"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'azcbobobegghakl'

longest1=''
longest2=''

for i in range(len(s)):
    if s[i]<=s[i+1]:
        longest1+=s[i+1]
    elif s[i]>s[i+1]:
        longest2+=s[i+1]
        
    if len(longest1)>=len(longest2):
        longest=longest1
    else:
        longest=longest2
print 'Longest substring in alphabetical order is:: '+longest