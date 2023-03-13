#Mehmet Kubilay Gülaçdı

#Gerekli kitaplıkları içe aktarıyoruz.
import csv
import datetime


#Pizza üst sınıfı oluşturuyoruz.

class Pizza:
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.__class__.cost
    

#Pizza alt sınıfları oluşturuyoruz.
class KlasikPizza(Pizza):
    cost = 25.0
    def __init__(self):
        self.description = "Klasik Pizza"
        print('\n' + self.description)
        
        
class Margherita(Pizza):
    cost = 30.0

    def __init__(self):
        self.description = "Margherita"
        print('\n' + self.description)
        
class TurkishPizza(Pizza):
    cost = 35.0

    def __init__(self):
        self.description = "TurkishPizza"
        print('\n' + self.description)

class DominosPizza(Pizza):
    cost = 40.0

    def __init__(self):
        self.description = "Dominos Pizza"
        print('\n' + self.description)


#Decorator üst sınıfını oluşturuyoruz.
class DecoratorClass(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
       return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
       return self.component.get_description() + \
        ',' + Pizza.get_description(self)
    

#Soslar için ayrı ayrı sınıflar oluşturuyoruz. DecoratorClass sınıfı sos sınıflarının süper sınıfı olarak adlandırılıyor.
class Zeytin(DecoratorClass):
    cost = 5.0
        
    def __init__(self, component):
        self.description = "Zeytin Sosu"
        super().__init__(component) #Super sınıf olan DecoratorClass'ın init methodundaki component özelliğini aktarıyoruz.
        print("\n...Zeytin eklendi...")

class Mantar(DecoratorClass):
    cost = 4.0 
    def __init__(self, component):
        self.description = "Mantar Sosu"
        super().__init__(component)
        print("\n...Mantar eklendi...")

class KeciPeyniri(DecoratorClass):
    cost = 3.0  
    def __init__(self, component):
        self.description = "Keci Peyniri Sosu"
        super().__init__(component)
        print("\n...KeciPeyniri eklendi...")
    
class Et(DecoratorClass):
    cost = 7.0  
    def __init__(self, component):
        self.description = "Et Sosu"
        super().__init__(component)
        print("\n...Et eklendi...")

class Sogan(DecoratorClass):
    cost = 3.0 
    def __init__(self, component):
        self.description = "Sogan Sosu"
        super().__init__(component)
        print("\n...Sogan eklendi...")

class Misir(DecoratorClass):
    cost = 3.0
    def __init__(self, component):
        self.description = "Misir Sosu"
        super().__init__(component)
        print("\n...Misir eklendi...")

#Menu ve sipariş işlemleri için bir main fonksiyon oluşturuyoruz.
def main():

    print("\n"*3)

    with open("Menu.txt", 'r') as menu:
        print(menu.read())

    order_dict ={1:KlasikPizza, 2:Margherita, 3:TurkishPizza, 4:DominosPizza,
                5:Zeytin, 6:Mantar, 7:KeciPeyniri, 8:Et, 9:Sogan, 10:Misir}
    
    print("\n")

    order_number= input("Lütfen menüden istediğiniz pizzanın numarasını giriniz: ")

    while order_number not in ["1","2","3","4"]: #Geçerli bir işlem yapana kadar döngüye sokuyoruz.
        order_number = input("Lütfen geçerli bir pizza tuşlayınız: ")

    order = order_dict[int(order_number)]() #Sınıfa ait obje oluşturuyoruz.

    while order_number != "0": #İstediği kadar malzeme ekleyebilmesi için müşteri onaylayana kadar döngüye sokuyoruz.
        order_number = input("Ekstra malzeme eklemek için menüden tuşlama yapınız yoksa onay için 0'ı tuşlayınız: ")
        if order_number in ["5","6","7","8","9","10"]:
            order = order_dict[int(order_number)](order)

        while order_number not in ["0","5","6","7","8","9","10"]: #Geçerli bir işlem yapılmaması halinde yapılana kadar döngüye sokuyoruz.
            order_number = input("Lütfen geçerli bir işlem tuşlayınız: ")     
    else:
        print("\nSeçmiş olduğunuz Pizza: "+ order.get_description() + "\nÖdeyeceğiniz tutar " + str(order.get_cost()) +  "TL" )
        print("\n")
        

#Sipariş Bilgilerini alıyoruz ve bir CSV dosyası oluşturuyoruz.
    print("----------Sipariş Bilgileri için lütfen doldurunuz----------\n")
    name = input("İsminiz: ")
    TCKN = input("TC Kimlik Numaranız: ")
    cc_no= input("Kredi Kartı Numaranızı Giriniz: ")
    cc_pw = input("Kredi Kartı Şifrenizi Giriniz: ")
    time = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as order_db:
        writer = csv.writer(order_db, delimiter=',')

        #CSV Dosyası için header oluşturuyoruz.
        try:
            with open('Orders_Database.csv', 'r') as order_db:
                order_db = csv.reader(order_db)
                next(order_db)  
        except StopIteration:
            writer.writerow(["Isim", "TC Kimlik No", "Kredi Karti No", "Kredi Karti Sifresi", "Siparis Aciklamasi", "Siparis Tarihi"])

        writer.writerow([name, TCKN, cc_no, cc_pw, order.get_description(), time])
        print("Siparişiniz Onaylandı. Afiyet olsun.")



main()