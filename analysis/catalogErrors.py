import sys
import re

def sortOutErrors(fileToCheck="test", sortFunction=lambda x: x[0], language="fra"):
    with open(f"../checkpoints/sig23/tagtransformer/{language}.decode.{fileToCheck}.tsv") as f:
        contents = f.read()

    lines = contents.strip().split("\n")
    columns = []
    for line in lines[1:]:
        columns.append(line.replace(" ","").split("\t"))

    errorColumns = list(filter(lambda x: x[3] != '0', columns))
    if fileToCheck == "test": fileToCheck = "tst"  #Because for whatever reason, neural_transducer doesnt use same extension formatting :/
    with open(f"../../2023InflectionST/part1/data/{language}.{fileToCheck}") as dat, open(f"errors.{language}.{fileToCheck}.tsv","w") as e, open(f"unexpectedForms.{language}.{fileToCheck}.tsv","w") as u:
        lemmaDict = {}
        e.write("lemma\t"+lines[0]+"\n")
        u.write(lines[0]+"\n")
        for form in dat.read().strip().split("\n"):
            splitForm = re.split(r"\s+",form)
            lemmaDict[splitForm[2]] = splitForm[0]
        reducedErrorColumns = []
        for line in errorColumns:
            try:
                line.insert(0,lemmaDict[line[1]])
                reducedErrorColumns.append(line)
            except:
                u.write("\t".join(line)+"\n")
        reducedErrorColumns.sort(key=sortFunction)
        for line in reducedErrorColumns:
            if len(line) == 5: e.write("\t".join(line)+"\n")

sortByDistance = lambda x: -1*int(x[4])
sortByLemma = lambda x: x[0]

if __name__ == "__main__":
    sortOutErrors("test", sortByLemma)