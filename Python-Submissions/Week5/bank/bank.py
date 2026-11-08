def main():
    greet = input('Enter your greeting: ')
    print(f"${value(greet)}")


def value(greet):
    if greet.strip().lower().startswith('hello'):
        return 0
    elif greet.strip().lower().startswith('h'):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
