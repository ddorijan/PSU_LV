import string

filename = "song.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        word_count = {}
        
        for line in file:
            words = line.translate(str.maketrans("", "", string.punctuation)).lower().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        
        single_occurrence_words = [word for word, count in word_count.items() if count == 1]
        
        print(f"Broj riječi koje se pojavljuju samo jednom: {len(single_occurrence_words)}")
        print("Riječi koje se pojavljuju samo jednom:")
        print(", ".join(single_occurrence_words))

except FileNotFoundError:
    print("Greška: Datoteka nije pronađena.")
except Exception as e:
    print(f"Došlo je do pogreške: {e}")
