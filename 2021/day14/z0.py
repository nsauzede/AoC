def walk(counts):
    counts['B']+=1

counts={'B':0}
walk(counts.copy())
print(counts)
