#                                                             ⣛⣛⣛⣛⣛⣛⡛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣉⣉⣉⣙⣛⣛⣛⣛⣛⡛⠛⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    File:         split.py                                   ⣿⣿⣿⣿⡿⣻⡽⠟⠒⠒⠪⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⣛⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶    #
#                                                             ⣿⣿⡿⣣⠌⠁⢀⣤⠀⠀⠀⠙⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠲⠿⠙⣙⣻⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    Project:      manga2books                                ⣿⣟⠻⠂⠀⣴⣿⢏⡀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢀⣤⣤⢀⣀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠾⠽⠛⢻⣿⣿⣿⣿⣿⣿    #
#    Github:       marsdevx                                   ⡌⠉⠃⠀⣼⣿⡿⣘⣛⡣⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⢸⣿⠿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣾⣯⣿⠿⣿⣿    #
#                                                             ⣿⣦⣄⠀⣿⣿⣿⣿⣿⣿⡆⠀⠀⢢⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢀⣴⣿⣿⣿⣿⣟⣼⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⢀⣴⣿⣿    #
#    Created:      15:35   06/01/2025                         ⣿⣿⣿⣦⢻⣿⣿⣿⣿⣿⡇⠀⠀⢼⡃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⢰⣶⣶⣄⠀⢀⣴⣿⣿⣿⣿    #
#    Updated:      15:35   06/01/2025                         ⣿⣿⣿⣿⡏⣿⣿⣏⢭⣵⣄⣀⣴⣯⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣇⠸⢿⣿⣮⡻⣿⣿⣿⢟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡩⣟⣛⣛⣫⣦⣄⣀⣴⣎⢮⡻⣿⡟⣠⣿⣿⣿⣿⣿⣿    #
#    Path:         ./split.py                                 ⣿⣿⣿⣿⣿⣿⣷⣶⣭⣭⣄⣉⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣞⡿⢊⣼⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣙⠿⣿⣿⣿⣿⣿⡿⠛⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣦⣤⣬⣭⣍⣀⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #

import os
import math
from PIL import Image

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

resize_cut("~/Desktop/Projects/manga2books/Childhood Friend Of The Zenith")