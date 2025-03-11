filename = "SMSSpamCollection.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        ham_word_count = 0
        ham_count = 0
        spam_word_count = 0
        spam_count = 0
        spam_exclamation_count = 0
        
        for line in file:
            parts = line.strip().split("\t", 1)
            if len(parts) != 2:
                continue
            label, message = parts
            word_count = len(message.split())
            
            if label == "ham":
                ham_word_count += word_count
                ham_count += 1
            elif label == "spam":
                spam_word_count += word_count
                spam_count += 1
                if message.endswith("!"):
                    spam_exclamation_count += 1
        
        if ham_count > 0:
            avg_ham_words = ham_word_count / ham_count
        else:
            avg_ham_words = 0

        if spam_count > 0:
            avg_spam_words = spam_word_count / spam_count
        else:
            avg_spam_words = 0
        
        print(f"Prosječan broj riječi u ham porukama: {avg_ham_words:.2f}")
        print(f"Prosječan broj riječi u spam porukama: {avg_spam_words:.2f}")
        print(f"Broj spam poruka koje završavaju uskličnikom: {spam_exclamation_count}")

except FileNotFoundError:
    print("Greška: Datoteka nije pronađena.")
except Exception as e:
    print(f"Došlo je do pogreške: {e}")
