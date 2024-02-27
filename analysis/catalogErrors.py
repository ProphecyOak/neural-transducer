import sys
import re

with open("../checkpoints/sig23/tagtransformer/fra.decode.dev.tsv") as f:
    contents = f.read()

lines = contents.strip().split("\n")
columns = []
for line in lines[1:]:
    columns.append(line.replace(" ","").split("\t"))

errorColumns = list(filter(lambda x: x[3] != '0', columns))
errorColumns.sort(key=lambda x: x[3],reverse=True)

with open("errors.tsv","w") as e:
    e.write(lines[0]+"\n")
    for row in errorColumns:
        e.write("\t".join(row)+"\n")