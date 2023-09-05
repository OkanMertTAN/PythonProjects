import math

print("######################")
print("---Hesap Makinasi---")
print("######################")


class Matematik:
    def temelDörtIslem(self):# 1
        try:
            print("Toplama : 1 , Çikartma : 2 , Çarpma : 3, Bölme : 4")
            item = input("Yapmak istediğiniz temel işleminin giriniz :")

            sayi1 = int(input("Birinci sayiyi giriniz : "))
            sayi2 = int(input("İkinci sayiyi giriniz : "))

            if item == "1":
                return  sayi1 + sayi2
            elif item == "2":
                return  sayi1 - sayi2
            elif item == "3":
                return  sayi1 * sayi2
            elif item == "4":
                if sayi2 == 0:    
                    print("İkinci sayi bölme işleminde payda değerdir. Ancak payda değeri sifir olamaz.")
                else :
                    return  sayi1 / sayi2
            else: 
                print("Lütfen dört işlem için geçerli bir operatör giriniz.")
        except ValueError:
            print("----------------------------------------------------------")
            print("Lütfen tüm değerleri eksiksiz bir şekilde giriniz.")
            print("----------------------------------------------------------")
        except ZeroDivisionError:
            print("----------------------------------------------------------")
            print("Lütfen tüm değerleri eksiksiz bir şekilde giriniz.")
            print("----------------------------------------------------------")


    def bilimselHesaplama(self):#2 ,aritmetik ort , geometri ort,
        try:
            print("Aritmetik Ortlama : 1 , Geometrik Ortalama : 2 , Varyans : 3")
            item = input("Yapmak istediğiniz işlemin sayisini yaziniz : ")
            if item =="1":
                print("----------------Aritmetik Ortalama----------------")
                count = int(input("İşlemde kaç adet sayi olacak : "))

                sayilar = []
                top = 0
                i = 0
                while i < count:
                    sayilar.append(int(input(" {0}. sayiyi giriniz : ").format(i)))
                    i += 1
            
                for i in sayilar:
                    top += i

                return top / (count)
        
            elif item == "2":
                print("----------------Geometrik Ortalama----------------")
                count = int(input("İşlemde kaç adet sayi olacak : "))

                sayilar = []
            
                i = 0
                while i < count:
                    sayilar.append(int(input(" {0}. sayiyi giriniz : ").format(i)))
                    i += 1
            
                carp = 1
                for i in sayilar:
                    carp *= i

                return carp **(1/len(sayilar))

            elif item == "3":
                print("----------------Varyans----------------")
                count = int(input("İşlemde kaç adet sayi olacak : "))

                sayilar = []
                top = 0
                i = 0
                mean = 0
                while i < count:
                    sayilar.append(int(input(" {0}. sayiyi giriniz : ").format(i)))
                    i += 1
                for i in sayilar:
                    top += i
            
                mean = top / count

                kareliDeger = []
                for i in sayilar:
                    kareliDeger.append(math.sqrt(math.fabs(i - mean)))

                karesiTop=0
                for i in kareliDeger:
                   karesiTop += i

                return karesiTop / (count - 1)
        
            else :
                print("Lütfen bilimsel hesaplama için geçerli bir operatör giriniz.")
        except ValueError:
            print("----------------------------------------------------------")
            print("Lütfen tüm değerleri eksiksiz bir şekilde giriniz.")
            print("----------------------------------------------------------")
        except ZeroDivisionError:
            print("----------------------------------------------------------")
            print("Lütfen tüm değerleri eksiksiz bir şekilde giriniz.")
            print("----------------------------------------------------------")

            

while True:
    print("######################")
    print("Temel İslemeleri için : 1 , Bilimsel Hesaplam için : 2 , Çikiş için : 3 veya herhangibi bir değer giriniz.")
    print("######################")

    islem = input("Hangi hesaplama yapmak istiyorsunuz : ")        
    if islem == "1":
        sonuc = Matematik().temelDörtIslem()
        print("-------------------------------------")
        print("İşlem sonucu : {0} ".format(sonuc))
        print("-------------------------------------")
    elif islem == "2":
        sonuc = Matematik().bilimselHesaplama()
        print("-------------------------------------")
        print("İşlem sonucu : {0} ".format(sonuc))
        print("-------------------------------------")
    else: 
        break



