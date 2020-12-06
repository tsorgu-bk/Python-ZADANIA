#! /usr/bin/env python

# *********************TEXT*************************
# w tym podpunkcie użyłem własych plików .txt ponieważ te z dropboxa miały jakąś dziwną zawartość

def words_removal(file_name):
    key_words = ["się", "i", "oraz", "nigdy", "dlaczego"]
    file = open(file_name).read()
    text = file.split(' ')
    punctuation = ['.', '!', '?', ',']
    new_text = []
    print(text)
    for word in text:
        if word == '':
            continue
        if word.lower() not in key_words and not (word[-1] in punctuation and word[:-1].lower() in key_words):
            new_text.append(word)
    new_file = ' '.join(new_text)
    print(new_file)
    new_file_name = "removed_" + file_name
    n_f = open(new_file_name, "w+")
    n_f.write(new_file)
    n_f.close()


def words_replace(file_name):
    file = open(file_name).read()
    print("Oryginalny tekst:", str(file))
    dictionary = {"i": "oraz", "oraz": "i", "nigdy": "prawie nigdy", "dlaczego": "czemu"}
    text = file.split()
    replaced_text = []
    for word in text:
        replaced_text.append(dictionary.get(word, word))

    replaced_text = ' '.join(replaced_text)
    print(" Zmieniony tekst: ", str(replaced_text))
    new_file_name = "replaced_" + file_name
    n_f = open(new_file_name, "w+")
    n_f.write(replaced_text)
    n_f.close()

if __name__ == '__main__':
    # words_removal('text2.txt')
    words_replace('text2.txt')
