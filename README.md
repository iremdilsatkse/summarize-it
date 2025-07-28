# YouTube Video Summarizer

Bu proje, YouTube videolarının transkriptlerini otomatik olarak alıp, Türkçe olarak özetleyen bir Streamlit uygulamasıdır. Kullanıcıdan alınan YouTube video bağlantısı ile videonun transkripti çıkarılır ve Google Gemini API kullanılarak 250 kelimeyi geçmeyen, bilgilendirici ve ilgi çekici bir özet oluşturulur.

## Özellikler

- YouTube videosunun transkriptini otomatik olarak alma
- Transkriptin Türkçe olarak özetlenmesi (Gemini API ile)
- Kullanıcı dostu Streamlit arayüzü

## Kurulum

1. Depoyu klonlayın:
    ```
    git clone https://github.com/kullaniciadi/proje-adi.git
    cd proje-adi
    ```

2. Bir env oluşturun:
    ```
    python -m venv venv
    ```
   
3. Gerekli Python paketlerini yükleyin:
    ```
    pip install -r requirements.txt
    ```

4. `.env` dosyasına Google Gemini API anahtarınızı ekleyin:
    ```
    GEMINI_API_KEY = your_gemini_api_key_here
    ```

## Kullanım

1. Uygulamayı başlatın:
    ```
    streamlit run app.py
    ```

2. Açılan web arayüzünde YouTube video bağlantısını girin ve "Özetle" butonuna tıklayın.

## Dosya Yapısı

- `app.py`: Streamlit arayüzü
- `transcribe.py`: YouTube videosundan transkript alma işlemleri
- `summarize.py`: Transkripti özetleyen fonksiyonlar
- `requirements.txt`: Gerekli Python paketleri

## Notlar

- YouTube videosunun transkriptinin açık olması gerekmektedir.
- Özetler her zaman Türkçe olarak oluşturulur.

