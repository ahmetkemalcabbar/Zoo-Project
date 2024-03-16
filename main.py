import numpy as np
import random

hyperparameter = {
    'hayvanlar' : {
        1: 'Erkek Koyun',
        2: 'Dişi Koyun',
        3: 'Erkek İnek',
        4: 'Dişi İnek',
        5: 'Horoz',
        6: 'Tavuk',
        7: 'Erkek Kurt',
        8: 'Dişi Kurt',
        9: 'Erkek Aslan',
        10: 'Dişi Aslan',
        11: 'Avcı',
    },
    
    'yönler' : {
        1: 'sağ',
        2: 'sol',
        3: 'aşağı',
        4: 'yukarı',
    },
    
    'av_birimi': {
        7: 4,
        8: 4,
        9: 5,
        10: 5,
        11: 8,
    },
}

"""
ÇİFTLEŞME KONTROL
Random bir hareket sonucunda, hareket eden hayvan karşı cinsiyle 3 birim veya 
daha fazla yakınlaşıp yakınlaşmadığını boolean değer olarak döndürüyor. 
    
İlk olarak yatay eksende (x) yakınlaşmaları, daha sonra dikey düzlemde yakınlaşmları
kontrol ediyor. Eğer bir yakınlaşma varsa True, yoksa False değer döndürüyor.

"""

def ciftesme_kontrol(erkek, disi):
    erkek_sayısı = erkek.shape[0]
    disi_sayısı = disi.shape[0]
    
    # Yatay düzlemde arama
    for i in range(0, erkek_sayısı):
        for j in range(0, disi_sayısı):
           if abs(erkek[i][0] - disi[j][0]) <= 3 and (erkek[i][1] == disi[j][1]):
                return True
            
    # Dikey düzlemde arama
    for i in range(0, erkek_sayısı):
        for j in range(0, disi_sayısı):
           if (abs(erkek[i][1] - disi[j][1]) <= 3) and (erkek[i][0] == disi[j][0]):
                return True
            
    return False

"""
AV KONTROL
Bir avcı ile avının avlanama birimi kadar yakınlaşıp yakınlaşmadığını
kontrol eden bir fonksiyon. Eğer yeteri kadar bir yakınlaşma varsa avcı
avı avlıyor. 

Av artık çiftlikte olmadığı için, avın arraydeki koordinatlarını tutan indexlere 
-1 değeri veriliyor. Ve av sayısı bir arttırılıyor.

Fonksiyon avın ait olduğu türün güncellenmeiş koordinat arrrayini ve av sayısını 
return ediyor. Bu sayede çiftlikteki hayvan sayısı da güncelleniyor. 

"""

def av_kontrol(avcı, av, birim):
    av_sayısı = 0
    
    # Yatay düzlemde arama
    for i in range(0, avcı.shape[0]):
        for j in range(0, av.shape[0]):
           if (abs(avcı[i][0] - av[j][0]) <= birim) and (avcı[i][1] == av[j][1]):
                av[j] = [-1, -1]
                av_sayısı += 1
                
    # Dikey düzlemde arama
    for i in range(0, avcı.shape[0]):
        for j in range(0, av.shape[0]):
           if (abs(avcı[i][1] - av[j][1]) <= birim) and (avcı[i][0] == av[j][0]):
                av[j] = [-1, -1]
                av_sayısı += 1
                
    return av, av_sayısı
    
"""
RANDOM HAREKET
Bir hayvanın random hareket etmesini sağlayan fonksiyon. 
İlk olarak random bir yön belirleniyor.
Daha sonrasında hareket edilecek birim sayısı random belirleniyor. Bu noktada çiftliğin
sınırları kontrol ediliyor. Hayvanın çiftlik sınırlarını aşan bir koordinata hareket etmesi engelleniyor. 

Ve geri kalan hareket miktarı kontrol ediliyor. Eğer random belirlenen hareket edilecek birim sayısı,
kalan birim hakkında büyükse hareket edilecek birim sayısı kalan birim hakkına eşitleniyor. Bu sayede,
kalan hareket birim hakkında daha fazla hareket etmenin önüne geçiliyor. 

"""

