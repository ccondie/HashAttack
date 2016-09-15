import hashlib
import random
import string
import time

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


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def collision_attack(bit_len, word_len):
    words_by_hash = {}
    collision_found = False

    start = time.time()
    while not collision_found:
        word = random_word(word_len)
        word_hash = sha1_wrapper(word, bit_len)
        if word_hash in words_by_hash:
            end = time.time()
            print()
            delta = end - start
            print('COLLISION FOUND in ' + str(delta))
            print(word + ': ' + sha1_wrapper(word, bit_len))
            print(words_by_hash[word_hash] + ': ' + sha1_wrapper(words_by_hash[word_hash], bit_len))
            collision_found = True
        else:
            words_by_hash[word_hash] = word


def main():
    collision_attack(35, 30)

main()
