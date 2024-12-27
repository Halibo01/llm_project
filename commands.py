import os
import re
import subprocess
import pytube
import requests
from bs4 import BeautifulSoup
from googlesearch import search as s
import sys

# Bu komutlar teker teker denenenebilir ve yeniden oluşturulabilir. Bu komutların model ile direkt etkileşimi yoktur yani 
# burada yapılan yanlışlar modelin yapısını etkilemez fakat modelin cevabını değiştirebilir.
# ayrıca bu komutlar herhangi bir model olmadan kullanılabilir onunu için **en aşağıdaki main yapısına bakınız**

# Model içinde en iyi sonuç veren model qwen2.5 3b coder instruct
# Model cevapları komut olarak verir ve böylelikle buradaki komutlar başka bir fonksiyon aracılığıyla çalışır


# Komutların genel yapısı: <Sınıf Fonksiyon dosya_yolu/website_linki> Argümanlar </Sınıf Fonksiyon dosya_yolu/website_linki> şeklindedir
# Arguman gerektiren modellerin arasına argümanlar yazılmalıdır yoksa komutlar düzgün çalışmayabilir.
# Arguman gerektirmeyen komutlar kapatma komutu olmadan çalışabilir. <Sınıf Fonksiyon dosya_yolu/website_linki> gibi
# Bazı komutları cevaplarla nasıl yazdırdığı örnekler şeklinde bazı komutların üst kısmında gösterilmiştir.



# Birden fazla argüman olabileceğinden ve komutların daha kolay olmasını sağlamak amacıyla komutlar bu formatta hazırlanmıştır
# Komut biçimleri değiştirilebilir çünkü komutlar tespit edilebilir olmak amacıyla bu şekilde hazırlanmıştır
# Modele her seferinde komutun çalışıp çalışmadığıyla alakalı geri bildirim verilmelidir. bundan dolayı return işlemleri her daim uygulanmalıdır.



# Boyut Hesaplama Fonksiyonu (tamamlandı)
# Komut gerektirmez
def convert_size(size_in_bytes):
    if size_in_bytes >= 1e12:
        return f"{size_in_bytes / 1e12:.2f} TB"
    elif size_in_bytes >= 1e9:
        return f"{size_in_bytes / 1e9:.2f} GB"
    elif size_in_bytes >= 1e6:
        return f"{size_in_bytes / 1e6:.2f} MB"
    elif size_in_bytes >= 1e3:
        return f"{size_in_bytes / 1e3:.2f} KB"
    else:
        return f"{size_in_bytes} bytes"
    

# İşletim sistemi işlemleri
class Os:
    def __init__(self, ip):# İp?
        pass



# Dosya İşlemleri
class File:
    def __init__(self, path):
        self.__path = path
        self.__path = os.path.abspath(self.__path)
        

    # Boyut Hesaplama
    # Çalışma şekli: <file size örnek.txt>
    def size(self):
        return f"Dosyanın boyutu: {str(convert_size(os.path.getsize(self.__path)))}"

    # Dosya Okuma
    # Çalışma şekli: <file read örnek.txt>
    def read(self):
        with open(self.__path, "r", encoding="utf-8") as file:
            content = file.read()
        return f"{self.__path} dosyasından okunan bilgiler: {content}"

    # Dosya içindeki bilgileri silip yazma
    # Çalışma şekli: <file clearwrite örnek.txt>Örnek olarak bu yazıyı içindeki bilgileri silip yazar</file clearwrite örnek.txt>
    def clearwrite(self, content):
        if not content:
            return f"Hata! '{self.__path}' Dosyasına yazılacak herhangi bir yazı bulunamadı!"
        with open(self.__path, "w", encoding="utf-8") as file:
            file.write(content)
        return f"'{self.__path}' dosyasına yazı yazımı başarılı bir şekilde yapıldı."

    # Dosyaya ek bilgi yazma
    def writemore(self, content):
        if not content:
            return f"Hata! '{self.__path}' Dosyasına ek olarak yazılacak herhangi bir yazı bulunamadı!"
        with open(self.__path, "a", encoding="utf-8") as file:
            file.write("\n" + content)
        return f"'{self.__path}' dosyasına yazı yazımı başarılı bir şekilde yapıldı."

    # Dosya yolu kontrolü
    def path(self):
        return self.__path

    # Dosya silme (Önemli dosyaları silebileceğinden aktif değildir)
    # Çalışma şekli: <file removefile test.txt>
    # def removefile(self):
    #     os.remove(self.path)


# Program Kontrol İşlemleri
class Program:
    def __init__(self, path):
        self.__path = path


    # Program Çalıştırma (yapılacak)
    # Planlanan Çalışma şekli: <program run test.exe>
    def run():
        ...


    # Python Programı Test ve Hata Kontrolü
    # Çalışma şekli: <program test test.py>
    def test(self):
        with open(self.__path, "r", encoding="utf-8") as file:
            readfile = file.read()
        try:
            
            process = subprocess.run(
                ["python", self.__path],
                capture_output=True,
                text=True
            )
            
            
            stdout_output = process.stdout
            stderr_output = process.stderr
            
            if process.returncode == 0:
                return f"{self.__path} programında yazanlar: \"{readfile}\". {self.__path} programı başarılı bir şekilde çalıştı. Program Çıktısı: {stdout_output}."
            
            else:
                return f"{self.__path} programında yazanlar: \"{readfile}\". {self.__path} programı hata verdi. Hata Çıktısı: {stderr_output}."

        except Exception as e:
            return f"Program hata Çıktısı: {str(e)}"
        

