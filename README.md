# Fat Photo

Store any file inside of a GIF file. The output GIF will be viewable as the original GIF as well
as able to be unzipped.


### Usage 
```
usage: fatphoto.py [-h] [--gif-source GIF_SOURCE] [--output OUTPUT_DIR]
                   [--verbose]
                   file
```

Example:
```
./fatphoto.py test.pdf --gif-source cool.gif
unzip test.pdf
```

__Note: You may get a warning when unzipping about junk data at the beginning of the file. This
can be ignored.__
