import nltk
from collections import defaultdict
from collections import Counter


def main():
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        text = ''.join(f.readlines())
        tokens = text.split()
        bigrams = list(nltk.bigrams(tokens))
        freq_dict = defaultdict(list)
        for bigram in bigrams:
            freq_dict[bigram[0]].append(bigram[1])
        for key, value in freq_dict.items():
            freq_dict[key] = Counter(value)
        head_choice = input()
        while head_choice != "exit":
            tails = freq_dict[head_choice]
            if tails:
                print(f"Head: {head_choice}")
                for tail in tails:
                    print("Tail: {0:<15} Count: {1:<10}".format(tail, tails[tail]))
            else:
                print("The requested word is not in the model. Please input another word.")
            head_choice = input()


nltk.download('all')
main()
