import os
import glob
from django.core.files import File  # Import the File class
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from faker import Faker

from .models import ImageUpload, TextUpload, VoiceUpload


class ImageUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        # Define the path to your sample image
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "api", "test_media", "base_test_image.jpg")

        # Open the sample image and read it
        with open(image_path, "rb") as image_file:
            image = File(image_file)
            self.image = SimpleUploadedFile(
                name="test_image.jpg",
                content=image_file.read(),
                content_type="image/jpeg",
            )

        self.url = "/api/images/"

    def test_create_image(self):
        # Test creating an image through the API
        response = self.client.post(self.url, {"image": self.image})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ImageUpload.objects.count(), 1)

    def test_retrieve_images(self):
        # Test retrieving images through the API
        self.client.post(self.url, {"image": self.image})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        # Define the path to your media/images folder
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_image_path = os.path.join(base_dir, "media", "images")

        # Pattern to match all files starting with 'test_' in the media/images directory
        test_files_pattern = os.path.join(media_image_path, "test_*")

        # Use glob to find all matching files
        test_files = glob.glob(test_files_pattern)

        # Remove each file
        for file in test_files:
            os.remove(file)

        super().tearDown()  # Call the tearDown method of the superclass.


class TextUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        self.text = """
GÖRÜŞ - Güney Afrika'nın UAD başvurusu: Emsal kararlar ne söylüyor?
UAD'nin, Güney Afrika'nın İsrail'e karşı açtığı davada ihtiyati tedbir kararı vermesine neredeyse kesin gözüyle bakılıyor. Mahkeme'nin tedbir kararı vermemesi, bilhassa Bosna, Rohingya ve Ukrayna vakalarındaki yaklaşımıyla tezatlık teşkil edecektir.

Boğaziçi Üniversitesi Hukuk Fakültesi Öğretim Üyesi Ali Emrah Bozbayındır, Güney Afrika'nın İsrail aleyhine açtığı soykırım davası çerçevesinde, Uluslararası Adalet Divanında (UAD) açılan emsal davalardan çıkan kararları ve etkilerini AA Analiz için kaleme aldı.

***

Güney Afrika'nın İsrail aleyhine UAD nezdinde açtığı soykırım davasının ihtiyati tedbir taleplerine ilişkin duruşmaları geçen hafta yapıldı. UAD'de 11 Ocak'taki oturumda, Güney Afrika hukuk ekibinin, oldukça iyi hazırlanmış hukuk sanatının icra edildiği sunumunun yanı sıra meselenin insani yönü de ıskalanmadı. Bu hususta özellikle Blinne Ni Ghralaigh sunumunda; Mahkeme, gerekli tedbirlerin alınması yolundaki kararı derhal almadığı takdirde telafisi zor zararların meydana geleceğinin ve soykırım teşkil eden yeni fiillerin icra edilebileceğinin altını çizdi. Gazze'deki mevcut durumun bir insanlık krizi olduğunu ve muadili olmayan bir dehşetle bütün halkın kuşatma altında açlıkla mücadele ettiğini anlatan Ghralaigh, derhal tedbir alınmazsa çok geç olabileceğini çarpıcı bir şekilde gözler önüne serdi. Günlük istatistiklere bakıldığında her gün 48'i anne, 117'si çocuk olmak üzere ortalama 247 Filistinlinin öldürüldüğü ifade edildi. Birleşmiş Milletler Çocuklara Yardım Fonu (UNICEF) ise İsrail’in fiillerinin çocuklara karşı bir savaş niteliğinde olduğunu açıkladı.

Güney Afrika, ihtiyati tedbir kararı verilebilmesi için gerekli yargı yetkisinin mevcudiyetini, soykırım teşkil eden fiillerden en azından bir kısmının işlendiğini ortaya koyarak talep edilen somut tedbir kararlarını açıkladı. Bunların en başta geleni ve hiç kuşkusuz en önemlisi Mahkeme'den İsrail’in Gazze’ye yönelik askeri operasyonlarını durdurması talebidir. Güney Afrika hukuk heyetinden Profesör Vaughan Lowe, İsrail’in Filistinlilere yönelik doğrudan saldırılarında şehirleri dümdüz ettiğini, sivil unsurları ayırmadığını ve insani yardımların ulaşmasına mani olduğunu vurguladı. Güney Afrikalı heyetin sunumunu ve İsrail'in savunmasını takiben UAD davasının nasıl sonuçlanabileceği merak konusu. Bu bağlamda UAD'de daha önce görülen davalara ve alınan emsal kararlara bakmak faydalı olacaktır.

Emsal kararlar
UAD'nin önceki kararlarında, Soykırım Sözleşmesi’nin ihlal edildiği iddiasıyla yapılan başvurularda da ihtiyati tedbirlere hükmedilmişti. Örneğin, 1993 yılında Bosna Hersek'in Sırbistan aleyhine açtığı davada soykırım teşkil eden fiillerin icra edildiği hususunda ciddi bir riskin olması nedeniyle ihtiyati tedbir kararı verilmişti. Keza, 2020 senesinde Gambiya’nın Myanmar aleyhine açtığı davada Rohingya halkının telafi edilmesi mümkün olmayan ağır fiillere uğradığı gerekçesiyle de ihtiyati tedbir kararı alınmıştı. Kararda, Rohingya halkının kitlesel öldürülme, yaralanma, gıdaya erişimlerinin engellenmesi ve diğer temel ihtiyaçlardan mahrum bırakılması gerekçe gösterilmişti. Güney Afrika hukuk heyeti, Ukrayna’nın Rusya’ya karşı açtığı soykırım davasında da ihtiyati tedbir kararı verilmesini örnek vererek, Gazze’de yaşananların ihtiyati tedbire ilişkin şartları taşıdığını vurguladı.

İhtiyati tedbir kararlarının verilmesine ilişkin bir süre olmamasına rağmen, vakanın acil olma niteliği genellikle göz önünde bulunduruluyor. Gambiya’nın Myanmar aleyhine ihtiyati tedbir başvurusu 11 Kasım 2019'da yapılmıştı ve Mahkeme’den Rohingya halkına yönelik soykırım tehdidi göz önüne alınarak bir an önce karar verilmesi yolunda talepte bulunulmuştu. Bu davaya ilişkin duruşmalar, 10 Aralık 2019'da gerçekleştirildi. Mahkeme 23 Ocak 2020'de ihtiyati tedbir kararını yayınladı. Görüldüğü üzere Mahkeme genel olarak ihtiyati tedbir kararları için 1 aydan biraz fazla bir süreye ihtiyaç duyuyor. Bu noktada, Ukrayna’nın ihtiyati tedbir başvurusunun ise yalnızca 18 günde karara bağlandığı vurgulanmalıdır. Bunda Rusya’nın duruşmaya katılmamasının da etkili olduğu ileri sürülüyor. Güney Afrika’nın İsrail aleyhine yaptığı başvuruda ise İsrail duruşmaya katıldı. Buna mukabil, Mahkeme’nin 5 Şubat'tan önce ihtiyati tedbir talebine ilişkin bir karar vermesi bekleniyor. Zira, anılan tarihte UAD'de bazı hakimler emekliye ayrılacak.

Bu noktada vurgulanması gereken bir diğer husus, soykırım iddialarının esasına ilişkin davanın ise çok uzun sürmesidir. Örneğin Divan, Bosna’nın Sırbistan aleyhine açtığı davayı 14 yıl sonra ancak neticelendirebildi. Devam eden katliamların bir kez daha göz önüne serilmesi ve Filistinlilere yönelik ağır saldırıların bir an önce son bulması bakımından, ihtiyati tedbir kararı büyük önem taşıyor. İhtiyati tedbir kararına muhatap olan bir devletin, bunu yerine getirmemesi halinde UAD'nin uygulayabileceği doğrudan bir yaptırım bulunmuyor. Geçmişte bazı devletlerin ilgili kararlara kısmen veya tamamen uyduğu örnekler olduğu gibi, Mahkeme’nin kararına uymayan örnekler de bulunuyor. Bu hususta, ilgili devletin gücü ve uluslararası toplumun ilgili davaya yönelik yaklaşımı da önemli rol oynuyor.

Verilecek kararın uluslararası hukuk açısından önemi
Güney Afrika’nın böyle bir başvuruyu yapabilmesi ve insanlık adına bir mahkeme önünde Filistinlilere karşı işlenen suçları ortaya koyması büyük önem taşıyor. UAD'nin muhtemel ihtiyati tedbir kararı, uluslararası kuralların var olduğu gerçeğini göstermesi açısından da oldukça önemlidir. İsrail’in, Birleşmiş Milletler (BM) kurumları karşısındaki mutat işbirliğine yanaşmayan tutumunu terk etmek durumunda kalması ve kendisini Mahkeme önünde savunması, olası bir ihtiyati tedbir kararının hukuki ve ahlaki gücünü gösteren unsurlar arasında yer alıyor. Buna ilave olarak Uluslararası Ceza Mahkemesi'nin (UCM) vereceği adil bir ihtiyati tedbir kararının uluslararası toplumun Filistin vakasındaki tutumlarını gözden geçirmelerine vesile olabileceği değerlendiriliyor. UAD’nin, Güney Afrika’nın İsrail’e karşı açtığı davada ihtiyati tedbir kararı vermesine neredeyse kesin gözüyle bakılıyor. Bununla birlikte uluslararası hukuk kurumlarının yapısında mündemiç uluslararası siyaset olgusunun Mahkeme’yi ne derecede etkileyeceği hususu da merak konusu olmaya devam ediyor. Gerçekten Mahkeme’nin soykırım sözleşmesi kapsamındaki ihtiyati tedbir kararlarına ilişkin içtihatları değerlendirildiğinde, Gazze vakasında tedbir kararı vermemesi, bilhassa Bosna, Rohingya ve Ukrayna vakalarındaki yaklaşımıyla tezatlık teşkil edecektir. Bu nedenle mevcut tartışma Mahkeme’nin ihtiyati tedbir kararının niteliği üzerinde yoğunlaşıyor. Gerçekten Mahkeme’nin İsrail’den Gazze’ye yönelik saldırılarını derhal durdurmasını isteyip istemeyeceği, tartışmaların merkezinde duruyor. Adalet Divanı hakimleri İsrail’in saldırılarının durdurulmasını talep ettiği takdirde, bunun İsrail üzerindeki uluslararası toplum baskısını artıracağı öngörülebilir.
"""
        self.url = "/api/texts/"

    def test_create_text(self):
        response = self.client.post(self.url, {"text": self.text})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TextUpload.objects.count(), 1)

    def test_retrieve_texts(self):
        self.client.post(self.url, {"text": self.text})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class VoiceUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        # Initialize Faker
        self.fake = Faker()

        self.voice_file = SimpleUploadedFile(
            name="test_voice.mp3",
            content=b"Some audio content",
            content_type="audio/mpeg",
        )
        self.url = "/api/voices/"

    def test_create_voice(self):
        # Use Faker to generate random text
        fake_transcript = self.fake.paragraph(nb_sentences=5)

        response = self.client.post(
            self.url, {"voice_file": self.voice_file, "transcript": fake_transcript}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VoiceUpload.objects.count(), 1)

        voice_upload = VoiceUpload.objects.first()

        self.assertEqual(
            voice_upload.transcript, fake_transcript
        )  # Check if the transcript matches the fake one

    def test_retrieve_voices(self):
        fake_transcript = self.fake.paragraph(nb_sentences=5)
        self.client.post(
            self.url, {"voice_file": self.voice_file, "transcript": fake_transcript}
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        # Define the path to your media/images folder
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_image_path = os.path.join(base_dir, "media", "voices")

        # Pattern to match all files starting with 'test_' in the media/images directory
        test_files_pattern = os.path.join(media_image_path, "test_*")

        # Use glob to find all matching files
        test_files = glob.glob(test_files_pattern)

        # Remove each file
        for file in test_files:
            os.remove(file)

        super().tearDown()  # Call the tearDown method of the superclass.
