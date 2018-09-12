# driveanon
This is a Python module that provides easy access to publicly shared Google Drive files through reference by blob id.

## Installation
Until we get this up on PyPI, the easiest way to install this is to clone the repo, move into the top directory of the repo, and then:
```
pip install -e .
```

## Basic Usage
```
import driveanon as da
blob_id = '1oq2pdwsDSKJEWmj8Ly6EvBv55MqYpZy-'
f = da.open_file(blob_id)
print(f.readline())
```

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
