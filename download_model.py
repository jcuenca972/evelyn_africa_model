import streamlit as st
import os
import requests
from tqdm import tqdm

def file_exists(filepath):
    return os.path.isfile(filepath)

def download_file(url, filepath):
    response = requests.get(url, stream=True)
    block_size = 1024
    with open(filepath, 'wb') as file, tqdm(
        desc=filepath,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))
