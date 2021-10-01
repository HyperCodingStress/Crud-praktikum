import os
import time
import datetime
import random
import csv

waktu = datetime.datetime.now()
jam = int (waktu.strftime("%H"))
menit = int (waktu.strftime("%M"))

print('='*45)
print(' >>>\t Pameran Kendaraan  \t\t<<<')
print (" >>> \t Waktu anda login : ", jam, ":", menit ,"\t<<<" )
print('='*45)

########################################
#databases
user =  [
        {   
            
            "nama":"abel",
            "password":"1",
            "kesempatan":3
        },
        {   
            
            "nama":"ibnu",
            "password":"2",
            "kesempatan":3
    },
        {
            "nama":"nita",
            "password":"3",
            "kesempatan":3
        },
    {
            "nama":"jharmi",
            "password":"4",
            "kesempatan":3
        }
    ]

admin =  [
        {   
            
            "nama":"Admin",
            "password":"Kelompok",
            "kesempatan":3
        }
    ]

############################
#color
def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): 
    print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): 
    print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): 
    print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): 
    print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): 
    print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): 
    print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): 
    print("\033[98m {}\033[00m" .format(skk))

#queue
class Queue:
    def __init__(self):
        self.head = None
        self.last= None
    def enqueue(self, data):
        if self.last is None:
            self.head =Node(data)
            self.last =self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev=self.last
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp= self.head.data
            self.head = self.head.next
            return temp

    def printqueue(self):
        print("~"*20)
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            print("")
            temp=temp.next

    def first(self):
        if self.head.data is None:
            return None
        else:
            return self.head.data
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

#############
#sorting 
def partition(arr, low, high):
	i = (low-1)		 
	pivot = arr[high]	 
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


#fungsi fibonaci search
def searching(isi, x, n):
    fibonaci2 = 0 
    fibonaci1 = 1 
    fibonaci = fibonaci2 + fibonaci1 
    while (fibonaci < n):
        fibonaci2 = fibonaci1
        fibonaci1 = fibonaci
        fibonaci = fibonaci2 + fibonaci1
    offset = -1
    while (fibonaci > 1):
        i = min(offset+fibonaci2, n-1)
        if (isi[i] < x):
            fibonaci = fibonaci1
            fibonaci1 = fibonaci2
            fibonaci2 = fibonaci - fibonaci1
            offset = i
        elif (isi[i] > x):
            fibonaci = fibonaci2
            fibonaci1 = fibonaci1 - fibonaci2
            fibonaci2 = fibonaci - fibonaci1
        else:
            return i
    if(fibonaci1 and isi[n-1] == x):
        return n-1
    return -1

def search():
    n = len(nama_user)
    x = input("Masukan Yang ingin anda cari : ")
    isi = searching(nama_user, x, n)
    if isi >= 0:
        print("Ditemukan di index ke :",isi)
    else:
        print(x,"Tidak ada di list")

