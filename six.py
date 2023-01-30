with open("list.csv") as fo:
  lines = fo.read().splitlines()
  header = lines[0].splitlines()
  data = lines[1:]
  print(list(map(lambda line: dict(zip(header, line.split(","))), data)))