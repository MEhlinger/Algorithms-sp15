# Anagram Test Algorithm
# by Marshall Ehlinger
# For Matt Haner's 2015 Analysis of Algorithms

# Simple algorithm for checking whether two input strings are anagrams


strVals1 = []
strVals2 = []
str1 = raw_input("Enter first string: ")
str2 = raw_input("Enter second string: ")
if len(str1) != len(str2):
	print "Not anagrams... differing lengths."
else:
	for i in range (0, len(str1)):
		strVals1.append(ord(str1[i]))
		strVals2.append(ord(str2[i]))
	strVals1 = sorted(strVals1)
	strVals2 = sorted(strVals2)
	if strVals1 != strVals2:
		print "Not an anagram."
	else:
		print "An anagram!"