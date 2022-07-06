import random
from read import *
import os

os.system("clear")
print ("Tebak Kata")
poin = 0
while True:
	jawaban = random.choice(pertanyaan)
	random_raw = random.sample(jawaban,len(jawaban))
	random1 = "-".join(random_raw)
	#pertanyaan
	print (random1)
	#menjawab
	jawab = input("jawab: ")
	if jawab == jawaban:
		print ("\njawaban anda benar, poin +1")
		poin += 1
	else:
		print (f"\njawaban adalah {jawaban}, poin -1")
		poin -= 1
	print (f"\npoin anda {poin}\n")
	if poin == -1:
		print("anda kalah")
		break
	elif poin == 20:
		print ("ANDA MENANG\n")