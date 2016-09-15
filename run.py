import hashlib
import random
import string
import time


def sha1_wrapper(input, bit_len):
    """
    takes in a string of any length and returns a truncated version of the digest

    :param input: string to hash with sha1
    :param bit_len: 1-160
    :return: sha1 hash of input truncated down to a sub_string of [0:bit_len]
    """
    h = hashlib.sha1()
    h.update(input.encode())
    digest = h.hexdigest()

    bin_digest = hexdigest_to_string(digest)
    short_digest = bin_digest[0:bit_len]

    return short_digest


def hexdigest_to_string(digest):
    bin_digest_array = []
    for el in digest:
        bin_digest_array.append(format(int(el, 16), '04b'))
    return ''.join(bin_digest_array)


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def collision_attack(bit_len, word_len):
    words_by_hash = {}

    start = time.time()
    word_count = 0
    while True:
        word = random_word(word_len)
        word_hash = sha1_wrapper(word, bit_len)
        word_count += 1

        if word_hash in words_by_hash:
            delta = time.time() - start
            # print()
            # print('COLLISION FOUND in ' + str(delta) + ' after ' + str(word_count) + ' tries')
            # print(word + ': ' + sha1_wrapper(word, bit_len))
            # print(words_by_hash[word_hash] + ': ' + sha1_wrapper(words_by_hash[word_hash], bit_len))
            return delta, word_count
        else:
            words_by_hash[word_hash] = word


def pre_image_attack(match_hash_str, hash_len, word_len):
    """

    :param match_hash_str: string value pre-hashing
    :param hash_len: truncation length of the sha1 output from match_hash_str
    :param word_len: word size to gen words to check for matching hashes
    :return:
    """
    match_hash_bin = sha1_wrapper(match_hash_str, hash_len)

    start = time.time()
    word_count = 0
    while True:
        word = random_word(word_len)
        word_hash = sha1_wrapper(word, hash_len)
        word_count += 1

        if word_hash == match_hash_bin:
            delta = time.time() - start
            # print()
            # print('MATCH FOUND in ' + str(delta) + ' after ' + str(word_count) + ' tries')
            # print('matched word: ' + word)
            # print('matched hash: ' + sha1_wrapper(word, hash_len))
            # print('inputed hash: ' + match_hash_bin)
            return delta, word_count


def main():
    test_bit_length = 0
    while True:
        with open('output.txt', 'a') as file:
            file.write('pre_image_attack: ' + str(test_bit_length) + 'bits\n')

        # run the pre_image attack X times for the current bit_length
        pre_image_results = []
        for i in range(0, 50):
            word = random_word(30)
            pre_image_results.append(pre_image_attack(word, test_bit_length, 30))
        # write the results, times first then word counts
        with open('output.txt', 'a') as file:
            for x in range(0, len(pre_image_results)):
                file.write(',' + str(pre_image_results[x][0]))
            file.write('\n')
            for y in range(0, len(pre_image_results)):
                file.write(',' + str(pre_image_results[y][1]))

        with open('output.txt', 'a') as file:
            file.write('\ncollision_attack: ' + str(test_bit_length) + 'bits\n')

        # run the collision attack X times for the current bit_length
        collision_attack_results = []
        for j in range(0, 50):
            collision_attack_results.append(collision_attack(test_bit_length, 30))
        # write the results, times first then word counts
        with open('output.txt', 'a') as file:
            for x in range(0, len(collision_attack_results)):
                file.write(',' + str(collision_attack_results[x][0]))
            file.write('\n')
            for y in range(0, len(collision_attack_results)):
                file.write(',' + str(collision_attack_results[y][1]))

        with open('output.txt', 'a') as file:
            file.write('\n\n')
            file.write('---------------------------------------------------------------------------------------')
            file.write('\n\n')

        test_bit_length += 1


main()
