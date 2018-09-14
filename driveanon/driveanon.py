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

def extract_file_indices(content_block, extension):
    # split up content up by common seperating character string
    all_elements = str(content_block[0]).split('\\x22')
    # extract indices for each extension occurance
    file_indices = [i for i, s in enumerate(all_elements) if extension in s]
    return file_indices, all_elements

def get_file_blobs(all_elements, indices):
    file_names = []
    blob_ids = []
    # iterate over indices of file names
    for ind in indices:
        # extract file name
        file_names.append(all_elements[ind])
        # extract blob id, which occurs 4 indices before the file name
        blob_ids.append(all_elements[ind-4])
    files_and_blobs = dict(zip(file_names, blob_ids))
    return files_and_blobs