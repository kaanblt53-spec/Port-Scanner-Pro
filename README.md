# Advanced Port Scanner 🚀

Bu proje, Python kullanarak geliştirilmiş, hızlı ve etkili bir ağ tarama aracıdır. Hedef IP veya domain üzerindeki açık portları tespit eder ve bu portlarda çalışan servisleri (Banner Grabbing yöntemiyle) tanımlamaya çalışır.

## Özellikler
- **Multi-threading:** `threading` kütüphanesi sayesinde çok kısa sürede binlerce portu tarar.
- **Banner Grabbing:** Açık portlardan servis versiyon bilgilerini çekmeye çalışır.
- **Servis Tanımlama:** Popüler portlar için (SSH, HTTP, SMB vb.) otomatik açıklama ekler.
- **Raporlama:** Tarama sonuçlarını otomatik olarak `bulunanlar.txt` dosyasına kaydeder.

## Kullanım
Projeyi bilgisayarınıza indirdikten sonra terminal üzerinden çalıştırabilirsiniz:

```bash
python port_scanner.py