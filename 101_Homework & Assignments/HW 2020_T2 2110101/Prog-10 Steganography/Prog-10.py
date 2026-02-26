# Prog-10: Steganography

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename): 
    im = Image.open(filename).convert('RGB')
    return numpy.asarray(im).tolist()      

def save_image(img, filename):     
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
  
def show_image(filename):  
    im = Image.open(filename)   
    im.show()

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------
# Nothing to be defined.
# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    img = load_image(file_in)
    out = [k for i in clone_image(img) for j in i for k in j]
    if len(out) >= 48+8*(len(text)) and len(text) <= 65535:
        repl = SPECIAL_BITS+int_to_bits(len(text))+''.join([char_to_bits(i) for i in text])+SPECIAL_BITS
        for i in range(len(repl)):
            if (out[i]%2 == 0 and repl[i] == '0') or (out[i]%2 == 1 and repl[i] == '1'): out[i] += 0
            elif out[i]%2 == 0 and repl[i] == '1': out[i] += 1
            elif out[i]%2 == 1 and repl[i] == '0': out[i] -= 1
        RGB = [[out[i],out[i+1],out[i+2]] for i in range(0,len(out)-2,3)]
        embeded_img = [[RGB[i+j] for j in range(len(img[0]))] for i in range(0,len(img)*len(img[0]),len(img[0]))]
        save_image(embeded_img,file_out)
        if get_embedded_text_from_image(file_out) == text:
            return True
    else:
        return False
# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    img = load_image(file_in)
    out = [k for i in clone_image(img) for j in i for k in j]
    bits = ''.join(['0' if i%2 == 0 else '1' for i in out])
    Char_c = bits_to_int(bits[16:32])
    if bits[:16] == SPECIAL_BITS and bits[32+Char_c*8:48+Char_c*8] == SPECIAL_BITS:
        return ''.join([bits_to_char(bits[i:i+8]) for i in range(32,32+8*Char_c,8)])
    else: 
        return ''
# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
# main()
exec(open('Prog-10-test.py').read)