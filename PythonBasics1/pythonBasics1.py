# Python Activtiy
# 
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. starts_with
# Define a function starts_with(s, char) that takes a string and a character
# and returns true if the string starts with that character and false otherwise.
def starts_with(s,char):
  if s[0:1] == char:
    return True
  else:
    return False

  return

# Part B. starts_with_vowel
# Define a function starts_with_vowel(s) that takes a string and
# returns true if the string starts with a vowel and false otherwise. 
# For our purposes, a consonant is any letter other than A, E, I, O, U)
# Your solution should work for both upper and lower cases 
def starts_with_vowel(s):
  if s[0:1] == 'a' or s[0:1] == 'e' or s[0:1] == 'i' or s[0:1] == 'o' or s[0:1] == 'u' or s[0:1] == 'A' or s[0:1] == 'E' or s[0:1] == 'I'or s[0:1] == 'O' or s[0:1] == 'U':
    return True
  else:
    return False

  return

# Part C. max_min_sum
# Define a function max_min_sum(arr) that takes an array and returns the sum
# of the largest element and the smallest element of the array.
# For an empty array it should return zero
# For an array with just one element, it should return that element
def max_min_sum(arr):
  if arr == []:
    return 0
  elif len(arr) == 1:
    return arr[0]
  else:
    return max(arr) + min(arr)
  
  return