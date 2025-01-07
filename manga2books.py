#                                                                                         ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷    #
#                                                                                         ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇    #
#    File:         manga2books.py                                                         ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽    #
#                                                                                         ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕    #
#    Project:      manga2books                                                            ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕    #
#    Github:       marsdevx                                                               ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕    #
#                                                                                         ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄    #
#    Created:      03:18   07/01/2025                                                     ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕    #
#    Updated:      03:18   07/01/2025                                                     ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿    #
#                                                                                         ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    Path:         ./manga2books.py                                                       ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟    #
#                                                                                         ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠    #
#                                                                                         ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙    #
#                                                                                         ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣    #

import sys
import os
import subprocess

import convert
import download
import get_cover

def main():
  if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: manga2books <manga_url>")
    sys.exit(1)

  url = sys.argv[1]
  ch_range = sys.argv[2] if len(sys.argv) > 2 else None

  result = subprocess.run(
  ["./manga_parser", "-t", "{{.Number}}", url, "1"],
  check=True,
  text=True,
  capture_output=True
  ).stdout.strip()

  lines = result.splitlines()
  chapters_count = int(lines[0]) if len(lines) > 0 else None
  name = lines[1] if len(lines) > 1 else None
  os.remove("1.cbz")

  if len(sys.argv) == 2 and chapters_count > 300:
    print("This manga has too many chapters. Please download it in smaller parts, e.g.:")
    print("  manga2books <manga_url> 1-300")
    print("  manga2books <manga_url> 301-___")
    sys.exit(1)

  print("Downloading imgs")
  download.download_extract(name, url, ch_range)

  print("Downloading cover img for Manga")
  get_cover.get_cover(url)

  print("Resizing imgs")
  download.resize_cut(name)

  print("Converting imgs to epub")
  convert.convert_imgs(name, "cover.webp")

  print(f"\nBook file: {name}, successfully created in Downloads")

if __name__ == "__main__":
	main()