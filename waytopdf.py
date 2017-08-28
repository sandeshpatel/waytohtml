#!/usr/bin/env python3
import os
import pdfkit

files_n_dir = os.listdir()
files = [file for file in files_n_dir if file.endswith('html')]
for file in files:
    file_name = file.rstrip('html') + 'pdf'
    # load webpage and convert to pdf, here file serve as url
    pdfkit.from_url(file, file_name)

