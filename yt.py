from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_vide0(url,save_path):
    try:
        yt = Youtube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
    except Exception as e:
        print(e)