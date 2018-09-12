import io
import requests

def _get_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def open_gdrive_file(blob_id):
    """ Read a file from Google Drive into memory. Returns an open (BytesIO) file-like object. """
    
    url = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(url, params = { 'id' : blob_id }, stream = True,)
    token = _get_token(response)
    if token:
        params = { 'id' : blob_id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)
    file_bytes = response.content
    return io.BytesIO(file_bytes)