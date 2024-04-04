# sic_assembler

Bu proje, SIC (Simplified Instructional Computer) mimarisi için tasarlanmış bir PASS1 Assembler'ın geliştirilmesini kapsamaktadır. SIC, eğitim amaçlı olarak tasarlanmış basitleştirilmiş bir bilgisayar mimarisidir ve bu projede, SIC için bir assembler'ın ilk geçiş algoritması (PASS1) implemente edilmiştir.bir montajcı programındaki hataları ve sembol tablolarını oluşturmak için kullanılan bir adımdır. Bu uygulama, SIC mimarisindeki tüm opcode'ları ve direktifleri destekler ve programın bellek gereksinimlerini de hesaplar.

SIC montajcı programlarının ilk geçiş aşamasında karşılaşılan bazı temel problemler şunlardır:
Hata Tespiti: Mevcut uygulamalar, tüm hataları doğru şekilde tespit edemeyebilir. Bu durum, programın hatalı çalışmasına veya çökmesine neden olabilir.
Sembol Tablosu Oluşturma: Sembol tablosu, programdaki tüm sembollerin ve adreslerinin kaydını tutar. Yanlış veya eksik bir sembol tablosu, programın yanlış yürütülmesine yol açabilir.
Bellek Gereksinimi Hesaplama: Programın bellek gereksinimi doğru şekilde hesaplanmazsa, program çalışırken bellek yetersizliği oluşabilir.

Bu projede amac:
Tüm opcode'ları ve direktifleri doğru şekilde işleyen bir ilk geçiş algoritması geliştirmek
Doğru ve eksiksiz bir sembol tablosu oluşturmak
Programın bellek gereksinimlerini doğru şekilde hesaplamak
Hataları ve uyarıları net bir şekilde raporlamak 

Proje calisma sekli:
 İlk olarak, giriş olarak verilen kaynak kod dosyası (input.txt) satır satır okunur. Kaynak kod içerisindeki boş satırlar ve yorum satırları işleme alınmaz. Her bir işlenen satır için etiket, opcode ve operand bilgileri ayrıştırılır. Eğer okunan satır bir 'START' direktifi içeriyorsa, bu direktifin operandı başlangıç adresi olarak tanımlanır ve lokasyon sayacı (LOCCTR) bu adrese ayarlanır. Eğer 'START' direktifi yoksa veya işlenen satır bu direktiften sonraysa, kod etiketlerin ve opcode'ların boyutlarını hesaplayarak LOCCTR'ı günceller. Etiketler sembol tablosu (SYMTAB) içerisine eklenir; eğer bir etiket tekrar ediyorsa, bu durum hata listesi (errors) içerisine kaydedilir. 'WORD', 'RESW', 'RESB', 'BYTE' gibi direktiflerin ve talimatların byte cinsinden boyutları hesaplanır ve LOCCTR buna göre artırılır. Tüm bu bilgiler, işleme esnasında bir ara dosya (intermediate.txt) içerisine yazılır. Bu işlem tamamlandığında, programın uzunluğu hesaplanır ve sembol tablosu ile varsa hatalar konsola yazdırılır.
