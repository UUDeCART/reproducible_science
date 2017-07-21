import argparse
import skimage.io as io 
from skimage.filters import sobel


def edge_detector(input_file, output_file):
    # Read the image from the file
    img = io.imread(input_file)
    edge_img = sobel(img)
    io.imsave(output_file, edge_img)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='edgy', description='computes an edge image')

    parser.add_argument('--input', help='The path to the input image.', required=True)
    parser.add_argument('--output', help='Where to write the output image.', required=True)

    args = parser.parse_args()

    edge_detector(args.input, args.output)