def random_hareket(x, y, hareket_kalan, hayvan_adı):
    hareket_birimi = 0
    hareket_yonu = random.randint(1, 4) # random hareket yönü bulma
    
    # 1 --> sağ yönde
    # 2 --> sol yönde
    # 3 --> aşağı yönde
    # 4 --> yukarı yönde
    
    if hareket_yonu == 1:
        hareket_birimi = random.randint(0, 499-x)
        if hareket_birimi>hareket_kalan:
            hareket_birimi = hareket_kalan
        #hareket_birimi = round(hareket_birimi/3)
        x += hareket_birimi
        print(f"Bir {hayvan_adı} {hyperparameter['yönler'][1]} yönde {hareket_birimi} birim hareket etti.\n")
    
    elif hareket_yonu == 2:
        hareket_birimi = random.randint(0, x)
        if hareket_birimi>hareket_kalan:
            hareket_birimi = hareket_kalan
        #hareket_birimi = round(hareket_birimi/3)
        x -= hareket_birimi
        print(f"Bir {hayvan_adı} {hyperparameter['yönler'][2]} yönde {hareket_birimi} birim hareket etti.\n")
        
    elif hareket_yonu == 3:
        hareket_birimi = random.randint(0, 499-x)
        if hareket_birimi>hareket_kalan:
            hareket_birimi = hareket_kalan
        #hareket_birimi = round(hareket_birimi/3)
        y += hareket_birimi
        print(f"Bir {hayvan_adı} {hyperparameter['yönler'][3]} yönde {hareket_birimi} birim hareket etti.\n")
        
    elif hareket_yonu == 4:
        hareket_birimi = random.randint(0, x)
        if hareket_birimi>hareket_kalan:
            hareket_birimi = hareket_kalan
        #hareket_birimi = round(hareket_birimi/3)
        y -= hareket_birimi
        print(f"Bir {hayvan_adı} {hyperparameter['yönler'][4]} yönde {hareket_birimi} birim hareket etti.\n")
    
    return x, y, hareket_birimi
    
    
"""
AV/ÇİFTLEŞME GÜNCELLEME
Hayvanların ilk çiftliğe random yerleştirilmesi ve her bir random hareketten sonra
çiftlikte her hangi bir av ya da çiftleşme durumunun olup olmadığı kontrol ediliyor. 

Eğer çiftleşme durumu varsa çiftleşen hayvanın cinsinde, random bir cinsiyette ve random bir koordinatta
yeni bir hayvan dünyaya geliyor ve bu hayvanın ait olduğu türün koordinat arrayi güncelleniyor. 
Hayvan sayısı 1 arttırılıyor. 

"""
def av_ciftlesme_update(i, j, hayvanlar, avlanacak_hayvanlar, hayvan_sayısı):
    
    #Eğer hayvan erkekse
    if (i%2 == 1) and (i != 11):
        
        #Çiftleşme olup olmadığı kontrol edilir
        yeni_hayvan = ciftesme_kontrol(hayvanlar[i], hayvanlar[i+1])

        if yeni_hayvan:
            bebek = np.random.randint(0, 499, size=(1, 2))
            cinsiyet = random.randint(0,1)
            if cinsiyet == 1:
                hayvanlar[i] = np.append(hayvanlar[i], bebek, axis=0)
            elif cinsiyet == 0:
                hayvanlar[i+1] = np.append(hayvanlar[i+1], bebek, axis=0)

            hayvan_sayısı+=1

        # Avlanma olup olmadığı kontrol edilir
        for key, value in avlanacak_hayvanlar.items():
            for value2 in value['av']:
                hayvanlar[value2], av_sayısı = av_kontrol(avcı =hayvanlar[key], 
                                                          av = hayvanlar[value2], 
                                                          birim = value['birim'])
                hayvan_sayısı -= av_sayısı
    
    #Eğer hayvan dişiyse
    elif (i%2 == 0):

        #Çiftleşme olup olmadığı kontrol edilir
        yeni_hayvan = ciftesme_kontrol(hayvanlar[i-1], hayvanlar[i])

        if yeni_hayvan:
            bebek = np.random.randint(0, 499, size=(1, 2))
            cinsiyet = random.randint(0,1)
            if cinsiyet == 1:
                hayvanlar[i-1] = np.append(hayvanlar[i-1], bebek, axis=0)
            elif cinsiyet == 0:
                hayvanlar[i] = np.append(hayvanlar[i], bebek, axis=0)

            hayvan_sayısı+=1

        # Avlanma olup olmadığı kontrol edilir
        for key, value in avlanacak_hayvanlar.items():
            for value2 in value['av']:
                hayvanlar[value2], av_sayısı = av_kontrol(avcı =hayvanlar[key], 
                                                          av = hayvanlar[value2], 
                                                          birim = value['birim'])
                hayvan_sayısı -= av_sayısı

    return hayvanlar, hayvan_sayısı


