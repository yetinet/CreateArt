#!/usr/bin/env python3

from helperFunctions import *
from nstFunctions import *

def main():
    content_image = sys.argv[1:][0]
    style_image = sys.argv[1:][1]


    model_nn(content_image, style_image)

    return


if __name__== "__main__":
  main()

# Invoke like
# parameters are content image path, style image path, output directory, number of training iterations, alpha for cost, beta for cost
# python3 CreateArt.py images/content/ventana-circle_300_400.jpg images/style/TheScream_300_400.jpg ~/CreateArt/output 300 10 40