######################
## class automobile
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Automobile:
    def __init__(self):
        self._nama = ''
        self._jenis = ''
        self._tahun = 0
        self._warna = ''
        self.head = None
        self.count = 0

    def addLast(self, nodeBaru):
        if self.head is None:
            self.head = Node(nodeBaru)
            self.count += 1
        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = Node(nodeBaru)
            self.count += 1

    def deleteNode(self,position):
        if self.head == None:
            return
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None 
            return 
        
        for i in range (position,-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None :
            return 
        
        if temp.next is None:
            return 
        
        next = temp.next.next 
        temp.next = None
        temp.next = next


    def printList(self):
        if self.head is None:
            print('Data Masih Kosong')
        else:
            nodeTampil = self.head
            while nodeTampil is not None: 
                print('-> ', nodeTampil.data)
                nodeTampil = nodeTampil.next
            print()
        
            
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    
    def search_item(self, val):
            # Search the list
            for node in self.iterate_item():
                if val == node:
                    return True
            return False

    def addVehicle(self):
        try:
            self._nama = input('Masukan Nama Kendaraan ~> ')
            self._jenis = input('Masukan Jenis Kendaraan ~>  ')
            self._tahun = int(input('Masukan Tahun Kendaraan ~>  '))
            self._warna = input('Masukan Warna Kendaraan ~> ')
            nama_kendaraan.addLast(self._nama)
            jenis_kendaraan.addLast(self._jenis)
            tahun_kendaraan.addLast(self._tahun)
            warna_kendaraan.addLast(self._warna)
            proses.enqueue(random.randint(0,200))
            time.sleep(1)
            os.system('cls')
            return True
        except ValueError:
            print('Masukan Tahun Dengan Benar ')
            time.sleep(1)
            os.system('cls')
            return False

    def __str__(self):
        return '\t'.join(str(x) for x in [self._nama, self._jenis, self._tahun, self._warna])

#class inventory
class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            time.sleep(1)
            os.system('cls')
            print ()
            print('Data Kendaraan Telah Dimasukan')
        time.sleep(1)
        os.system('cls')

    def viewInventory(self):
        time.sleep(1)
        os.system('cls')
        print ('~'*40)
        print('\t'.join(['ID','nama', 'jenis','tahun', 'warna']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx , end='\t')
            print(vehicle)
        print ('~'*40)
        time.sleep(1)
    
    def descInventory(self):
        time.sleep(1)
        os.system('cls')
        print ('~'*40)
        jumlah = len(self.vehicles)
        data = []
        print('\t'.join(['ID','nama', 'jenis','tahun', 'warna']))
        for idx, vehicle in enumerate(self.vehicles) : 
            data.append(str(vehicle))
        for i in range(0,len(data)): 
            print(f'{jumlah-i-1}\t{data[len(data)-i-1]}')
        print ('~'*40)
        time.sleep(1)   

def menu_awal():
    while True:
        print("="*40)
        prGreen ('>>>\t1. Login User\t\t<<<')
        prPurple ('>>>\t2. Login Admin\t\t<<<')
        prCyan ('>>>\t3. Register Akun User\t<<<')
        prRed ('>>>\t4. Exit\t\t\t<<<')
        print("="*40)
        pilih = input('Masukan Pilihan ~> ')
        if pilih == "1":
            login_user()
        elif pilih == "2":
            login_admin()
        elif pilih == "3":
            register()
        elif pilih == '4':
            time.sleep(0.5)
            os.system('cls')
            print('='*45)
            print(' >>>\t TerimaKasih  \t\t\t<<<')
            print (" >>> \t Waktu anda Keluar : ", jam, ":", menit ,"\t<<<" )
            print('='*45)
            raise SystemExit
        else:
            print('Pilihan hanya ada 1-4')

def login_user():
    while True:
        time.sleep(1)
        os.system('cls')
        login = input("Enter Nama ~> ")
        login1 = input("Enter Password ~>")
        for each in user:
            if login in each["nama"] and login1 in each ["password"] and each["kesempatan"] >= 1:
                time.sleep(1)
                os.system('cls')
                print ("logged")
                time.sleep(1)
                os.system('cls')
                print("Hallo ",each['nama'])
                time.sleep(1)
                os.system('cls')
                menu_user()
        else:
            if each["kesempatan"] <= 1 :
                print ("Kesempatan Anda 0 Silahkan Hub Database Administrator")
                raise SystemExit
            else:
                print("Masukan Nama Dan Password Dengan Benar ")
                each["kesempatan"] -= 1
                print("Kesempatan Anda tersisa : ", each["kesempatan"])

def login_admin():
    while True:
        login = input("Enter Nama ~> ")
        login1 = input("Enter Password ~>")
        if login in admin[0]["nama"] and login1 == 'Kelompok' and admin[0]["kesempatan"] >= 1:
            time.sleep(1)
            os.system('cls')
            print ("logged")
            time.sleep(1)
            os.system('cls')
            print("Hallo ",admin[0]['nama'])
            time.sleep(1)
            os.system('cls')
            menu_admin()
        else:
            if admin[0]["kesempatan"] <= 1 :
                print ("Kesempatan Anda 0 Silahkan Hub Database Administrator")
                raise SystemExit
            else:
                print("Masukan Nama Dan Password Dengan Benar")
                admin[0]["kesempatan"] -= 1
                print("Kesempatan Anda tersisa : ", admin[0]["kesempatan"])
            
def register():
    time.sleep(1)
    os.system('cls')
    nama = input('Masukan Nama Baru ~> ')
    password = input('Masukan Password Baru ~> ')
    user.append(
        {
        'nama':(nama),
        'password':(password),
        "kesempatan":3}
    )
    nama_user.append(nama)
    time.sleep(1)
    os.system('cls')
    menu_awal()
###########################################
#llist

inventory = Inventory()
nama_kendaraan = Automobile()
jenis_kendaraan = Automobile()
tahun_kendaraan = Automobile()
warna_kendaraan = Automobile()
proses = Queue()
nama_user = []

for i in user:
    i = i["nama"]
    nama_user.append(i)
###########################################
def menu_user():
    while True:
        print("="*45)
        prYellow('>>>\t1 Liat Kendaraan Di Showroom\t<<<')
        prCyan('>>>\t2 Cari Nama Kendaraan\t\t<<<')
        prRed('>>>\t3 Kembali\t\t\t<<<')
        print("="*45)
        pilihan=input('Masukan pilihan ~>  ') 
        if pilihan == '1':
            time.sleep(1)
            os.system('cls')
            if len(inventory.vehicles) < 1:
                    print('Data Kendaraan Di Showroom Masih Kosong')
                    time.sleep(1)
                    os.system('cls')
                    continue
            time.sleep(0.5)
            os.system('cls')
            print("="*50)
            print(">>>\t1.Lihat Data Kendaraan Secara ASC\t<<<")
            print(">>>\t2.Lihat Data Kendaraan Secara DESC\t<<<")
            print("="*50)
            pilihan = input ("Pilih Menu : ")
            if pilihan == "1":
                inventory.viewInventory()
            elif pilihan == "2":
                inventory.descInventory()
        elif pilihan == '2':
            time.sleep(1)
            os.system('cls')
            print("="*45)
            prPurple ('>>>\t1.Berdasarkan Nama\t<<<')
            prPurple ('>>>\t2.Berdasarkan Jenis\t<<<')
            prPurple ('>>>\t3.Berdasarkan Warna\t<<<')
            prPurple ('>>>\t4.Berdasarkan Tahun\t<<<')
            print("="*45)
            pilih = input("Masukan Pilihan Nomor  : ")
            time.sleep(1)
            os.system('cls')
            if pilih == '1':
                time.sleep(1)
                os.system('cls')
                x = input("Masukan Nama : ")
                if nama_kendaraan.search_item(x):
                    print("Nama Kendaraan",x,"Ditemukan")
                else:
                    print("Nama Kendaraan",x,"Tidak Ditemukan")
            elif pilih == '2':
                time.sleep(1)
                os.system('cls')
                x = input("Masukan Jenis : ")
                if jenis_kendaraan.search_item(x):
                    print("Jenis Kendaraan",x,"Ditemukan")
                else:
                    print("Jenis Kendaraan",x,"Tidak Ditemukan")
            elif pilih == '3':
                time.sleep(1)
                os.system('cls')
                x = input("Masukan Warna : ")
                if warna_kendaraan.search_item(x):
                    print(" Warna Kendaraan",x,"Ditemukan")
                else:
                    print("Warna  Kendaraan",x,"Tidak Ditemukan")
            elif pilih == '4':
                time.sleep(1)
                os.system('cls')
                while True:
                    try:
                        x = int(input("Masukan Tahun : "))
                        break
                    except ValueError:
                        print("Masukan Menggunakan Angka")
                if tahun_kendaraan.search_item(x):
                    print("Tahun Kendaraan",x,"Ditemukan")
                else:
                    print("Tahun Kendaraan",x,"Tidak Ditemukan ")
            else:
                print("Pilihan Hanya ada 1-4")
        elif pilihan == '3':
            time.sleep(1)
            os.system('cls')
            menu_awal()
        else:
            time.sleep(1)
            os.system('cls')
            prRed('Nomor Tidak Valid.Masukan Kembali')

def menu_admin():          
    while True:
        prRed('='*50)
        with open('menu.txt') as file:
            reader = csv.reader(file)
            for row in reader:
                prLightPurple(row)
        prRed('='*50)
        pilihan=input('Masukan pilihan ~>  ') 
        if pilihan=="1":
            time.sleep(0.5)
            os.system('cls')
            inventory.addVehicle()
        elif pilihan=='2':
            if len(inventory.vehicles) < 1:
                time.sleep(0.5)
                os.system('cls')
                print('Data  Kendaraan Di Showroom Masih Kosong')
                time.sleep(0.5)
                os.system('cls')
                continue
            inventory.viewInventory()
            while True:
                try:
                    item = int(input('Masukan ID Berapa Yang Ingin Dihapus: '))
                    break
                except ValueError:
                    print("Input Dengan Nomor ")
            if item + 1  > len(inventory.vehicles):
                print('Nomor invalid')
            else:
                inventory.vehicles.remove(inventory.vehicles[item])
                nama_kendaraan.deleteNode(item)
                tahun_kendaraan.deleteNode(item)
                jenis_kendaraan.deleteNode(item)
                warna_kendaraan.deleteNode(item)
                time.sleep(0.5)
                os.system('cls')
                print ()
                print('Kendaraan Telah Dihapus')
                time.sleep(0.5)
                os.system('cls')
        elif pilihan == '3':
            if len(inventory.vehicles) < 1:
                time.sleep(0.5)
                os.system('cls')
                print('Data  Kendaraan Di Showroom Masih Kosong')
                time.sleep(1)
                os.system('cls')
                continue
            time.sleep(0.5)
            os.system('cls')
            print("="*50)
            print(">>>\t1.Lihat Data Kendaraan Secara ASC\t<<<")
            print(">>>\t2.Lihat Data Kendaraan Secara DESC\t<<<")
            print("="*50)
            pilihan = input ("Pilih Menu : ")
            if pilihan == "1":
                inventory.viewInventory()
            elif pilihan == "2":
                inventory.descInventory()
        elif pilihan == '4':
            if len(inventory.vehicles) < 1:
                time.sleep(0.5)
                os.system('cls')
                print('Data Kendaraan Di Showroom Masih Kosong')
                time.sleep(0.5)
                os.system('cls')
                continue
            inventory.viewInventory()
            while True:
                try:
                    item = int(input('Masukan Nomor Berapa Yang Ingin Diupdate: '))
                    break
                except ValueError:
                    print("Input Dengan Nomor ")
            time.sleep(0.5)
            os.system('cls')
            if item + 1  > len(inventory.vehicles):
                print('Nomor invalid')
            else:
                automobile = Automobile()
                if automobile.addVehicle() == True :
                    inventory.vehicles.remove(inventory.vehicles[item])
                    nama_kendaraan.deleteNode(item)
                    tahun_kendaraan.deleteNode(item)
                    jenis_kendaraan.deleteNode(item)
                    warna_kendaraan.deleteNode(item)
                    inventory.vehicles.insert(item , automobile)
                    time.sleep(0.5)
                    os.system('cls')
                    print ()
                    print('Data Kendaraan Telah Di Update')
                    time.sleep(0.5)
                    os.system('cls')
        elif pilihan == '5':
            time.sleep(1)
            os.system('cls')
            print("="*50)
            print(">>>\t1. Menampilkan user secara ASC\t<<<")
            print(">>>\t2. Menampilkan user secara DESC\t<<<")
            pilih = input ("Masukan Pilihan : ")
            print("="*50)
            if pilih == '1':
                time.sleep(0.5)
                os.system('cls')
                print("="*20)
                print("Database User")
                n = len(nama_user)
                quickSort(nama_user, 0, n-1)
                for x in nama_user:
                    print("~>",x)
                print("="*20)
                print("=> ENTER")
                input("")
                time.sleep(0.5)
                os.system('cls')
            elif pilih == '2':
                time.sleep(0.5)
                os.system('cls')
                print("="*20)
                print("Database User")
                n = len(nama_user)
                quickSort(nama_user, 0, n-1 )
                for i in range(0, len(nama_user)) :
                    nama_user[i] = (nama_user[i])
                    nama_user.sort(reverse = True)
                for x in nama_user:
                    print("~>",x)
                print("="*20)
                print("=> ENTER")
                input("")
                time.sleep(0.5)
                os.system('cls')
            else:
                time.sleep(0.5)
                os.system('cls')
                print("Pilih hanya ada 1-2")
        elif pilihan == '6':
            os.system('cls')
            time.sleep(0.5)
            search()
        elif pilihan == "7":
                time.sleep(0.5)
                os.system('cls')
                try:
                    print("Id ", proses.first(), "Yang Sedang Di Proses")
                    proses.dequeue()
                    print("ID yang Ditunggu : ", proses.first())
                    print("Enter")
                    input("")
                    time.sleep(1)
                    os.system('cls')
                except AttributeError:
                    print("Tidak Ada Atrian Lagi")
                    input("")
                    time.sleep(1)
                    os.system('cls')
                finally:
                    print("Kembali")
                    time.sleep(1)
                    os.system('cls')
        elif pilihan == '8':
            time.sleep(0.5)
            os.system('cls')
            menu_awal()
        elif pilihan == '9':
            time.sleep(0.5)
            os.system('cls')
            print('='*45)
            print(' >>>\t TerimaKasih  \t\t\t<<<')
            print (" >>> \t Waktu anda Keluar : ", jam, ":", menit ,"\t<<<" )
            print('='*45)
            raise SystemExit
        else:
            time.sleep(0.5)
            os.system('cls')
            prRed('Nomor Tidak Valid.Masukan Kembali')

menu_awal() 