#                                                                                         ⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⢟⡋⠋⠁⠀⢀⣬⢟⣿⣿⣿⣿⣟⡻⣾⡿⣿⣿    #
#                                                                                         ⣿⣿⣿⣿⣿⣌⠂⢂⣿⣿⢟⡵⠋⠀⠀⠀⠞⣩⣾⠿⢛⡩⣠⣾⢟⣿⢦⡀⠈⠻    #
#                                                                                         ⣿⣿⣯⢿⣿⣿⣿⣿⡟⠁⠀⠀⡂⠀⠀⠀⠚⣩⠄⠐⢁⣼⣿⢫⢿⣿⠈⡇⡀⠀    #
#                                                                                         ⣿⣿⣿⡏⣿⣿⣿⡟⡠⠀⣼⡿⠁⠀⣠⣴⡿⢁⡴⠁⣼⠟⢁⡏⢸⢸⠀⠀⢡⠀    #
#    File:         download.py                                                            ⣿⣿⢛⠷⢿⣿⡿⣰⠃⠘⢋⠃⣠⣾⣿⣿⢁⣾⠁⢸⠏⡀⣼⡁⠀⠈⠀⠀⠸⡀    #
#                                                                                         ⣿⣿⣎⣃⣵⣿⣻⢣⠀⠀⢀⣼⣷⣾⣿⡇⣾⡟⢀⠏⡐⣼⣿⣧⠀⠀⠀⠀⠀⣇    #
#    Project:      manga2books                                                            ⣿⣿⣿⣿⣿⣿⢧⢿⠇⠀⠎⢛⡋⠻⣿⣷⣿⣧⠈⣰⣳⣝⢿⣿⡀⠀⠀⠀⢠⢻    #
#    Github:       marsdevx                                                               ⣿⣿⣿⣿⡿⠳⣳⠋⠀⠀⣼⠋⠀⠠⢸⣿⣿⣿⣠⣿⣿⣿⣷⣝⡷⠀⢠⠀⢨⢸    #
#                                                                                         ⣿⣿⡿⢋⢄⠞⠁⣠⡆⢸⣿⢸⡻⡀⣸⣿⣿⣿⣿⣿⣿⠂⠉⠻⢿⣧⡈⢆⠀⠀    #
#    Created:      13:02   06/01/2025                                                     ⣿⣿⠘⠁⢀⣴⣾⡿⢣⣦⢻⣬⣯⣾⣿⣿⣿⣿⣿⣿⢃⣤⣄⠠⣤⠹⣷⡈⠀⠀    #
#    Updated:      13:03   06/01/2025                                                     ⠋⠁⠠⠊⠀⠀⠀⠾⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢘⣟⣫⢆⣿⡇⣿⠃⠀⠀    #
#                                                                                         ⣀⢂⡔⢶⣿⠟⣫⣾⢿⣪⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣩⣵⣿⣿⡵⠁⡀⢀⣶    #
#    Path:         ./download.py                                                          ⣿⣾⣿⢆⡗⣾⣯⣷⡿⢟⣯⣾⣻⣞⢿⢿⣿⣿⣿⣿⣿⣿⣿⣟⣉⡤⢗⣵⣿⣿    #
#                                                                                         ⣿⣿⢣⣿⣷⠽⣿⣿⣿⣿⢟⣯⣶⢹⣿⠿⡿⠿⠿⠿⢿⣿⣿⠿⣋⠾⢿⣛⣿⣿    #
#                                                                                         ⣿⣷⣿⣿⣿⢸⣮⡻⣿⣿⣿⣿⠍⡚⢱⣿⡏⣿⡇⣿⡿⣶⣦⠀⠘⠿⠿⠽⠛⠃    #
#                                                                                         ⣿⣿⣿⣹⣾⣼⣿⣿⣷⣭⣭⣵⠇⣥⣾⣿⣿⣿⣿⣿⣿⣿⢣⣾⣿⣿⣿⣿⣷⣥    #
#                                                                                         ⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⡿⣴⡹⣿⣿⣿⣿⣿⣿⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                                                         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣽⣿⣿⣯⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿    #

import os
import zipfile
import subprocess

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

download_extract("https://readmangabat.com/read-eo409007")