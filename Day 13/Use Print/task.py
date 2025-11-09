"""
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

-- Assign Operator '=' and equality operator '=='
-- has a huge difference, hence print(total_words)
-- didn't worked as in line 4 it didn't assigned
-- but valued an equality to the term which was undiscovered.

-- No need to inititalise wpp as 0 (line 2)
"""

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
