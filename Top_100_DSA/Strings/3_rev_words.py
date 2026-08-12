def rev_words(s):
    words = s.split()
    return " ".join(reversed(words))

s = "I Love That One"
print(rev_words(s))   # One That Love I