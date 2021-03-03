import nltk
from collections import defaultdict, Counter
from random import choice, choices


def get_freq_dict():
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        text = ''.join(f.readlines())
        tokens = text.split()
        trigrams = list(nltk.trigrams(tokens))
        freq_dict = defaultdict(list)
        for trigram in trigrams:
            freq_dict[trigram[0:2]].append(trigram[2])
        for key, value in freq_dict.items():
            freq_dict[key] = Counter(value)
    return freq_dict


def generate_sentence(freq_dict):
    punc_marks = [".", "!", "?"]
    # Choose a random head from freq_dict to begin the sentence
    sentence = ""
    head = choice(list(freq_dict.keys()))
    # First word of the sentence should be capitalized and without punctuation marks
    while not head[0][0].isupper() or head[0][-1] in punc_marks:
        head = choice(list(freq_dict.keys()))
    sentence += f"{head[0]} {head[1]}"
    for _i in range(4):
        tail_options = freq_dict[(head[0], head[1])]
        tail_choice = choices(list(tail_options), [tail_options[tail] for tail in tail_options])
        while tail_choice[0][-1] in punc_marks:
            tail_choice = choices(list(tail_options), [tail_options[tail] for tail in tail_options])
        sentence += f" {tail_choice[0]}"
        head = (head[1], tail_choice[0])
    end_found = False
    while not end_found:
        tail_options = freq_dict[(head[0], head[1])]
        tail_choice = choices(list(tail_options), [tail_options[tail] for tail in tail_options])
        if tail_choice[0][-1] in punc_marks:
            end_found = True
        sentence += f" {tail_choice[0]}"
        head = (head[1], tail_choice[0])
    return sentence



def main():
    freq_dict = get_freq_dict()
    for _i in range(10):
        print(generate_sentence(freq_dict))


nltk.download('all')
main()
