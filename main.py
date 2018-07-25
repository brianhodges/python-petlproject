import petl
from language import Language

filename = 'languages.csv'
csv = petl.fromcsv(filename)
languages = []

print
print("PETL Table")
print("----------")
x = 0
for row in petl.skip(csv,1):
	if x < 5:
		print(row)
		x += 1
		
for row in petl.skip(csv,1):
	languages.append(Language(row))

print
print("Languages Array")
print("----------------")
print(languages)
	
print
print("PROOF")
print("-----")
for l in languages:
	print("Name: " + str(l.programming_language))
print