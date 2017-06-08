#! /usr/bin/env python

import argparse
import os
import shutil
import zipfile
import time

# Config
WORK_DIR = '.data/'
DEFAULT_GIF = 'cool.gif'


# Parse arguments
parser = argparse.ArgumentParser(description='Save any file in a GIF. Openable with both the GIF and ZIP archiver.')
parser.add_argument('file', help='File you want to hide in a GIF (required)')
parser.add_argument('--gif-source', dest='gif_source', default=DEFAULT_GIF, help='The GIF you want to append to')
parser.add_argument('--output', dest='output_dir', help='The output directory')
parser.add_argument('--verbose', dest='verbose', action='store_true', help='Display debug information')
parser.set_defaults(verbose=False)
args = parser.parse_args()


def print_v(message):
    # Print out debug message if in verbose mode
    if args.verbose:
        print(message)


# Determine the final location and name of file
file_basename = os.path.basename(args.file)
output_filename = file_basename + '.gif'
if args.output_dir:
    if args.output_dir.endswith('/'):
        output_dir = args.output_dir
    else:
        output_dir = args.output_dir + '/'
    output_filename = output_dir + file_basename + '.gif'


# Create WORK_DIR if doesn't exist
if not os.path.exists(WORK_DIR):
    print_v("Creating work directory because it doesn't exist")
    os.makedirs(WORK_DIR)


# Zip up given file
print_v('Zipping up file')
timestamp = time.time()
temp_zip_filename = WORK_DIR + file_basename + str(timestamp) + '.zip'
new_zip = zipfile.ZipFile(temp_zip_filename, 'w')
new_zip.write(args.file, compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()


# Concatenate ZIP to end of GIF
print_v('Appending ZIP to end of GIF')
with open(output_filename, "w") as output_file, \
     open(args.gif_source, "r") as gif_file, \
     open(temp_zip_filename, "r") as temp_zip_file:
    shutil.copyfileobj(gif_file, output_file)
    shutil.copyfileobj(temp_zip_file, output_file)


# Cleanup zip file
print_v('Cleaning up')
os.remove(temp_zip_filename)
print('Finished! File located at ' + output_filename)
