import pyqrcode

url = input("Lütfen QR kod oluşturmak istediğiniz url adresini giriniz:")

qr_code=pyqrcode.create(url)

qr_code.svg('qrcode.svg',scale=5)