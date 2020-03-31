fin = open("latest100matches.txt", "rt")
fout = open("latest100matches.json", "wt")

for line in fin:
#	fout.write(line.replace("'", "\""))
	for r in (("True", '"True"'), ("False", '"False"'), ("'", "\"")):
		line = line.replace(*r)
	fout.write(line)
fin.close()
fout.close()