"""
İLK YERLEŞME
Program ilk çalıştırıldığı zaman hayvan koordinatlarını (x, y) tutan arrayler her bir 
tür için oluşturuluyor. Hayvanlar random olarak yerleştiriliyor. 

Daha sonrasında bu hayvanlar bir dictionary içine alınıyor. 

"""

def ilk_yerlesme():
    
    hayvan_sayısı = 78
    
    erkek_koyun = np.random.randint(0, 499, size=(15, 2))
    disi_koyun = np.random.randint(0, 499, size=(15, 2))

    erkek_inek = np.random.randint(0, 499, size=(5, 2))
    disi_inek = np.random.randint(0, 499, size=(5, 2))

    tavuk = np.random.randint(0, 499, size=(10, 2))
    horoz = np.random.randint(0, 499, size=(10, 2))

    erkek_kurt = np.random.randint(0, 499, size=(5, 2))
    disi_kurt = np.random.randint(0, 499, size=(5, 2))

    erkek_aslan = np.random.randint(0, 499, size=(4, 2))
    disi_aslan = np.random.randint(0, 499, size=(4, 2))

    avcı = np.random.randint(0, 499, size=(1, 2))
    
    hayvanlar = {
        1: erkek_koyun,
        2: disi_koyun,
        3: erkek_inek,
        4: disi_inek,
        5: horoz,
        6: tavuk,
        7: erkek_kurt,
        8: disi_kurt,
        9: erkek_aslan,
        10: disi_aslan,
        11: avcı
    }
    
    avlanacak_hayvanlar = {
        7: {
            'av': [1, 2, 5, 6],
            'birim' : 4,
        },
        8: {
            'av': [1, 2, 5, 6],
            'birim' : 4, 
        },
        9: {
            'av': [1, 2, 3, 4],
            'birim' : 5, 
        },
        10: {
            'av': [1, 2, 3, 4],
            'birim' : 5,
        },
        11: {
            'av': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'birim' : 8, 
        },
    }
    
    for i in range (1, 12):
        for j in range(0, hayvanlar[i].shape[0]):
            hayvanlar, hayvan_sayısı = av_ciftlesme_update(i = i, 
                                                           j = j, 
                                                           hayvanlar = hayvanlar, 
                                                           avlanacak_hayvanlar = avlanacak_hayvanlar, 
                                                           hayvan_sayısı = hayvan_sayısı)
            
    
    return hayvanlar, avlanacak_hayvanlar, hayvan_sayısı


"""
MAIN FUNCTION
"""

if __name__ == "__main__":
    birim_sayısı = 1000

    hayvanlar, avlanacak_hayvanlar, hayvan_sayısı = ilk_yerlesme()

    while(birim_sayısı>0):
        i = random.randint(1, 11)
        j = random.randint(0, hayvanlar[i].shape[0]-1)

        hayvanlar[i][j][0],hayvanlar[i][j][1], hareket_birimi = random_hareket(x = hayvanlar[i][j][0], 
                                                                               y = hayvanlar[i][j][1], 
                                                                               hareket_kalan = birim_sayısı, 
                                                                               hayvan_adı = hyperparameter['hayvanlar'][i])
        birim_sayısı -= hareket_birimi

        hayvanlar, hayvan_sayısı = av_ciftlesme_update(i = i, 
                                                       j = j, 
                                                       hayvanlar = hayvanlar, 
                                                       avlanacak_hayvanlar = avlanacak_hayvanlar, 
                                                       hayvan_sayısı = hayvan_sayısı)
        print(f"Birim Sayısı: {birim_sayısı}\n")

    print(f"Hayvan Sayısı: {hayvan_sayısı}\n")
