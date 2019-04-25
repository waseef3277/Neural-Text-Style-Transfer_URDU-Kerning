import json
import hashlib

def get_font_infos():
    with open('../../shared-data/font_infos.json', 'r') as f:
        font_infos = json.load(f)

    return font_infos

def font_path_to_hex_hash(font_path):
    def baseN(num,b,numerals):
        return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

    original_hash = hashlib.sha1(font_path).hexdigest()

    chars = list ()

    with codecs.open ('charsets/urduCharsetdeg2.txt', 'r', encoding="utf-8") as f:
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

def get_z_space_dict(dimensionality):
    # This returns a dict which maps from the img-hash to it's coordinates in the Z space
    z_space_dict = {}

    with open('../../shared-data/tsne_dump_{0}d_48px.json'.format(dimensionality), 'r') as f:
        tsne_dump = json.load(f)

    Z = tsne_dump['Z']

    img_names = tsne_dump['img_names']
    img_hashes = [name[:-4] for name in img_names]

    for i, img_hash in enumerate(img_hashes):
        z_space_dict[img_hash] = Z[i]

    return z_space_dict

