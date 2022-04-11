from collections import Counter

def p59():
    with open('./data/p059_cipher.txt') as file:
        message = list(map(int, file.read().split(',')))
    
    # we are given that the key length is 3
    counters = [Counter(), Counter(), Counter()]

    for pos in range(len(message)):
        counters[pos % 3][message[pos]] += 1
    
    # space (32) is the most common ascii char in english text
    key_numbers = [counters[x].most_common(1)[0][0] ^ 32 for x in range(3)]

    output = [''] * len(message)
    for pos in range(len(message)):
        output[pos] = chr(message[pos] ^ key_numbers[pos % 3])

    return sum(map(ord, output))

if __name__ == '__main__':
    print(p59())
