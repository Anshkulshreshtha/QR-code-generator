#  import QRCode from pyqrcode

import pyqrcode

# String which represent the qr code,, here I used my css site u can use whichever u want.

site = "https://anshkulshreshtha.github.io/my-site/"

#  generate the qr code

url = pyqrcode.create(site)

# create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
