# Lost Ark Fishing Bot

Lost Ark ekranındaki balıkçılık simgesini OpenCV ile algılayıp `E` tuşuna basan, Python ile yazılmış deneysel bir otomasyon projesi.

> **Uyarı:** Bu araç ekran görüntüsü alır ve klavye girdisi gönderir. Kullanımı oyun kurallarını veya hizmet şartlarını ihlal edebilir; kullanmadan önce bunları kontrol edin. Proje eğitim/deney amaçlıdır ve geliştiricisi tarafından desteklenen ya da oyun tarafından onaylanan bir araç değildir.

## Özellikler

- Ekran görüntüsünde `ikon.png` şablonunu arar.
- Eşleşme algılandığında `E` tuşunu kullanır.
- Görüntü yakalama ve kontrol işlemlerini sürekli tekrarlar.

## Gereksinimler

- Python 3
- Masaüstü ekranını ve klavyeyi kontrol edebilen bir ortam
- Aşağıdaki Python paketleri:
  - OpenCV (`opencv-python`)
  - NumPy
  - PyAutoGUI
  - schedule

## Kurulum

Depoyu klonlayın ve proje klasörüne geçin:

```bash
git clone https://github.com/melihtop35/Lost_ark_fishing.git
cd Lost_ark_fishing
```

Gerekli paketleri yükleyin:

```bash
python -m pip install opencv-python numpy pyautogui schedule
```

## Çalıştırma

Görsel dosyalarının (`ikon.png` ve `resim.png`) arandığı `Main_file` klasörüne geçip betiği başlatın:

```bash
cd Main_file
python main.py
```

`ikon.png`, ekranda aranacak simge şablonudur. Betik ekran görüntüsünü `resim.png` adıyla kaydeder ve şablon eşleştirmesi yapar. Daha iyi algılama için oyun penceresini görünür tutun ve simgenin görünümünün şablonla eşleştiğinden emin olun.

## Durdurma ve dikkat edilmesi gerekenler

Program, `main.py` içinde sürekli çalışan bir döngü kullanır; uygulama içinde ayrı bir durdurma tuşu veya durdurma mekanizması tanımlı değildir. Betiği durdurmak için çalıştığı terminali kapatın veya işletim sisteminizin süreç yönetimini kullanın. PyAutoGUI'nin klavye girdileri aktif pencereye gönderildiğinden, çalıştırmadan önce doğru pencerenin etkin olduğundan emin olun.

## Proje yapısı

```text
Lost_ark_fishing/
├── Main_file/
│   ├── ikon.png
│   ├── main.py
│   ├── main.spec
│   └── resim.png
└── README.md
```

## Lisans

Depoda lisans dosyası bulunmadığından, kullanım ve yeniden dağıtım koşulları belirtilmemiştir. Lisans eklenene kadar hak sahibinden izin almadan yeniden dağıtım yapmayın.
