import streamlit as st
import os
import requests
from tqdm import tqdm

def file_exists(filepath):
    return os.path.isfile(filepath)

def download_file(url, filepath):
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = st.progress(0)
    with open(filepath, 'wb') as file, tqdm(
        desc=filepath,
        total=total_size_in_bytes,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))
            progress_bar.progress(min(int(bar.n / total_size_in_bytes * 100), 100))
    progress_bar.empty()
