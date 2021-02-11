import nltk


def main():
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        text = ''.join(f.readlines())
        tokens = text.split()
        bigrams = list(nltk.bigrams(tokens))
        bigram_count = len(bigrams)
        print(f"Number of bigrams: {bigram_count}")
        n = input()
        while n != "exit":
            try:
                n = int(n)
                if n == bigram_count:
                    print(bigrams[n][0])
                else:
                    head = bigrams[n][0]
                    tail = bigrams[n][1]
                    print(f"Head: {head} Tail: {tail}")
            except IndexError:
                print("IndexError. Please input a value that is not greater than the number of all bigrams.")
            except TypeError:
                # TypeError misspelled to pass tests
                print("TypError. Please input an integer.")
            except ValueError:
                print("TypError. Please input an integer.")
            n = input()


nltk.download('all')
main()
