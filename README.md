# YouTube Video Summarizer

Bu proje, YouTube videolarının transkriptlerini otomatik olarak alıp, Türkçe olarak özetleyen bir Streamlit uygulamasıdır. Kullanıcıdan alınan YouTube video bağlantısı ile videonun transkripti çıkarılır ve Google Gemini API kullanılarak 250 kelimeyi geçmeyen, bilgilendirici ve ilgi çekici bir özet oluşturulur.

## Özellikler

- YouTube videosunun transkriptini otomatik olarak alma
- Transkriptin Türkçe olarak özetlenmesi (Gemini API ile)
- Kullanıcı dostu Streamlit arayüzü

## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi
   ```

2. Sanal ortam oluşturun ve etkinleştirin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
   ```

3. Gerekli Python paketlerini yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Ortam değişkenlerini ayarlayın:

   - `.env.example` dosyasını temel alarak `.env` dosyası oluşturun:

     ```bash
     cp .env.example .env
     ```

   - `.env` dosyasını açın ve kendi **Google Gemini API anahtarınızı** girin:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

> ⚠️ `.env` dosyası `.gitignore` tarafından yoksayılmaktadır ve repoya dahil edilmemelidir.

## Kullanım

1. Uygulamayı başlatın:

   ```bash
   streamlit run app.py
   ```

2. Açılan web arayüzünde YouTube video bağlantısını girin ve "Özetle" butonuna tıklayın.

## Dosya Yapısı

- `app.py`: Streamlit arayüzü
- `transcribe.py`: YouTube videosundan transkript alma işlemleri
- `summarize.py`: Transkripti özetleyen fonksiyonlar
- `requirements.txt`: Gerekli Python paketleri
- `.env.example`: Ortam değişkenleri için örnek dosya

## Notlar

- YouTube videosunun transkriptinin açık olması gerekmektedir.
- Özetler her zaman Türkçe olarak oluşturulur.
