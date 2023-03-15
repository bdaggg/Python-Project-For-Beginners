import pyqrcode
import png
from pyqrcode import QRCode

x = input("enter the address you want to make a url: ") # the url received from the user was assigned to the s variable.
url = pyqrcode.create(x)
url.png('myqrcode.png', scale = 6)