import io
import requests

def _get_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def _is_folder(response):
    if 'P3P' in response.headers:
        return True
    else:
        return False

def _get_response(blob_id):
    session = requests.Session()
    url = 'https://drive.google.com/open'
    response = session.get(url, params = { 'id' : blob_id })

    if _is_folder(response):
        return response

    url = "https://docs.google.com/uc?export=download"
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

def save(blob_id, filename = None, overwrite = False):
    """ Save a file from Google Drive to disk."""

    # get response
    response = _get_response(blob_id)

    # parse filename
    if not filename:
        filename = response.headers['Content-Disposition'].split('=')[1].split('"')[1]

    # check if filename is a file
    from pathlib import Path
    p = Path(filename)
    if p.is_file() and not overwrite:
        raise FileExistsError('File exists: %s' % filename)

    # write file
    import builtins
    with builtins.open(filename, 'wb') as w:
        w.write(response.content)
