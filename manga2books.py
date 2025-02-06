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

import os
import sys
import validators
import subprocess

import convert
import download
import get_cover

def print_help():
  print("""
manga2books - A tool to download manga and convert it to EPUB format for compatibility with Apple's Books app.

Usage:
  1. Copy the Manga URL:
    - Visit the Manga Bat website: https://h.mangabat.com/
    - Find the manga you want to download.
    - Copy the manga page URL from your browser's address bar.

  2. Download the Manga:
    Run the following command, replacing <url> with the copied URL:
      manga2books <url>
    Example:
      manga2books https://readmangabat.com/read-iw386363

  3. Download Specific Chapters:
    To download a specific range of chapters, provide the chapter range after the URL:
      manga2books <url> <start-end>
    Example:
      manga2books https://readmangabat.com/read-iw386363 30-70
        
Options:
  --help, -h            Show this help message and exit.
  """)

def main():
  if len(sys.argv) != 2 and len(sys.argv) != 3:
    print_help()
    sys.exit(1)

  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
     print_help()
     sys.exit(1)

  url = sys.argv[1]
  validators.url(url)
  if not validators.url(url):
    print("Invalid URL")
    sys.exit(1)
      
  ch_range = sys.argv[2] if len(sys.argv) > 2 else None

  script_dir = os.path.dirname(os.path.abspath(__file__))
  manga_parser_path = os.path.join(script_dir, "manga_parser")

  result = subprocess.run([manga_parser_path, "-t", "{{.Number}}", url, "1"], check=True, text=True, capture_output=True).stdout.strip()
  lines = result.splitlines()
  chapters_count = float(lines[0]) if len(lines) > 0 else None
  name = lines[1] if len(lines) > 1 else None
  os.remove("1.cbz")

  if len(sys.argv) == 2 and chapters_count > 300:
    print("This manga has too many chapters. Please download it in smaller parts, e.g.:")
    print("  manga2books <manga_url> 1-300")
    print("  manga2books <manga_url> 301-___")
    sys.exit(1)

  print("Downloading imgs")
  download.download_extract(manga_parser_path, name, url, ch_range)

  print("Downloading cover img for Manga")
  get_cover.get_cover(url)

  print("Resizing imgs")
  download.resize_cut(name)

  print("Converting imgs to epub")
  convert.convert_imgs(name, "cover.webp")

  print(f"\nBook file: \033[95m{name}\033[0m, successfully created in Downloads")

if __name__ == "__main__":
	main()