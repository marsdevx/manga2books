#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⣼⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⡌⠙⢿⣿⣿⡐⣿⣷⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣹⢻⡟⡘⣿⠇⣿⣿⣿⣿⣿⣿⣿⡏⣿⠻⣿⣿⣿⣿⡌⢷⡉⢙⠀⠈⠀⡶⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠐⠀⠾⢠⣷⣜⢸⣿⣿⡇⣿⣿⣿⣿⡇⢻⣧⢻⣿⣿⣿⣷⡀⡁⠀⠁⡁⣦⣄⠁⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢀⠑⣸⡦⣈⡻⠇⢨⢹⣿⡧⣿⣿⣿⣿⡇⣘⣿⡜⣿⣿⣿⢿⢇⠀⠀⣧⢱⡹⣷⡌⠂⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⡄⡈⠻⣿⣿⣿⣿⣿⣿⠁⠌⢀⢇⡿⠀⣿⣿⡇⣦⣾⣿⣃⣿⣿⣿⣿⡇⠸⣟⢃⢛⣋⡴⠂⠎⡀⠘⣿⡌⣷⡘⣿⡄⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⡿⢀⠟⢜⣼⠀⣼⣿⣿⣿⣿⠇⠌⠀⣸⠸⡇⠀⡇⠟⣃⣿⣿⣿⢸⣿⢿⣶⣭⠁⡁⠹⡠⠌⢉⣬⣉⣀⡃⠀⠸⣷⢸⣧⡹⣷⡀⢧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    File:         download.py                                ⣿⣿⣿⣿⣿⣿⣿⣷⡈⠲⠛⢉⠀⢻⣿⣿⣿⡟⠀⣼⠀⣿⢰⡇⠀⠀⣿⡇⣿⣿⡟⢨⡿⣸⣿⡟⢠⣿⣄⠁⠀⣿⣿⣿⣿⢰⠀⠀⢿⡆⢿⣷⡙⣷⡈⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡾⠛⠻⣾⣿⣿⣿⠃⢰⡏⠠⣿⠸⣧⠀⠀⠁⠁⠹⡿⠁⣼⠃⡟⠉⠀⠒⠈⠉⠁⠀⠛⣿⣿⣿⢸⢐⠲⠘⣿⠈⣻⣷⡌⢿⡄⢾⣿⣿⣿⣿⣿⣿⣿⣿   #
#    Project:      manga2books                                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⠀⢀⣿⣿⣿⣿⢀⡿⠁⠘⣿⢨⢻⡀⠀⢦⠂⠀⠠⣤⣥⣤⣦⣶⡆⠀⠀⠙⣿⡇⢀⣿⣿⣿⡏⢐⠳⡄⢿⡇⡟⡏⢻⣆⢈⠀⠙⠛⣛⠉⢸⣿⣿⣿   #
#    Github:       marsdevx                                   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠸⠁⠀⡇⡟⠘⡘⣧⠀⢸⣇⠀⡀⢹⣿⣿⣿⣿⣧⠐⣸⠀⣽⠇⡏⣿⣿⡿⠇⢘⠵⠃⢸⡇⠃⠇⠈⡜⡄⠻⣶⣦⣤⣶⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠌⠛⠋⠀⠰⠀⠁⡇⠀⢧⠘⠧⡀⠿⢦⠡⣾⣿⣿⣿⣿⡿⢓⡿⠶⡟⠘⢰⣿⣿⢱⠀⠀⠀⠀⣼⠇⢰⠀⠀⢱⡀⢧⢹⣿⣿⣿⣿⣿⣿⣿   #
#    Created:      13:02   06/01/2025                         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⠟⠃⠀⠀⠀⠃⠀⠘⡀⠀⠀⠐⢄⣠⣿⣿⣿⣿⣿⣯⡐⣜⢂⡠⠂⣿⣿⡧⢸⠀⠀⠀⢠⠋⠀⠈⠀⠀⠘⠀⠈⢂⣿⣿⣿⣿⣿⣿⣿   #
#    Updated:      02:51   07/01/2025                         ⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠃⠆⠀⠸⠇⠀⠀⠀⠄⠥⠀⢀⠀⠀⠙⠛⠿⢶⣼⣿⡿⠿⠛⢉⣤⢰⣿⡿⠃⡇⠀⠀⠀⠀⠀⠀⠀⡴⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣭⣭⣭⡒⡄⠂⠀⠀⠀⠀⠀⠀⡀⣀⠀⢰⣿⢃⣾⠿⠁⠀⠀⠀⠀⢀⠀⠀⠠⢄⠀⠀⢀⣜⣠⣿⣿⣿⣿⣿⣿⣿⣿   #
#    Path:         ./download.py                              ⣇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⡀⠐⢂⣀⣤⣴⠊⡠⠴⠀⠉⠡⠛⠁⠀⠀⢠⡶⢀⡴⣄⡐⢶⡄⢠⡀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢡⠀⠹⢿⣿⢃⢰⣶⣥⣒⡶⠟⣓⣤⣤⡾⢋⠔⣩⣾⣿⣿⠖⣠⣾⠇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣷⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠂⠀⠀⠁⣌⢦⠙⢛⣣⣵⣾⣿⠿⢋⣐⣁⣨⣭⣭⣤⣤⣤⣤⣤⣬⣀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠄⠀⠀⣫⡕⣬⣓⡲⣶⠖⠂⡄⠛⠉⠙⣿⣿⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⢰⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠐⠀⠀⣿⣿⠸⣿⠟⣱⣾⡆⢱⢠⢰⠈⠉⣀⣤⢠⣤⣤⠔⣠⣶⡀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠈⣷⡈⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠁⠈⢿⠿⠿⠈⢺⣿⣿⣷⠈⡌⢸⠀⣿⣿⠇⣾⡟⢁⠠⠤⠄⠠⢀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡐⡄⠰⢊⣀⣀⡛⠻⣿⡿⠀⡇⠆⠀⠿⠋⠀⠋⠀⠤⣴⣶⣶⢶⣤⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢱⠀⠚⠉⣩⡶⠀⢀⠀⠀⢀⠀⠠⣀⣀⠀⠀⠀⢐⣄⠀⠀⠀⠈⢂⠀⢨⣿⣿⣿⣿⣿⣿⣿   #

