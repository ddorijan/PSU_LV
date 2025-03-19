filename = input("Unesite ime datoteke: ")

try:
    with open(filename, "r") as file:
        total_confidence = 0
        count = 0
        
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence_value = float(line.split("X-DSPAM-Confidence:")[1].strip())
                    total_confidence += confidence_value
                    count += 1
                except ValueError:
                    print("Greška pri konverziji vrijednosti.")
        
        if count > 0:
            average_confidence = total_confidence / count
            print(f"Average X-DSPAM-Confidence: {average_confidence}")
        else:
            print("Nema pronađenih vrijednosti X-DSPAM-Confidence u datoteci.")

except FileNotFoundError:
    print("Greška: Datoteka nije pronađena.")
except Exception as e:
    print(f"Došlo je do pogreške: {e}")
