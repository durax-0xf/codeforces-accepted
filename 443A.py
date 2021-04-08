import re
print(len(set(list(re.sub("[^a-zA-Z]+", "", input())))))