import os
import math
import zipfile
import subprocess
from PIL import Image

def download_extract(url):

  temp_path = os.path.expanduser("~/Desktop/Projects/manga2books/temp")
  os.makedirs(temp_path, exist_ok=True)

  command = ["./manga_parser", url, "-o", temp_path, "-t", "{{.Number}}"]
  manga_name = subprocess.run(command, check=True, text=True, capture_output=True).stdout.strip()

  manga_path = os.path.expanduser(f"~/Desktop/Projects/manga2books/{manga_name}")
  os.rename(temp_path, manga_path)

  for filename in os.listdir(manga_path):
    if filename.endswith(".cbz"):
      cbz_path = os.path.join(manga_path, filename)
      target_folder = os.path.join(manga_path, os.path.splitext(filename)[0])
      with zipfile.ZipFile(cbz_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)
      os.remove(cbz_path)

def resize_cut(manga_path):

  manga_path = os.path.expanduser(manga_path)
  max_height = 1500

  for root, _, files in os.walk(manga_path):
    for file in files:
      file_path = os.path.join(root, file)
      if file.lower().endswith(('.png', '.jpg', '.jpeg', '.img', '.tiff', '.bmp', '.gif')):
        img = Image.open(file_path)
        img_width, img_height = img.size

        split_count = math.ceil(img_height / max_height)
        split_height = math.ceil(img_height / split_count)

        base_name, ext = os.path.splitext(os.path.basename(file_path))
        base_dir = os.path.dirname(file_path)

        for i in range(split_count):
          top = i * split_height
          bottom = min((i + 1) * split_height, img_height)
          cropped_img = img.crop((0, top, img_width, bottom))

          split_name = f"{base_name},{i + 1}{ext}"
          save_path = os.path.join(base_dir, split_name)
          cropped_img.save(save_path)

        os.remove(file_path)

download_extract("https://readmangabat.com/read-eo409007")
resize_cut("~/Desktop/Projects/manga2books/Childhood Friend Of The Zenith")