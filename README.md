#  Basit Phishing URL Tespit Aracı

Bu proje, kullanıcıdan alınan bir URL’yi analiz ederek onun potansiyel olarak **güvenli**, **şüpheli** ya da **phishing olabilir** olup olmadığını belirlemeye çalışan basit bir URL analiz aracıdır.

# Projenin Amacı

Siber güvenlik dünyasında en sık karşılaşılan saldırılardan biri **phishing (oltalama)** saldırılarıdır. Bu saldırılarda kullanıcılar sahte web sitelerine yönlendirilerek şifre, banka bilgisi gibi hassas verileri vermeleri sağlanır.

Bu proje, temel URL özelliklerine bakarak bir URL'nin ne kadar güvenli olduğunu tespit etmeye çalışır. Basit bir terminal arayüzü ile kullanıcıdan bir site adresi alınır ve sonucu kısa bir özetle çıktılar.

# Kullanılan Kütüphaneler ve Amaçları

| `urllib.parse`    | URL’yi parçalayarak bileşenlerine ayırmak (örneğin: domain, path).   
| `tldextract`      | Domain’in kök ve üst düzey alan adlarını ayırmak.                    
| `socket`          | IP adresi tespiti için kullanılır (IP ile yazılmış URL'leri anlamak).
| `whois`           | Alan adının kime ait olduğunu kontrol etmek için.                    
| `re`              | Regex ile şüpheli karakterleri kontrol etmek için (potansiyel kullanım). 

# Nasıl Çalışır? 

Girilen URL analiz edilerek:
- IP adresi kullanımı
- HTTPS olup olmadığı
- Uzunluk
- Şüpheli karakterlerin varlığı
- Whois kaydı olup olmadığı
- Şüpheli anahtar kelimeler içerip içermediği gibi
özellikler incelenir ve toplam puan üzerinden bir güvenlik değerlendirmesi yapılır.

# Kurulum ve Kullanım

Python 3 yüklü olmalıdır.

Gerekli kütüphaneleri yükleyin:

```
pip install tldextract python-whois
```

Programı çalıştırmak için terminalde:

```
python main.py
```

Gelen isteme URL girin, analiz sonucu ekrana yazdırılır.

Bu araç eğitim amaçlıdır ve tam kapsamlı phishing tespiti için yeterli değildir.
