#String
s = "hello"

#String indexing
s = "python"
print(s[0])   # p
print(s[-1])  # n

#String traversal
s = "python"
for ch in s:
    print(ch)

#length of the string
s = "python"
print(len(s))  # 6

#Reverse a string
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#click palindrome
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#count vowels
s = "education"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
#count each character
s = "apple"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

#check two strings are equal
s1 = "hello"
s2 = "hello"

if s1 == s2:
    print("Equal")
else:
    print("Not Equal")

