import pyqrcode
import png
from pyqrcode import QRCode

#O link que você deseja transformar em Qrcode
link = str(input('Qual url você transformar em códigoQR? '))
QrString = f'{link}'

# Cria o Qrcode
url = pyqrcode.create(QrString)

# Salva o QR no local escolhido
url.png(r'qr.png', scale=8)