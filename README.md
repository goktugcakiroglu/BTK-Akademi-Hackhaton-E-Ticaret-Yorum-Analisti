# 🛒 Akıllı E-Ticaret Yorum Analisti (Multimodal & Agentic AI)
**BTK Akademi Hackathon '26 - E-Ticaret Teması**

Bu proje, e-ticaret platformlarındaki müşteri yorumlarını ve **kanıt fotoğraflarını** otonom olarak analiz eden, kurumsal yazılım mimarisiyle (**Strategy Pattern**) geliştirilmiş çoklu ajan (Multimodal Agentic) sistemidir.

## 🚀 Projenin Çözdüğü Problem ve Kullanıcı Değeri
E-ticaret ekosisteminde binlerce metin ve görsel yorumun manuel incelenmesi imkansızdır. Sistemimiz:
* **Müşteriler için:** Metin yorumları ve ürün fotoğraflarındaki (hasar, kusur vb.) detayları birleştirerek net bir **Satın Alma Rehberi** sunar.
* **Marka Yöneticileri için:** Ajanımız otonom olarak **internete bağlanır**, global sektör trendlerini (kronik şikayetler vb.) çeker ve bu veriyi yerel veri tabanımızla harmanlayarak kurumsal bir **Kriz Yönetimi ve Ar-Ge Raporu** yazar.

## ⚙️ Teknik Mimari ve SOLID İlkeleri (Ravioli Code)
Proje, LangChain altyapısı ve Nesne Yönelimli Programlama (OOP) prensipleriyle tasarlanmıştır. Sistem asla çökmemesi için **Session State (Hafıza)** ve **Büyük Veri (Token) Daraltma** kalkanlarıyla korunmaktadır.

1. **Görsel Dedektif Ajanı (Multimodal):** Yüklenen ürün fotoğraflarını yapay zeka ile analiz ederek fiziksel kusurları metne çevirir.
2. **Veri Ayıklayıcı Ajan:** Ham metin yorumlarını süzerek duygu analizi yapar.
3. **Web-Search Ajanı:** Karar vermeden önce DuckDuckGo üzerinden canlı pazar araştırması yapar.
4. **Sentezleyici Ajan (Strategy Pattern):** Arayüzden seçilen hedef kitleye uygun strateji sınıfını (**MusteriStratejisi** veya **MarkaStratejisi**) otonom olarak seçerek nihai raporu yazar.

## 🛠️ Kullanılan Teknolojiler
* **Dil & Görsel Modeli:** Google Gemini 2.5 Flash (Multimodal Capable)
* **Orkestrasyon & Ajanlar:** LangChain (Prompt Templates, StrOutputParser, DuckDuckGoSearchRun)
* **Veri İşleme ve İş Zekası:** Pandas
* **Kullanıcı Arayüzü:** Streamlit
* **Kurumsal Dışa Aktarım:** Python-Docx (Markdown to Word Parser)

## 💻 Kurulum ve Çalıştırma
1. Repoyu klonlayın ve kök dizine gidin.
2. Gerekli kütüphaneleri yükleyin: 
`pip install streamlit pandas langchain-google-genai python-dotenv python-docx duckduckgo-search langchain-community`
3. Kök dizinde bir `.env` dosyası oluşturup içine `GOOGLE_API_KEY=sizin_anahtarınız` yazın.
4. Uygulamayı başlatın: `streamlit run app.py`

*(Not: Üretilen raporlar, arayüz üzerinden kurumsal formata dönüştürülerek **.docx (Word)** olarak indirilebilmektedir.)*
