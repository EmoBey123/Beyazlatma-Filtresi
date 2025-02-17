#Google Colab
#!pip install -q -U google-genai

import numpy as np
from PIL import Image
from google import genai

resim = Image.open("/content/Eharfi.png")
kod="""
      deger1=int(input("Beyazlatma Degeri Giriniz"))
      matris=np.array(resim)
      matris=np.where(matris>deger1,255,matris)
      resim=Image.fromarray(matris)
    """

client = genai.Client(api_key="your_api_key")
response = client.models.generate_content(
    model="gemini-2.0-flash-exp", contents=f"""{resim} {kod} resim bu bunu daha iyi yapmak istiyorum ve koda bakarak beyazlaştırma için deger1 hangi sayıyı gireyim kendin dene ve bana söyle tek kelime cevap""")
print(response.text)

deger1=int(input("Beyazlatma Degeri Giriniz"))
matris=np.array(resim)
matris=np.where(matris>deger1,255,matris)
resim=Image.fromarray(matris)
resim
