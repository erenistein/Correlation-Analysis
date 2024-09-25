
# CSV Dosyası Yükleme ve Korelasyon Analizi Web Uygulaması

## Proje Açıklaması

Bu proje, kullanıcıların bir CSV dosyası yükleyerek içerisindeki sayısal veriler üzerinde **korelasyon analizi** yapmasını sağlayan bir web uygulamasıdır. Uygulama ayrıca, sayısal sütunlar arasındaki korelasyonları **ısı haritası** olarak görselleştirir ve son sütunu hedef sütun kabul ederek bir **lineer regresyon modeli** ile tahminlerde bulunur. Sonuçlar, **Mean Squared Error (MSE)** değeri ile birlikte bir tablo olarak kullanıcıya sunulur.

## Kullanılan Teknolojiler

- **Python**: Uygulamanın backend kısmını oluşturmak için kullanıldı.
- **Flask**: Web uygulaması framework'ü olarak kullanıldı.
- **Pandas**: CSV dosyalarını işlemek ve veri analizi yapmak için kullanıldı.
- **Seaborn & Matplotlib**: Korelasyon ısı haritasını görselleştirmek için kullanıldı.
- **Scikit-learn**: Lineer regresyon modelini oluşturmak ve değerlendirmek için kullanıldı.
- **HTML & Bootstrap**: Kullanıcı arayüzünü tasarlamak için kullanıldı.

## Kurulum ve Çalıştırma

1. **Gereksinimler**: 
   - Python 3.x
   - Gerekli paketler: Flask, Pandas, Seaborn, Matplotlib, Scikit-learn
   
   Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install Flask pandas seaborn matplotlib scikit-learn
   ```

2. **Proje Dosyaları**:
   - `app.py`: Uygulamanın ana dosyası. Flask server'ını çalıştırır ve yüklenen CSV dosyaları üzerinde işlem yapar.
   - `templates/index.html`: Ana sayfa (CSV dosyasının yüklendiği form).
   - `templates/result.html`: Analiz sonuçlarının gösterildiği sayfa (ısı haritası ve tahmin sonuçları).
   - `static/`: CSS dosyalarını ve diğer statik kaynakları içerir.
   - `uploads/`: Yüklenen CSV dosyalarının geçici olarak saklandığı klasör.

3. **Uygulamanın Çalıştırılması**:

   Aşağıdaki adımları izleyerek uygulamayı çalıştırabilirsiniz:

   - `app.py` dosyasının bulunduğu dizinde terminali açın ve şu komutu çalıştırın:
     ```bash
     python app.py
     ```
   
   - Uygulama, yerel sunucuda başlatılacak ve şu adresten erişilebilecektir: `http://127.0.0.1:5000/`

4. **Kullanım Adımları**:

   - Uygulama açıldığında ana sayfa üzerinde bir **CSV dosyası** yüklemenizi isteyen bir form göreceksiniz.
   - Yükleyeceğiniz CSV dosyası, sadece **sayısal sütunlar** içermelidir (örn: fiyat, miktar gibi).
   - CSV dosyasını yükledikten sonra, uygulama otomatik olarak:
     - Yüklediğiniz dosyadaki verileri analiz eder.
     - Sayısal veriler arasındaki **korelasyon ısı haritasını** oluşturur.
     - Veriler üzerinde **lineer regresyon** analizi yapar ve sonuçları gösterir.
   
   Sonuçlar:
   - **Korelasyon Isı Haritası**: CSV'deki sayısal sütunlar arasındaki korelasyonları görsel olarak sunar.
   - **Mean Squared Error (MSE)**: Lineer regresyon modelinin hata oranını gösterir.
   - **Tahmin Sonuçları**: Gerçek değerler ve model tarafından tahmin edilen değerleri bir tablo şeklinde gösterir.

## Proje Yapısı

```
|-- app.py                   # Uygulamanın ana dosyası
|-- templates/
|   |-- index.html            # Ana sayfa (CSV yükleme formu)
|   |-- result.html           # Sonuç sayfası (Isı haritası ve tahminler)
|-- static/
|   |-- css/                  # CSS dosyaları (Bootstrap vs.)
|-- uploads/                  # Yüklenen CSV dosyalarının saklandığı klasör
```

## Sorun Giderme

- Eğer uygulama çalışmıyorsa veya ısı haritası gösterilmiyorsa, CSV dosyasının formatını kontrol edin. Uygulama sadece **sayısal sütunlar** içeren CSV dosyalarını kabul eder.
- Yüklediğiniz CSV dosyasında eksik veya boş veriler varsa, uygulama bu satırları temizleyecektir. Veri setinin yeterli miktarda sayısal veri içerdiğinden emin olun.

## Geliştirme

Bu projeyi geliştirmek isterseniz:
- **Farklı model algoritmaları** ekleyerek (örneğin: Decision Tree, Random Forest) daha gelişmiş analizler yapabilirsiniz.
- **Kullanıcı arayüzünü** geliştirerek daha kullanıcı dostu hale getirebilirsiniz.

---


