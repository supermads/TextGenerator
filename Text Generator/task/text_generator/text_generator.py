def main():
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        text = ''.join(f.readlines())
        tokens = text.split()
        token_count = len(tokens)
        unique_token_count = len(set(tokens))
        print("Corpus statistics")
        print(f"All tokens: {token_count}")
        print(f"Unique tokens: {unique_token_count}")
        n = input()
        while n != "exit":
            try:
                print(tokens[int(n)])
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
            except TypeError:
                print("Type Error. Please input an integer.")
            except ValueError:
                print("Type Error. Please input an integer.")
            n = input()


main()
