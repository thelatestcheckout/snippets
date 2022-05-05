import os.path


def main():
    for fname in os.listdir('/Users/ashu/Desktop/snippets/input/csv'):
        if fname.endswith('.csv'):
            print("here")
            break
        else:
            print("there")


if __name__ == "__main__":
    main()
