import operator
import os
import time
import datetime
from datetime import datetime as date

# Logovanje korisnika
def login():
	global username
	storekeeper = open('magacioneri.txt','r').readlines()
	username = input("\nUnesite korisnicko ime: ")
	password = input("Unesite lozinku: ")
	attempt = 0
	for i in storekeeper:
		storekeeper=i.strip("\n").split(":")
		if (username==storekeeper[0] and password==storekeeper[1] and attempt<3): #Proverava unetu sifru sa sifrom iz tekstualnog fajla
			print("\nUlogovao se korisnik: " + storekeeper[0]+ "\n" + storekeeper[2].title(), storekeeper[3].title())
			meni()
			attempt=+1
	login()
	if attempt>3: #Ako korisnik ne uspe da se uloguje posle 3 pokusaja, program se prekida
		print("error")
		exit()

#Korisniku se prikazuje meni
def meni():
	opcije = input('\n   ====== MENI ======\n1. Prikaz stanja lagera\n2. Pretraga magacina\n3. Izdavanje uredjaja\n4. Unos uredjaja\n5. Izvestaji\n6. Izloguj se\n7. Kraj rada\n\nIzaberite opciju:')
	if opcije == '1':
		prikaz_stanja_lagera()
	if opcije == '2':
		pretraga_uredjaja()
	if opcije == '3':
		iznos_uredjaja()
	if opcije == '4':
		unos_uredjaja()
	if opcije == '5':
		izvestaji()
	if opcije == '6':
		login()
	if opcije == '7':
		exit()
	else:
		meni()

# Funkcija sluzi za pregledniji ispis
def formatheader():
	print()
	print(
"Sifra|    Naziv    |  Proizvodjac  |       Opis       |   Kolicina   |\n"
"-----+-------------+---------------+------------------+--------------|")

#########################################
#########################################
#########################################
#########################################
#########################################

#Korisniku se, ukoliko izabere prvu opciju, ispisuje podmeni
def prikaz_stanja_lagera():
	opcije = input('===== PRIKAZ STANJA NA LAGERU =====\n1. Sortiraj po sifri\n2. Sortiraj po nazivu\n3. Sortiraj po proizvodjacu\n4.Povratak na glavni meni\n\nIzaberite opciju:')
	if opcije == '1':
		sortiraj_sifru()
	if opcije == '2':
		sortiraj_naziv()
	if opcije == '3':
		sortiraj_proizvodjaca()
	if opcije == '4':
		meni()
	else:
		prikaz_stanja_lagera()

#U podmeniju korisniku se sortiraju uredjaji po sifri
def sortiraj_sifru():
	device_file = open('uredjaji.txt', 'r')
	formatheader()
	devices = []
	for line in device_file:
		devices.append([i  for i in line.strip("\n").split(":")])
	devices.sort(key=lambda x:x[0])
	for device in devices:
		if device[4] > '0':
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
	print()
	meni()

#Korisniku se uredjaji sortiraju po nazivu
def sortiraj_naziv():
	device_file = open('uredjaji.txt', 'r')
	formatheader()
	devices = []
	for line in device_file:
		devices.append([i  for i in line.strip("\n").split(":")])
	devices.sort(key=lambda x:x[1])
	for device in devices:
		if device[4] > '0':
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
	print()
	meni()

#Uredjaji se sortiraju po proizvodjacu
def sortiraj_proizvodjaca():
	device_file = open('uredjaji.txt', 'r')
	formatheader()
	devices = []
	for line in device_file:
		devices.append([i  for i in line.strip("\n").split(":")])
	devices.sort(key=lambda x:x[2])
	for device in devices:
		if device[4] > '0':
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
	print()
	meni()

#########################################
#########################################
#########################################
#########################################
#########################################

#Korisniku se ispisuje novi podmeni
def pretraga_uredjaja():
	opcije = input('\n===== PRETRAGA UREDJAJA =====\n1. Pretraga po sifri\n2. Pretraga po nazivu\n3. Pretraga po proizvodjacu\n4.Povratak na glavni meni\n\nIzaberite opciju:')
	if opcije == '1':
		pretrazi_sifru()
	if opcije == '2':
		pretrazi_naziv()
	if opcije == '3':
		pretrazi_proizvodjaca()
	if opcije == '4':
		meni()
	else:
		pretraga_uredjaja()

#Korisnik unosi sifru po kojoj bi zeleo da pretrazi magacin gde mu se izbacuje uredjaj sa unesenom sifrom
def pretrazi_sifru():
	device_file = open('uredjaji.txt', 'r')
	sifra = input("Unesite sifru: ")
	formatheader()
	for i in device_file:
		device = i.strip("\n").split(":")
		if sifra == device[0]:
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
			break
	if sifra != device[0]:
		print ('Ne postoji uredjaj sa unetom sifrom!')
	pretraga_uredjaja()

#Prolazi se kroz tekstualni fajl gde se uneti naziv uporedjuje sa nazivom iz fajla
def pretrazi_naziv():
	device_file = open('uredjaji.txt', 'r').readlines()
	naziv = input("Unesite naziv: ").lower()
	formatheader()
	for i in device_file:
		device = i.strip("\n").split(":")
		if naziv in device[1].lower():
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
	pretraga_uredjaja()

# Funkcija radi na istom principu kao i prethodna, samo sto se odnosi na proizvodjace
def pretrazi_proizvodjaca():
	device_file = open('uredjaji.txt', 'r').readlines()
	producer = input("Unesite naziv proizvodjaca: ").lower()
	formatheader()
	for i in device_file:
		device = i.strip("\n").split(":")
		if producer in device[2].lower():
			print("{0:5}|{1:13}|{2:15}|{3:18}|{4:5}".format(    
				device[0],
				device[1],
				device[2],
				device[3],
				device[4]))
	pretraga_uredjaja()

