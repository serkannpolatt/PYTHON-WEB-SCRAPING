## Türkçe
## Hisse Senedi Fiyatları ve Hacim Verileri Çekme

Bu proje, www.isyatirim.com.tr adresinden belirli bir hisse senedinin kapanış fiyatları ve hacim verilerini çeken bir Python scriptini içerir. Ayrıca, bu verileri bir veri çerçevesine dönüştürür ve tarih sıralı hale getirir

### Amaç ve İşlev
Bu proje, finansal analistler, yatırımcılar ve veri bilimciler için aşağıdaki amaçlara hizmet etmek üzere tasarlanmıştır:

**1. Hisse Senedi Verilerini Çekme:**

- Belirli bir hisse senedinin kapanış fiyatları ve hacim verilerini, www.isyatirim.com.tr web sitesinden otomatik olarak çeker.
- Script, bu verileri JSON formatında alır ve bir Python veri çerçevesine dönüştürür.

**2. Veri Analizi ve Görselleştirme:**

- Çekilen veriler, tarih sıralı hale getirilir ve ilgili hisse senedinin zaman içindeki performansını analiz etmek için kullanılır.
- Veriler, ayrı bir CSV dosyasına kaydedilir ve gerektiğinde çeşitli veri analizi araçları ve görselleştirme kütüphaneleri ile kullanılabilir.

**3. Toplu Veri Çekme:**

- first_df veri çerçevesindeki BIST TÜM endeksine ait hisse senetlerinin verilerini toplu bir şekilde çeker ve ayrı ayrı CSV dosyalarına kaydeder.
- Bu, kullanıcıların birden fazla hisse senedi verisini tek bir script çalıştırarak toplu bir şekilde elde etmelerine olanak tanır.

## English
## Pulling Stock Prices and Volume Data

This project includes a Python script that retrieves closing prices and volume data of a specific stock from www.isyatirim.com.tr. It also converts this data into a dataframe and makes it date-sorted

### Purpose and Function
This project is designed to serve the following purposes for financial analysts, investors and data scientists:

**one. Extracting Stock Data:**

- It automatically retrieves the closing prices and volume data of a particular stock from the www.isyatirim.com.tr website.
- The script takes this data in JSON format and converts it into a Python data frame.

**2. Data Analysis and Visualization:**

- The data pulled is date-ordered and used to analyze the performance of the relevant stock over time.
- Data is saved in a separate CSV file and can be used with various data analysis tools and visualization libraries as needed.

**3. Bulk Data Extraction:**

- It collects the data of the stocks of the BIST ALL index in the first_df data frame in bulk and saves them in separate CSV files.
- This allows users to retrieve multiple stock data in bulk by running a single script.