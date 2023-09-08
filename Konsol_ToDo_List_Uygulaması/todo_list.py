import os
from datetime import datetime

todolists = []


def todoListTespitEtme():
    dizin_yolu = "C:\\OkanMert-ÇalışmaKlasör\\PythonProjects\\Konsol_ToDo_List_Uygulaması"

    for dosya in os.listdir(dizin_yolu):
        if dosya.endswith(".txt"):
            yeniDosya = dosya[:-4]  # Son 4 karakteri sil
            todolists.append(yeniDosya)

öncelikAtma = ["DÜŞÜK","ORTA","YÜKSEK"]
def toDoListOluşturma():
    print("----ToDoList Oluşturma----")
    #Kullanıcıdan bilgiler alınıyor. 

    todoListBaslik = input("Todolist için bir kısa bir konu başlığı yazınız :  ") #Hem başlık hem de todolist adı

    todoListAtananKisi = input("ToDoList kimin için oluşturuluyor : ")

    item = input("Öncelik Atama Seçin (Düşük = 1 , Orta = 2 , Yüksek = 3) : ")
    todoListAtamaÖnceliği = ""
    if item == "1":
        todoListAtamaÖnceliği = öncelikAtma[0]
    elif item == "2":
        todoListAtamaÖnceliği = öncelikAtma[1]
    elif item == "3":
        todoListAtamaÖnceliği = öncelikAtma[2]
    else:
        todoListAtamaÖnceliği = "NONE"
        print("Geçerli bir değer giriniz. Daha sonra düzeltme seçeneği ile değiştirilebilir. ")

    todoListIcerikKullaniciGirisi = input("ToDoList için içeriğini giriniz (Sadece 40 karakter ile sınırlıdır. ) : ")
    todoListIcerik = todoListIcerikKullaniciGirisi[:40]

    todoListSontarih = {
        "Gün" : "00",
        "Ay"  : "00",
        "Yıl" : "0000"
    }
 
    print("Son tarih bilgisini giriniz.(Not : Bu bilgiyi değiştiremiyeceksiniz.)")
    todoListSontarih["Gün"] = input("Son tarih  gün bilgisini giriniz : ")
    todoListSontarih["Ay"] = input("Son tarih ay bilgisi giriniz : ")
    todoListSontarih["Yıl"] = input("Son tarih yıl bilgisini giriniz : ")

    #Alınan bilgiler sayesinde dosya oluşturuluyor.
    
    try:
        metinDosyasiOlusturma = "{}.txt".format(todoListBaslik)    
        todoListDosya = open(metinDosyasiOlusturma,"x",encoding="utf-8")
    except FileExistsError:
        i = 0    
        metinDosyasiOlusturma = "{0}_{1}.txt".format(todoListBaslik,i)    
        todoListDosya = open(metinDosyasiOlusturma,"x",encoding="utf-8")
        i += 1
    
    todoListDosya.write("------------------------------------------\n")
    todoListDosya.write("  Başlık : {}".format(todoListBaslik)+"\n")
    todoListDosya.write("  Atanan Kişi : {}".format(todoListAtananKisi)+"\n")
    todoListDosya.write("  Öncelikli Atama : {}".format(todoListAtamaÖnceliği)+"\n")
    todoListDosya.write("  İçerik : \n   {}".format(todoListIcerik)+"\n")
    todoListDosya.write("  Son Tarih : {0}/{1}/{2}".format(todoListSontarih["Gün"],todoListSontarih["Ay"],todoListSontarih["Yıl"])+"\n")
    todoListDosya.write("  Durum : " + "Devam Ediyor"+"\n")
    todoListDosya.write("------------------------------------------")
    todoListDosya.close()
    todolists.append(todoListBaslik)
    os.system("cls")





def toDoListSilme():
    print("Var olan todolistleriniz : ")
    for i in todolists:
        print("-" + i)

    item = input("Hangisini silmek istiyorsunuz : ")

    todoListSilmeDosyasi = "{}.txt".format(item)

    try:
        os.remove(todoListSilmeDosyasi)
        print("ToDoList silindi.")
    except FileNotFoundError:
        print("ToDo list bulunamadı. ")
    os.system("cls")

def main():
    todoListTespitEtme()
    while True:
        print("############################")
        print("ToDoList Uygulaması")
        print("1) ToDoList Oluşturma \n"
             +"2) ToDoList Silme \n"
             +"3) ToDoList Çıkış \n")
        print("############################")
        print("---Var olan todolistler---")
        for i in todolists:
            print("-" + i)
        
        item = input("İstediğiniz işlemi seçiniz : ")
        if item == "1":
            toDoListOluşturma()
        elif item == "2":
            toDoListSilme()
        else:
            break

main()





