# ** SIC Assembler Projesi ** 
Bu depo, Simplified Instructional Computer (SIC) için bir assembler simülasyonunu içerir. Bu proje, SIC makine diline ait kodları işleyerek ara dosyalar ve nesne dosyaları oluşturur. Assembler, belirlenen kaynak kodları alır ve işlenmiş çıktılar üretir.

## ***Başlarken***
Bu rehber, projenin nasıl kurulacağı ve çalıştırılacağı hakkında adım adım bilgi vermektedir. Assembler'ı başarıyla kurmak ve kullanmak için aşağıdaki adımları takip edin.

## ***Ön Koşullar***
Projeyi kullanabilmek için sisteminizde Python'un yüklü olması gerekmektedir. Python'ı Python resmi web sitesinden `(https://www.python.org/downloads/)` indirip yükleyebilirsiniz.

## ***Proje Dosyalarını İndirme***
Projeyi bilgisayarınıza indirmek için GitHub reposundan klonlama yapabilirsiniz. Aşağıdaki git komutunu kullanarak projeyi klonlayın:
 
```
git clone https://github.com/yourusername/sic-assembler.git
cd sic-assembler
```

## Çalıştırma 
Assembler'ı çalıştırmak için, projenin bulunduğu dizinde terminal veya komut istemcisini açın ve aşağıdaki komutu girin:
SIC montajcı programlarının ilk geçiş aşamasında karşılaşılan bazı temel problemler şunlardır:
Hata Tespiti: Mevcut uygulamalar, tüm hataları doğru şekilde tespit edemeyebilir. Bu durum, programın hatalı çalışmasına veya çökmesine neden olabilir.
Sembol Tablosu Oluşturma: Sembol tablosu, programdaki tüm sembollerin ve adreslerinin kaydını tutar. Yanlış veya eksik bir sembol tablosu, programın yanlış yürütülmesine yol açabilir.
Bellek Gereksinimi Hesaplama: Programın bellek gereksinimi doğru şekilde hesaplanmazsa, program çalışırken bellek yetersizliği oluşabilir.
```
python assembler.py
```
Bu komut, assembler betiğini başlatır ve işlem sonuçlarını terminalde görüntüler.


##  Dosya Yapısı
Projede bulunan dosyalar şunlardır:

input.txt: Assembler'ın işleyeceği kaynak kodun bulunduğu dosya.
intermediate.txt: Assembler tarafından oluşturulan ara dosya.
assembler.py: Assembler işlevlerini içeren Python betiği.


--> Proje calisma sekli:
 İlk olarak, giriş olarak verilen kaynak kod dosyası (input.txt) satır satır okunur. Kaynak kod içerisindeki boş satırlar ve yorum satırları işleme alınmaz. Her bir işlenen satır için etiket, opcode ve operand bilgileri ayrıştırılır. Eğer okunan satır bir 'START' direktifi içeriyorsa, bu direktifin operandı başlangıç adresi olarak tanımlanır ve lokasyon sayacı (LOCCTR) bu adrese ayarlanır. Eğer 'START' direktifi yoksa veya işlenen satır bu direktiften sonraysa, kod etiketlerin ve opcode'ların boyutlarını hesaplayarak LOCCTR'ı günceller. Etiketler sembol tablosu (SYMTAB) içerisine eklenir; eğer bir etiket tekrar ediyorsa, bu durum hata listesi (errors) içerisine kaydedilir. 'WORD', 'RESW', 'RESB', 'BYTE' gibi direktiflerin ve talimatların byte cinsinden boyutları hesaplanır ve LOCCTR buna göre artırılır. Tüm bu bilgiler, işleme esnasında bir ara dosya (intermediate.txt) içerisine yazılır. Bu işlem tamamlandığında, programın uzunluğu hesaplanır ve sembol tablosu ile varsa hatalar konsola yazdırılır.
https://github.com/nazlidilara/sic_assembler/issues/1#issue-2226406423
