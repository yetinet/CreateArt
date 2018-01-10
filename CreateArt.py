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
# python3 CreateArt.py ~/CreateArt/images/louvre_small.jpg  ~/CreateArt/images/monet.jpg ~/CreateArt/output 200 10 40
