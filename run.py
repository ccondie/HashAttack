import hashlib


def main():
    hasher = hashlib.sha1()
    hasher.update(b'cat')

    digest = hasher.hexdigest()
    digest_size = hasher.digest_size

    print(digest_size)
    print(digest)

    bin_digest_array = []
    for el in digest:
        bin_digest_array.append(format(int(el,16),'04b'))

    bin_digest = ''.join(bin_digest_array)
    print(bin_digest)


main()
