#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠁⠀⠀⠀⠀⠈⠉⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    File:         convert.py                                 ⣿⣿⣿⣿⣿⡿⠟⢋⣁⣠⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣈⡙⠻⢿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣧⣴⣾⣿⣿⡿⠿⠛⠉⠩⠭⠭⢍⣉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣉⡩⠭⠭⠍⠉⠛⠿⢿⣿⣿⣷⣦⣽⣿⣿⣿⣿   #
#    Project:      manga2books                                ⣿⣿⣿⣿⣿⣿⣿⠟⡩⠔⠈⠀⠀⠀⠀⠀⠀⠉⠛⢦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⡴⠛⠁⠀⠀⠀⠀⠀⠀⠁⠢⢍⠻⣿⣿⣿⣿⣿⣿⣿   #
#    Github:       marsdevx                                   ⣿⣿⣿⠻⠿⠟⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠙⠌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠠⠋⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⢄⠻⠿⠛⣿⣿⣿   #
#                                                             ⣿⣿⣿⣷⣠⠀⠀⠀⢀⡄⠀⠀⠀⣼⣿⣿⣿⣿⣦⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⠀⠀⠀⣴⣿⣿⣿⣿⣧⠀⠀⠀⢠⡀⠀⠀⠠⣄⣾⣿⣿⣿   #
#    Created:      00:54   07/01/2025                         ⣛⠛⠉⠉⠀⠀⠀⢠⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢰⣿⣿⣿⣿⣿⣿⠆⠀⠀⠈⣷⡄⠀⠀⠀⠉⠙⠛⣛   #
#    Updated:      00:54   07/01/2025                         ⣿⣿⣿⣿⣿⡄⠠⣿⣿⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢿⣿⣿⣿⣿⡿⠀⠀⠀⠀⣿⣿⠀⢠⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣄⠹⣿⡆⠀⣠⡀⠀⠙⠛⠛⠋⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢀⡈⠛⠛⠛⠋⠀⠀⠀⠀⢸⣿⠏⣠⣿⣿⣿⣿⣿⣿   #
#    Path:         ./convert.py                               ⣿⣿⣿⣿⣿⣿⣿⣦⣽⣿⣦⡿⠿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣾⣿⠄⠀⠀⠀⠀⠀⠀⣰⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢷⣄⣀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡀⠀⠀⠀⣀⣤⡾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣤⠉⠙⠛⠛⠛⢛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡛⠛⠛⠛⠉⠁⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #

import os
import sys
import random
from PIL import Image
from ebooklib import epub
from natsort import natsorted

def make_ch(chapter_title, image_paths, chapter_file_name):

  chapter = epub.EpubHtml(
    title=chapter_title,
    file_name=chapter_file_name,
    lang="en"
  )

  chapter_content = [
    "<html>",
    "  <head>",
    "    <meta charset='utf-8' />",
    "    <style>",
    "      body { margin: 0; padding: 0; text-align: center; }",
    "      img { max-width: 100%; height: auto; margin: 10px auto; display: block; }",
    "    </style>",
    "  </head>",
    "  <body>",
    f"    <h1>{chapter_title}</h1>"
  ]

  items_to_add = []

  for idx, img_path in enumerate(image_paths, start=1):
    ext = os.path.splitext(img_path)[1].lower()
    with open(img_path, "rb") as f:
      img_data = f.read()

    img_filename = f"images/{chapter_file_name}_img_{idx}{ext}"
    img_item = epub.EpubItem(
      uid=f"{chapter_file_name}_img_{idx}",
      file_name=img_filename,
      media_type="image/jpeg",
      content=img_data
    )

    items_to_add.append(img_item)
    chapter_content.append(
      f"    <div class='page-break'><img src='{img_filename}' alt='Page {idx}'/></div>"
    )

  chapter_content += [
    "    <div style='height:50px;'></div>",
    "  </body>",
    "</html>"
  ]

  chapter.content = "\n".join(chapter_content)
  return chapter, items_to_add

def convert_imgs(path):

  path = os.path.expanduser(path)
  manga_name = os.path.basename(os.path.normpath(path))
  output_dir = os.path.expanduser(f"~/Downloads/{manga_name}.epub")
  chapters = natsorted(os.listdir(path))

  if not os.path.isdir(path):
    print(f"Error: {path} is not a valid directory.")
    sys.exit(1)
  
  book = epub.EpubBook()
  book.set_identifier(str(random.randint(100000, 999999)))
  book.set_title(manga_name)
  book.set_language("en")
  book.add_author("manga2books")

  chapters_list = []
  for i, chapter_name in enumerate(chapters, start=1):
    chapter_dir = os.path.join(path, chapter_name)
    image_files = sorted(os.path.join(chapter_dir, fname) for fname in os.listdir(chapter_dir))
    chapter_title = f"Chapter {chapter_name.strip('()')}"
    chapter_filename = f"chapter_{i}.xhtml"
    chapter_obj, image_items = make_ch(chapter_title, image_files, chapter_filename)
    book.add_item(chapter_obj)
    for item in image_items:
      book.add_item(item)
    chapters_list.append(chapter_obj)

  book.add_item(epub.EpubNcx())
  book.add_item(epub.EpubNav())
  book.spine = chapters_list
  book.toc = [epub.Link(chap.file_name, chap.title, f'chap_{i}') for i, chap in enumerate(chapters_list, start=1)]

  epub.write_epub(output_dir, book, {})