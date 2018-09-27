import io
import requests

def _get_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def _get_response(blob_id):
    url = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(url, params = { 'id' : blob_id }, stream = True,)
    token = _get_token(response)
    if token:
        params = { 'id' : blob_id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)
    return response

def open(blob_id):
    """ Read a file from Google Drive into memory. Returns an open (BytesIO) file-like object. """

    response = _get_response(blob_id)
    return io.BytesIO(response.content)
