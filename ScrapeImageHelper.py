from PIL import Image
import requests
from io import BytesIO

def read_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

