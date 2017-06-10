# Fat Photo

Store any file inside of a GIF file. The output GIF will be viewable as the original GIF as well
as able to be unzipped.

Tested and working on Ubuntu Linux with Python 2.7

### Example
```bash
# Create the new gif/pdf file
./fatphoto.py test.pdf --gif-source cool.gif
# Retrieve the original file
unzip test.pdf.gif
```

__Note: You may get a warning when unzipping about junk data at the beginning of the file. This
can be ignored.__

### Usage 
```
usage: fatphoto.py [-h] [--gif-source GIF_SOURCE] [--output OUTPUT_DIR]
                   [--verbose]
                   file
```

