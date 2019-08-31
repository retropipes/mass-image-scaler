#!/usr/local/bin/python3
# encoding: utf-8
from PIL import Image
import argparse
import os
import os.path

def scale2x(img):
    width  = img.width
    height = img.height
    #create src and dst
    src = img
    dst = img.resize((width*2, height*2))
    for x in range( width ):
        for y in range( height  ):
            dx = x*2
            dy = y*2
            x1 = x -1
            if ( x1 < 0 ): x1 = 0;
            y1 = y - 1
            if ( y1 < 0 ): y1 = 0;
            x2 = x + 1
            if x2 > width-1: x2 = width-1
            y2 = y + 1
            if y2 > height-1: y2 = height-1
            #A (-1,-1)	B (0,-1) C (1,-1)
            #D (-1,0)	E (0,0)	 F (1,0)
            #G (-1,1)   H (0,1)	 I (1,1)
            #a = src[x1,y1] #not used
            b = src.getpixel((x,y1))
            #c = src[x,y1] #not used
            d = src.getpixel((x1,y))
            e = src.getpixel((x,y))
            f = src.getpixel((x2,y))
            #g = src[x1,y2] #not used
            h = src.getpixel((x,y2))
            #i = src[x2,y2] #not used
            #E0 = D == B && B != H && D != F ? D : E;
            #E1 = B == F && B != H && D != F ? F : E;
            #E2 = D == H && B != H && D != F ? D : E;
            #E3 = H == F && B != H && D != F ? F : E;
            if ( d == b and b != h and d != f ):
                e0 = d
            else:
                e0 = e
            if ( b == f and b != h and d != f ):
                e1 = f
            else:
                e1 = e
            if ( d == h and b != h and d != f  ):
                e2 = d
            else:
                e2 = e
            if ( h == f and b != h and  d != f  ):
                e3 = f
            else:
                e3 = e
            dst.putpixel((dx,dy), e0)
            dst.putpixel((dx+1,dy), e1)
            dst.putpixel((dx,dy+1), e2)
            dst.putpixel((dx+1,dy+1), e3)
    return dst

parser = argparse.ArgumentParser(description='Resize images using the Scale2x algorithm.')
parser.add_argument('--input', '-i', required=True)
parser.add_argument('--output', '-o', required=True)
parser.add_argument('--corner-cut', '-c')
args = vars(parser.parse_args())
input = args['input']
output = args['output']
corner_cut = None
if 'corner-cut' in args:
    corner_cut = args['corner-cut']
found = 0
print('Processing images...')
with os.scandir(input) as it:
    for entry in it:
        if entry.is_file() and entry.name.endswith('.png'):
            found = found + 1
            print('Scaling image ' + str(found))
            src = Image.open(entry.path)
            if corner_cut is not None:
                src = src.crop((0, 0, corner_cut, corner_cut))
            dst = scale2x(src)
            dst.save(os.path.join(output, entry.name))
print('Done!')