#########################################
#########################################
#########################################
#########################################
#########################################

#Korisnik unosi sifru i kolicinu uredjaja koji iznosi iz magacina
def iznos_uredjaja():
	code = input("Unesite sifru uredjaja: ")
	amount = int(input("Koliko uredjaja iznosite: "))
	with open("uredjaji.txt", "r+") as f:
		current_position = 0 #Trenutna pozicija u fajlu
		line = f.readline()
		while line:
			if line[:len(code) + 1] == code + ":":
				line = line.rstrip()  # Brise prazna mesta
				amount_index = line.rfind(":") + 1 #Nalazi indeksnu poziciju
				current_amount = int(line[amount_index:]) #Prikazuje kolicinu	
				if (amount > current_amount):
					print("Nema toliko uredjaja na lageru.")
					return #Ne dozvoljava da se iz magacina iznese vise uredjaja nego sto ima
				remaining_content = f.read()
				f.seek(current_position) #Vraca se na trenutnu poziciju
				f.truncate() #Brise ostatak fajla ukljucujuci trenutnu liniju
				line = line[:amount_index] + str(current_amount - amount) + "\n"
				f.write(line) #Upisuje u fajl
				f.write(remaining_content) #Upisuje novu vrednost uredjaja
				with open('transakcije.txt') as transactions:
					index= sum(1 for _ in transactions)+1
					transactions.close() #Izvlaci se indeks da bi se moglo upisati u transakcije
				with open('transakcije.txt','a+') as transactions:
					date = datetime.date.today().strftime('%d.%m.%Y.')
					transactions.write(str(index) + ":" + str(code) + ":" + str(amount) + ":" + "iznos" + ":" + str(date) + ":" + username + "\n")
					transactions.close() #Unosi se transakcija i zatvara taj fajl
				return #Vraca novu vrednost
			current_position = f.tell()
			line = f.readline()
	print("Ne postoji uredjaj sa unetom sifrom: {}".format(code))

#Isti je princip kao sa prethodnom funkcijom, samo sto se sada unosi jedan uredjaj
def unos_uredjaja():
	code = input("Unesite sifru uredjaja: ")
	amount = int(input("Koliko uredjaja dodajete: "))
	with open("uredjaji.txt", "r+") as f:
		current_position = 0  
		line = f.readline()
		while line:
			if line[:len(code) + 1] == code + ":":  
				remaining_content = f.read()  
				f.seek(current_position) 
				f.truncate()  
				line = line.rstrip()  
				amount_index = line.rfind(":") + 1
				current_amount = int(line[amount_index:])  
				line = line[:amount_index] + str(current_amount + amount) + "\n"
				f.write(line)  
				f.write(remaining_content)  
				return  
			current_position = f.tell()  
			line = f.readline()  
		print("Invalid device code: {}".format(code))
		if code not in f:
			print("\nNe postoji uredjaj sa unetom sifrom: {}".format(code)+"\n"+"Dodavanje uredjaja.\n")
			device_name=input("Unesite naziv uredjaja: ")
			device_producer=input("Unesite naziv proizvodjaca: ")
			device_description=input("Unesite kratki opis uredjaja: ")
			if (len(device_name)==0 or len(device_producer)==0 or len(device_description)==0):
				print("\nNaziv, proizvodjac i opis uredjaja su obavezni za unos! Pokusajte ponovo.")
				unos_uredjaja()
			f.write(str(code) + ":" + str(device_name) + ":" + str(device_producer) + ":" + str(device_description) + ":" + str(amount) + "\n")
			f.close()	
			with open('transakcije.txt') as transactions:
				index= sum(1 for _ in transactions)+1
				transactions.close() 
			with open('transakcije.txt','a+') as transactions:
				date = datetime.date.today().strftime('%d.%m.%Y.')
				transactions.write(str(index) + ":" +str(code) + ":" + str(amount) + ":" + "unos" + ":" + str(date) + ":" + username + "\n")
			print("Uredjaj uspesno dodat")

			
#########################################
#########################################
#########################################
#########################################
#########################################




#Korisnik otvara novi podmeni
def izvestaji():
	opcije= input('\n    ===== IZVESTAJI =====\n1. Izlistavanje po datumima\n2. Izvestaji po magacionerima\n\nIzaberite opciju: ')
	if opcije == '1':
		izvestaj_datum()
	if opcije == '2':
		izvestaj_magacioneri()
	else:
		izvestaji()

#Korisnik unosi pocetni i krajnji datum gde mu se u okviru tog vremena ispisuju transakcije
def izvestaj_datum():
	start_date = input("Unesite pocetni datum (format: dan.mesec.godina.): ")
	try:
		date1 = date.strptime(start_date, "%d.%m.%Y.")
	except:
		print("Pogresno unet datum.")
		izvestaj_datum()
	end_date = input("Unesite krajnji datum datum: ")
	try:
		date2 = date.strptime(end_date, "%d.%m.%Y.")
	except:
		print("Pogresno unet datum.")
		izvestaj_datum()
	if date1 > date2:
		print("Pogresno unet datum:")
		izvestaj_datum()
	elif date1 < date2:
		print("\n===Transakcije u datom vremenskom periodu===")
		with open('transakcije.txt') as f:
			for line in f:
				l_date = date.strptime(line.split(':')[4], "%d.%m.%Y.")
				if date1 <= l_date <= date2:
					print (line)	
login()