# 🎥 Summarize It

**Summarize It**, YouTube videolarını analiz ederek içeriklerini özetleyen bir mobil uygulamadır.  
Flutter ile geliştirilen bu uygulama, FastAPI tabanlı bir backend'e bağlanarak Google Gemini API üzerinden video transkriptini işler, başlık ve özet üretir.

---

## 🚀 Özellikler

- 🔗 YouTube video linki ile otomatik özet alma
- ✍️ Gemini AI ile içerik analizi ve Türkçe başlık + özet oluşturma
- 📄 Oluşturulan özeti cihazınıza PDF olarak kaydedebilme
- 🧠 Özet üzerinden quiz oluşturma ve çözüm geçmişi takibi
- 🎓 Video içeriğini ders notu formatında görselleştirme
- 📊 Quiz sonucunu gösterme ve tekrar çözüm opsiyonu
- 📱 Flutter ile modern, sezgisel ve kullanıcı dostu arayüz

---

## 🧰 Kullanılan Teknolojiler

| Katman        | Teknoloji                     |
| ------------- | ----------------------------- |
| 🎯 Mobil      | Flutter (Dart)                |
| ⚙️ Backend    | FastAPI (Python)              |
| 🧠 Yapay Zeka | Google Gemini (Generative AI) |
| 🔠 NLP        | youtube-transcript-api        |
| 🔒 Ortam      | python-dotenv                 |

---

## 📱 Uygulama Görselleri

<p align="center">
  <img src="assets/mainscreen2.jpg" alt="Ana Ekran" width="200"/>
  <img src="assets/summarize2.jpg" alt="Özet Oluşturma" width="200"/>
  <img src="assets/keypoints2.jpg" alt="Önemli Noktalar" width="200"/>
</p>

<p align="center">
  <b>Ana Ekran</b> &nbsp;&nbsp;&nbsp;&nbsp;
  <b>Özet Oluşturma</b> &nbsp;&nbsp;&nbsp;&nbsp;
  <b>Önemli Noktalar</b>
</p>

<br/>

<p align="center">
  <img src="assets/quiz2.jpg" alt="Quizler" width="200"/>
  <img src="assets/pdf.jpg" alt="PDF Kaydet" width="200"/>
</p>

<p align="center">
  <b>Quiz Listesi</b> &nbsp;&nbsp;&nbsp;&nbsp;
  <b>PDF Kaydetme</b>
</p>

---

## 🧪 Nasıl Çalışır?

1. Kullanıcı bir YouTube video linki girer.
2. Flutter uygulaması bu linki backend'e gönderir (`/summarize` endpoint).
3. Backend, videonun transkriptini çeker ve Gemini ile:
   - Kısa bir başlık (10 kelimeyi geçmeyen)
   - Maksimum 250 kelimelik Türkçe özet üretir.
4. Sonuçlar Flutter arayüzünde kullanıcıya gösterilir.

---

## 📦 Kurulum

### ✅ Backend (FastAPI)

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/iremdilsatkse/summarize-it.git
   cd summarize-it
   ```
2. Sanal ortam oluşturun ve etkinleştirin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Gereken Python paketlerini yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Ortam değişkenlerini tanımlayın:

.env.example dosyası örnek ortam dosyasıdır. Kendi .env dosyanızı şu şekilde oluşturun:

```bash
cp .env.example .env # Windows: copy .env.example .env
```

Ardından .env dosyasını açın ve Gemini API anahtarınızı girin:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ .env dosyası .gitignore içinde yer alır ve Git'e eklenmez. Bu sayede gizliliğiniz korunur.

5. Uygulamayı başlatın:

   ```bash
   uvicorn main:app --reload
   ```

   API dokümantasyonu: http://localhost:8000/docs

   ***

## 📱 Flutter Mobil Arayüz Kaynağı

Uygulamanın kullanıcı arayüzü Flutter ile geliştirilmiştir.  
Mobil uygulamanın kaynak kodlarına aşağıdaki bağlantıdan ulaşabilirsiniz:

🔗 [Flutter Arayüz Repo Linki](https://github.com/ozgurilter/summarize_it)

> Bu repo, YouTube video özetleme, quiz görüntüleme, PDF kaydetme ve kullanıcı etkileşimleri gibi tüm arayüz işlemlerini içermektedir.

## Uygulama videosu

🔗 [Youtube Video Linki](https://youtube.com/shorts/0hpD9SlNDsI?si=qbjG73DX5zI8gitP)
