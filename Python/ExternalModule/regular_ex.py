# For deeper understand to this topic go to :-  regexr.com

import re     # No need to install any package to import this
text = "The quick brown fox jumps over the lazy dog. brown fox"

# Search for a pattern (Only first occurance of brown not give the data of second occurance)
match = re.search("brown", text)
print(match)
if match:
    print("Match Found")
    print("Start Index:", match.start())
    print("End Index:", match.end())


# Find all occurrences of a pattern
matches = re.findall("the", text, re.IGNORECASE)  # Case insenstive search
print("Matches:", matches)


# Replace all occurrences of a pattern
new_text = re.sub("fox", "cat", text)
print("New text:", new_text)