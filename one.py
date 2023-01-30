from collections import defaultdict

with open("textfile.txt") as fo:
    for line in fo:
      line_d = defaultdict(int)
      for word in line.split():
          w_len = len(word)
          line_d[w_len] = line_d[w_len] + 1