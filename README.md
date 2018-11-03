# driveanon
This is a Python module that provides easy anonymous access to publicly shared Google Drive files via blob id. We are in the early stages so this is pretty basic, but we hope to add functionality soon!

## Installation
Until we get this up on PyPI, the easiest way to install this is to clone the repo, move into the top directory of the repo, and then:
```
pip install -e .
```

## Basic Usage
### Sharing Requirements
driveanon only works with files on Google Drive that have sharing on, for "Anyone with the link" or "Public on the web". Any other sharing that requires a sign in will not work with driveanon.
### Opening Files
```python
import driveanon as da
blob_id = '1oq2pdwsDSKJEWmj8Ly6EvBv55MqYpZy-'
f = da.open(blob_id)
print(f.readline())
```
`driveanon.open(blob_id)` returns an in-memory open (BytesIO) file-like object. If the file is very large your memory may page or it may not work at all. We are currently working on a lazy (out-of-memory) file loading capability.
### Saving Files
```python
import driveanon as da
blob_id = '1oq2pdwsDSKJEWmj8Ly6EvBv55MqYpZy-'
da.save(blob_id)
```
`driveanon.save(blob_id, filename=None, overwrite=False)` saves a file to the local disk. If no filename is passed, the file will be named as it is named on Google Drive.

## Getting Blob Ids
One way to get a list of blob ids using authentication is with [rclone](https://rclone.org). See the rclone docs on how to install and configure this tool. To get a list of files and blob ids from a remote, use:
```
rclone lsf --format pi --csv remote:path
```
We are currently working on ways to get a list of blob ids without authentication.

## To Do
  1. Anonymous blob id listing
  2. File save-to-disk function
  3. Lazy (out of memory) file loading
