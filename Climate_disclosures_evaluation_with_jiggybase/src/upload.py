
import os
import jiggybase
from typing import Optional

def initialize_jiggybase(org_name: str, collection_name: str):
    jb = jiggybase.JiggyBase()
    org = jb.get_org(org_name)
    collection = org.collection(collection_name)
    return jb, org, collection

def upload_file(collection, filename: str):
    print(f'Uploading {filename}')
    try:
        upsert_rsp = collection.upsert_file(filename)
    except IOError:
        print(f'File {filename} not accessible.')
        return
    except Exception as e:
        print(f'Error on {filename}: {e}')
        return

    doc_id = upsert_rsp.ids[0]
    dcl =  collection.get_doc(doc_id)
    text_len = len(" ".join([dc.text for dc in dcl]))
    title = dcl[0].metadata.title if dcl[0].metadata.title else "Unknown Title"
    print(f'Processed {filename}: "{title}"  {text_len//1024} KB text ({len(dcl)} chunks)')

def upload_directory(collection, dirname: str):
    for fn in os.listdir(dirname):
        fn = os.path.join(dirname, fn)
        upload_file(collection, fn)

def upload_content(collection, path: str):
    if os.path.isfile(path):
        upload_file(collection, path)
    elif os.path.isdir(path):
        upload_directory(collection, path)
    else:
        print(f"The path provided is not a valid file or directory: {path}")
