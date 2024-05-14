import random

def generate_request():
    return random.randint(0, 4999)

def generate_input_file(file_name):
    with open(file_name, 'w') as file:
        for _ in range(1000):
            request = generate_request()
            file.write(str(request) + '\n')

generate_input_file('input.txt')
