import hashlib


def sha1_wrapper(input, bit_len):
    """
    :param input: string to hash with sha1
    :param bit_len: 1-160
    :return: sha1 hash of input truncated down to a sub_string of [0:bit_len]
    """
    h = hashlib.sha1()
    h.update(input.encode())
    digest = h.hexdigest()

    bin_digest_array = []
    for el in digest:
        bin_digest_array.append(format(int(el, 16), '04b'))

    bin_digest = ''.join(bin_digest_array)
    short_digest = bin_digest[0:bit_len]

    return short_digest


def main():
    pass


main()
