brojevi = []

while True:
    user_input = input("Unesite broj ili 'Done' za završetak: ")
    
    if user_input.lower() == "done":
        break
    
    try:
        number = float(user_input)
        brojevi.append(number)
    except ValueError:
        print("Greška: Molimo unesite ispravan broj.")

if brojevi:
    print(f"Broj unesenih brojeva: {len(brojevi)}")
    print(f"Srednja vrijednost: {sum(brojevi) / len(brojevi):.2f}")
    print(f"Minimalna vrijednost: {min(brojevi)}")
    print(f"Maksimalna vrijednost: {max(brojevi)}")
    brojevi.sort()
    print(f"Sortirana lista: {brojevi}")
else:
    print("Nema unesenih brojeva.")
