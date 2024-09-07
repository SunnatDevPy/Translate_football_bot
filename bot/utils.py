import cairosvg
import requests
from PIL import Image
from io import BytesIO


def upload_file(img_bytes):
    url = 'https://telegra.ph/upload'
    response = requests.post(url, files={'file': img_bytes})
    if response.status_code == 200:
        return "https://telegra.ph" + response.json()[0]['src']
    print(f"Error uploading file: {response.status_code}")
    return


def bytes_omg(url):
    response = requests.get(url)

    png_data = cairosvg.svg2png(bytestring=response.content)
    img = Image.open(BytesIO(png_data))
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io
