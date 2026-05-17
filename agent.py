import base64
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun # 🌐 YENİ: Ajanın İnternet Aracı
from config import llm
from abc import ABC, abstractmethod

prompt_ajan1 = PromptTemplate.from_template("""
Aşağıdaki e-ticaret müşteri yorumlarını oku. Sadece şu formatta bir özet çıkar, ekstra cümle kurma:
- Olumlu Özellikler: [liste]
- Olumsuz Özellikler: [liste]
- Genel Memnuniyet Skoru (10 üzerinden): [puan]

Yorumlar:
{yorumlar}
""")
ajan1_zinciri = prompt_ajan1 | llm | StrOutputParser()

class RaporStratejisi(ABC):
    @abstractmethod
    def rapor_uret(self, ham_analiz: str) -> str:
        pass

class MusteriStratejisi(RaporStratejisi):
    def rapor_uret(self, ham_analiz: str) -> str:
        prompt = PromptTemplate.from_template("""
        Aşağıdaki ham analiz verisini kullanarak, Müşteriler için ürünü alıp almamaları konusunda tavsiye veren bir ürün incelemesi yaz.
        Ham Analiz:
        {ham_analiz}
        """)
        zincir = prompt | llm | StrOutputParser()
        return zincir.invoke({"ham_analiz": ham_analiz})

class MarkaStratejisi(RaporStratejisi):
    def rapor_uret(self, ham_analiz: str) -> str:
        arama_araci = DuckDuckGoSearchRun()
        try:
            sektor_trendleri = arama_araci.invoke("akıllı saat kronik sorunlar kullanıcı şikayetleri 2026")
        except Exception:
            sektor_trendleri = "İnternet araması şu an yapılamadı, yerel verilerle ilerlenecek."

        prompt = PromptTemplate.from_template("""
        Aşağıdaki verileri kullanarak, Marka Yöneticisi için profesyonel bir Kriz Yönetimi ve Ar-Ge raporu yaz.
        Raporu yazarken, internetten anlık olarak çektiğin 'Küresel Sektör Trendleri' ile 'Bizim Ürünümüzün Sorunlarını' mutlaka karşılaştır (Örn: 'Sektördeki genel sorun bu iken, bizim ürünümüzde de bu yaşanmış...' gibi).
        
        🌐 AJANIN CANLI İNTERNET ARAŞTIRMASI (Küresel Rakipler/Trendler):
        {sektor_trendleri}
        
        📊 BİZİM ÜRÜNÜN HAM MÜŞTERİ ANALİZİ:
        {ham_analiz}
        """)
        
        zincir = prompt | llm | StrOutputParser()
        return zincir.invoke({
            "ham_analiz": ham_analiz, 
            "sektor_trendleri": sektor_trendleri
        })

def gorsel_analiz_et(resim_bytes: bytes) -> str:
    resim_b64 = base64.b64encode(resim_bytes).decode("utf-8")
    mesaj = HumanMessage(
        content=[
            {"type": "text", "text": "Bu e-ticaret ürünü fotoğrafındaki fiziksel hasarı, kusuru veya öne çıkan durumu tek bir kısa cümleyle özetle."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{resim_b64}"}}
        ]
    )
    yanit = llm.invoke([mesaj])
    return yanit.content

def analiz_surecini_baslat(yorumlar_metni: str, strateji: RaporStratejisi):
    guvenli_metin_limiti = 15000
    if len(yorumlar_metni) > guvenli_metin_limiti:
        yorumlar_metni = yorumlar_metni[-guvenli_metin_limiti:] 
        
    ham_analiz_sonucu = ajan1_zinciri.invoke({"yorumlar": yorumlar_metni})
    
    final_rapor = strateji.rapor_uret(ham_analiz_sonucu)
    return final_rapor