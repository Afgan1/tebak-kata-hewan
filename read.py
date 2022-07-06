pertanyaan = []


file = open("hewan.txt","r")
list_file = list(file)
long = len(list_file)
#index1 = list_file[0]
#find = index1.index("=")
#place = index1[:-(find)-1]
#delete = index1.replace(place,""), index1.replace("\n","")

#print(find)
#print(place)
#print(delete)
#print(list_file)

for i in range(long):
	#file = open("hewan.txt","r")
	index1 = list_file[i]
	find = index1.index("=")
	place = index1[:(find)+1]
	delete = index1.replace(place,"").replace("\n","")
	finish = delete.strip().lower()
	#print(place)
	#print(finish)
	pertanyaan.append(finish)

file2 = open ("hewan2.txt","r")
list_file2 = list(file2)
long2 = len(list_file2)
#print(list_file2)

for i in range(long2):
	index2 = list_file2[i]
	find2 = index2.index(":")
	place2 = index2[:(find2)+1]
	delete2 = index2.replace(place2,"").replace("\n","")
	finish2 = delete2.lower().strip()
	pertanyaan.append(finish2)
	#print (finish2.index(" "))
#print (pertanyaan)

#a = "kucing terbang"
#print (a.index("l"))
long0 = len(pertanyaan)
print(pertanyaan)
for j in range(long0):
	try:
		pertanyaan[j].index(" ")
	except ValueError:
		continue
	#print (pertanyaan[j])
