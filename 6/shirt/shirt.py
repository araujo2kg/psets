import sys
import os
from PIL import Image, ImageOps


def main():
    overlay_shirt(sys_check(sys.argv))


def sys_check(filenames):
    if len(filenames) != 3:
        sys.exit("Incorrect number of arguments.")
    elif (
        filenames[1].lower().endswith((".jpg", ".jpeg", ".png")) == False
        or filenames[2].lower().endswith((".jpg", ".jpeg", ".png")) == False
    ):
        sys.exit("Incorrect extension.")
    elif filenames[1][-4:] != filenames[2][-4:]:
        sys.exit("Extensions don't match.")
    elif os.path.exists(filenames[1]) == False:
        sys.exit("File does not exist.")
    else:
        return sys.argv


def overlay_shirt(filenames):
    inputimage = Image.open(filenames[1])
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    inputimage = ImageOps.fit(inputimage, size=shirt_size)
    inputimage.paste(shirt, shirt)
    inputimage.save(filenames[2])


if __name__ == "__main__":
    main()
