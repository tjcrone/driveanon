import io
import requests
from bs4 import BeautifulSoup

def _get_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def open_file(blob_id):
    """ Read a file from Google Drive into memory. Returns an open (BytesIO) file-like object. """
    
    url = 'https://docs.google.com/uc?export=download'
    session = requests.Session()
    response = session.get(url, params = { 'id' : blob_id }, stream = True)
    token = _get_token(response)
    if token:
        params = { 'id' : blob_id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)
    file_bytes = response.content
    return io.BytesIO(file_bytes)

def request_folder_blob(blob_id):  
    url = "https://drive.google.com/drive/folders/%s" % blob_id
    session = requests.Session()
    response = session.get(url, params = { 'usp' : 'sharing' })
    html_response = BeautifulSoup(response.text, 'html.parser')
    return html_response
    
def find_content_block(html_response, extension):
    content_block = []
    for element in html_response.find_all('script'):
        if extension in element.text: 
            content_block.append(element)
    return content_block