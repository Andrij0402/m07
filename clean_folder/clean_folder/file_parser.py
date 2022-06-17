from importlib.resources import path
import re
import sys
from pathlib import Path
from typing import Container

IMAGES = []
VIDEO = []
AUDIO = []
ARCHIVES = []
DOCUMENTS = []
OTHER = []
FOLDERS = []

REGISTER_EXTENSIONS = {
    'JPEG': IMAGES, 'JPG': IMAGES, 'PNG': IMAGES, 'SVG': IMAGES,
    'AVI': VIDEO, 'MP4': VIDEO, 'MOV': VIDEO, 'MKV': VIDEO,
    'MP3': AUDIO, 'OGG': AUDIO, 'WAV': AUDIO, 'AMR': AUDIO,
    'ZIP': ARCHIVES, 'TAR': ARCHIVES, 'GZ': ARCHIVES,
    'DOC': DOCUMENTS, 'DOCX': DOCUMENTS, 'TXT': DOCUMENTS, 'PDF': DOCUMENTS, 'XLSX':DOCUMENTS, 'PPTX': DOCUMENTS
}

EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)
    
if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'start in folder {folder_for_scan}')
    
    scan(Path(folder_for_scan))
    print(f'Images: {IMAGES}')
    print(f'Video: {VIDEO}')
    print(f'Documents: {DOCUMENTS}')
    print(f'Archives: {ARCHIVES}')
    
    print(f'Types of files in folders: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')
    
    print(FOLDERS)