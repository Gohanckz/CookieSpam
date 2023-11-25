import random
import sys

def generate_random_string(length):
    characters = '0123456789abcdef'
    return ''.join(random.choice(characters) for _ in range(length))

def save_to_file(strings, filename):
    with open(filename, 'w') as file:
        for string in strings:
            file.write(string + '\n')

def main():
    print("Bienvenido al generador de strings aleatorios.")
    print("Este script genera strings con caracteres del 0 al 9 y letras de la a a la f.")

    if len(sys.argv) != 3:
        print("Uso: python script.py <largo_del_string> <num_strings>")
        return

    try:
        length = int(sys.argv[1])
        num_strings = int(sys.argv[2])
    except ValueError:
        print("Error: El largo del string y la cantidad de strings deben ser números enteros.")
        return

    print(f'Generando {num_strings} strings de largo {length}.\n')

    strings = [generate_random_string(length) for _ in range(num_strings)]

    output_filename = 'generated_strings.txt'
    save_to_file(strings, output_filename)

    print(f'Se generaron {num_strings} strings y se guardaron en "{output_filename}".')

if __name__ == "__main__":
    main()