class Packagemanager:
    def __init__(self, package):
        self.package = package
        if "=" in self.package:
            self.version = self.package.split("=")[-1]

    def install(self):

        try:
            if self.version:
                subprocess.check_call([sys.executable, "-m", "pip", "install", self.package + "=" + self.version])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", self.package])
            return f"{self.package} installed successfully."
        except Exception as e:
            return f"Error installing {self.package}: {str(e)}"
        
    def uninstall(self):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", self.package])
            return f"{self.package} uninstalled successfully."
        except Exception as e:
            return f"Error uninstalling {self.package}: {str(e)}"
        
    def check(self):
        try:
            import pkg_resources
            version = pkg_resources.get_distribution(self.package).version
            return f"{self.package} version: {version}"
        except ImportError:
            return f"{self.package} is not installed."
        except Exception as e:
            return f"Error checking {self.package}: {str(e)}"
        
    def list(self):
        
        if self.package.lower() == "all":
            try:
                result = subprocess.run([sys.executable, "-m", "pip", "list"], capture_output=True, text=True)
                return result.stdout
            except Exception as e:
                return f"Error listing installed packages: {str(e)}"
    
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "show", self.package], capture_output=True, text=True)
            ret = result.stdout.strip("\n").split("\n")
            ret = ret[:2] + ret[-2:]
            ret = "\n".join(ret)
            return ret
        except Exception as e:
            return f"Error listing dependencies for {self.package}: {str(e)}"
        
    def upgrade(package_name):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
            return f"{package_name} upgraded successfully."
        except Exception as e:
            return f"Error upgrading {package_name}: {str(e)}"
        

        
# Klasör Kontrolü
class Folder:
    def __init__(self, path):
        self.__path = path
        self.__path = os.path.abspath(self.__path)

    # Klasör içindekileri görüntüleme (tamamlanmadı)
    # Çalışma şekli: <folder listpath path>
    def listpath(self):
        return os.listdir(self.__path)
    
    
# Youtube İşlemleri
class YT:
    def __init__(self, url):
        self.__url = url

    # Kanal Bilgisi Öğrenme (yapılacak)
    def channelinfo(self):
        ...

    # Video Bilgisi Öğrenme (yapılacak)
    def videoinfo(self):
        ...

    # Youtube ses/müzik yükleme (yapılacak)
    def downloadaud(self):
        ...

    # Youtube video yükleme (yapılacak)
    def downloadvid(self):
        ...

    # Ek İşlem (yapılacak)
    def connect(self):
        ...

# Linux Terminaline Yazılabilecek komutlar (planlanıyor)
class Command:
    ...


# Internet Bilgi İşlemleri
# Geliştirilmesi gerekiyor
class Internet:
    def __init__(self, url):
        self.__url = url

    # Arama Motoru Araştırma (yalnızca google)
    # Google araştırması yapar ve bulunan ilk 10 linki listeler (kurallara uygun değil)
    # Nasıl çalışacağı daha iyi planlanıyor fakat program çalışıyor
    # Örnek çalışma şekli: <internet engine google>menemen nasıl yapılır?</internet engine google>
    def engine(self, content):
        if self.__url == "google":
            links = ""
            for i in s(content, tld="co.in", num=10, stop=10, pause=2):
                links =+ i + ", "
            links[:-1]
        

    # Sitede Yazan Bilgileri Alma
    # Çalışma şekli: <internet content https://orneksite.com>
    def getcontent(self):

        response = requests.get(self.__url)
        if response.status_code != 200:
            return f"{self.__url} sitesi okuma başarısız oldu. Durum kodu: {response.status_code}"
        response.raise_for_status()  # Hata kontrolü

        soup = BeautifulSoup(response.text, "html.parser")

        yazilar = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"])
        text = ""

        for yazi in yazilar:
            text += yazi.get_text().replace("\n", " ")

        return f"'{self.__url}' sitesi başarılı bir şekilde okundu. Site içeriği: {text}"
        
    # Sitedeki html Kodlarını alma
    # Çalışma şekli: <internet gethtml https://orneksite.com>
    def gethtml(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            
            css_links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]
            print("CSS dosyaları:")
            for css_link in css_links:
                print(css_link)
                

                if not css_link.startswith("http"):
                    css_link = requests.compat.urljoin(self.__url, css_link)
                
                css_response = requests.get(css_link)
                if css_response.status_code == 200:
                    print(f"\n{css_link} içeriği:")
                    print(css_response.text)
                else:
                    print(f"{css_link} yüklenemedi.")
        else:
            print(f"HTML alınamadı. Durum kodu: {response.status_code}")


#############    MAIN YAPISI    ###########################
## ÖNEMLİ: MAIN YAPISINI KALDIRMAYINIZ YOKSA PROGRAM DÖNGÜYE GİREBİLİR!!!
# Bu komutlar yine örnek olarak yazıldığında test edilebilir.

if __name__ == "__main__":

##########################################################################################
    command = "<packagemanager list all>"    # denemek istediğiniz komutlarınızı buraya girebilirsiniz
##########################################################################################
    
    try:
        result = subprocess.run(["execute", "-C", command], capture_output=True, text=True, shell=True, check=True)
        

        print("Standart Çıktı:")
        print(result.stdout)


        if result.stderr:
            print("Hata Çıktısı:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Komut başarısız oldu: {e}")
        print(f"Çıktı: {e.output}")
        print(f"Standart Hata: {e.stderr}")



# Bu programın mantığı şu şekildedir:

# commands.py ----------- (string) ----------> execute.exe
# commands.py <----- (bulunmuş komutlar) ----- execute.exe

# Bu yapıdan dolayı bu her iki programı da çalıştırabilmek için her iki programa da ihtiyacınız var

        
    
    




            
        
        
        

        








