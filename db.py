import _sqlite3

# tablo bağlantısı kurma ve işaretci oluşturma
#con = _sqlite3.connect("Users.db")
#cursor=con.cursor()

def createTable(): #tablo oluşturma attribute'ları belirleme
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS ("
                   "userID INT PRIMARY KEY NOT NULL, "
                   "uName TEXT NOT NULL, "
                   "uMail TEXT,"
                   "uPassword TEXT NOT NULL,"
                   "authorized BOOL NOT NULL, "
                   "verifyCode INT(6))")
    con.commit()
    con.close()

def createUser(userID,name,mail,password,authorized,verifyCode): #yetkili kullanicinin id'si 1 diğerleri sıralı olmalı
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO USERS (userID,uName,uMail,uPassword,authorized,verifyCode) VALUES(?,?,?,?,?,?) ",(userID,name,mail,password,authorized,verifyCode))
    con.commit()
    con.close()

def fetch(id,req): #userID ye göre istenilen degeri döndürür
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("SELECT "+req+" FROM USERS WHERE userID == "+id+"")
    data=cursor.fetchall()
    request=data[0][0] # data değişkenin tipi list. listenin ilk elemani aradigimiz deger
    con.close
    return request

def updateInfo(id,changeX,changeY): #girilen id'nin changeX attribute'undaki değerini changeY ile değiştirir veriler dogru girilmeli

    if(changeX == "authorized"):#yetki değerleri degistirilemez
        print("izin verilmeyen durum..")
    else:
        con = _sqlite3.connect("Users.db")
        cursor = con.cursor()
        cursor.execute("UPDATE USERS SET '{}' = '{}' WHERE userID=='{}'".format(changeX,changeY,id))
        con.commit()
        con.close()

def deleteUser(id):#kullanici silme
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    if(isAuthorized(id)!=1):#yetkili kullanici silinemez
        cursor.execute("DELETE FROM USERS WHERE userID== '{}'".format(id))
        con.commit()
        con.close()
    else:
        print("islem basarisiz..")

def isAuthorized(id): #kulanıcının yetki durumunu döndürür
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("SELECT authorized FROM USERS WHERE userID == " + id + "")
    data = cursor.fetchall()
    response = data[0][0]
    con.close()
    return response
#yüz verilerinin kişilerle eşleşmesi için id değerlerinin 1 ile 5 arasında değerler olması gerek
def genereteID(): #id üretme fonksiyonu
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("SELECT userID FROM USERS")
    data = cursor.fetchall()#bütün userID'ler data listesinin içerisine atıldı fakat bu liste bize uygun degil

    i=1
    IDs=[]#yeni id listemiz
    for i in range(len(data)):#data listesindeki bütün id ler istedigimiz formda IDs listesine atılıyor
        IDs.append(data[i][0])
    IDs.sort() #taramada avantaj saglanması icin liste siralandi

    id=1 #deger değişmemeli min id=1 max id =5 olmalı
    i=0
    for i in range(len(IDs)):#1'den 5'e kadar gezip liste içerisinde eksik olan ilk degeri bulur
        if id in IDs:
            id=id+1
        else:
            break
    con.close()
    return id

def isUserInTable(): #tablo içerisinde kullanıcı var mı?
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("SELECT userID FROM USERS")
    data=cursor.fetchall()
    con.close()
    if data:
        return True
    else :
        return False

def totalUserInTable(): #toplam kullanıcı sayısını döndürür
    con = _sqlite3.connect("Users.db")
    cursor = con.cursor()
    cursor.execute("SELECT userID FROM USERS")
    data = cursor.fetchall()
    con.commit()
    con.close()
    return len(data)



#createTable()
#createUser(genereteID(),"Volkan","2@hotmail.com","0123456789",True,"")
#print(fetch("1","uName"))
#print(totalUserInTable())
#deleteUser("5")
#updateInfo("3","uName","kursat")
#newPass="asdae"
#updatePassword(newPass,"1")
