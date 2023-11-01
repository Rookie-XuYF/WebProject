import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

output_path = 'test.txt'
with open(output_path, 'w', encoding='UTF-8') as fw:
    for _ in range(0, 10000):
        fw.write(generate_random_string(10) + '\t' + generate_random_string(10) + '\n')