from animals import animals_list

def main():
    print("\nAnimal Information:")
    for animal in animals_list:
        animal.info()
        animal.make_sound()

if __name__ == '__main__':
        main()
