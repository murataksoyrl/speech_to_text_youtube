# Konuşmayı Metne Dönüştürmek

Bu Python uygulaması, youtube videolarındaki konuşmayı kayıtlarını metne dönüştürmek için kullanılan basit bir araçtır. Ses dosyasını alır, metne çevirir ve sonucu bir .txt dosyasına kaydeder.

# Speech to Text Conversion

This Python application is a simple tool for converting speech recordings from YouTube videos to text. It takes the audio file, converts it to text, and saves the result in a .txt file.

## Kullanım

Aşağıdaki adımları izleyerek bu uygulamayı kullanabilirsiniz:

1. Öncelikle projeyi bilgisayarınıza klonlayın:

git clone https://github.com/KullaniciAdiniz/speech_to_text_youtube.git

2. Uygulamanın ana dizinine gidin:

cd speech_to_text_youtube

3. Python'un gerekli bağımlılıklarını yükleyin:

```python
pip install -r
import os
import youtube_dl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
```

4. Ses dosyanızı bu dizine ekleyin veya yolunu belirtin.

5. Uygulamayı çalıştırın:

`sesdosyasi.wav` yerine dönüştürmek istediğiniz ses dosyasının adını kullanın.

6. Dönüştürülmüş metin sonucunu `sonuc.txt` adlı bir metin dosyasında bulabilirsiniz.

### Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Fork (çatallama) düğmesini kullanarak bu projeyi kendi GitHub hesabınıza çatallayın.

2. Kendi çatalınıza klon alarak projeyi yerel ortamınıza indirin:

git clone https://github.com/KullaniciAdiniz/speech_to_text_youtube.git

3. Yeni özellikler veya düzeltmeler eklemek için çalışmalarınızı yapın ve tekrar github'a yükleyin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [Lisans Dosyası](LICENSE) sayfasını inceleyin.
