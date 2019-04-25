# -*- coding: utf-8 -*-

import json
import hashlib
import codecs

def get_font_infos():
    with open('../../shared-data/font_infos.json', 'r') as f:
        font_infos = json.load(f)

    return font_infos

def font_path_to_hex_hash(font_path):
    def baseN(num,b,numerals):
        return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

    original_hash = hashlib.sha1(font_path).hexdigest()

    chars = list ()

    with codecs.open ('charsets/urduCharset3d.txt', 'r', encoding="utf-8") as f:
        for line in f:
            line = u"%s" % line
            # char = line.split()[0]
            reshaped_text = reshaper.reshape (line)
            artext = get_display (reshaped_text)
            chars.append (artext)


    numerals = chars
    #numerals = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # len = 62
    large_num_almost_prime = 15485867 * 32452843
    # large_num_almost_prime = 202357 * 202361
    hash_int = int(original_hash, 16) % large_num_almost_prime
    truncated_hash = baseN(hash_int, len(numerals), numerals)

    return truncated_hash
