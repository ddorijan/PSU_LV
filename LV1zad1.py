def total_euro(radni_sati, cijena_po_satu):
    return radni_sati * cijena_po_satu

radni_sati = float(input("Unesite broj radnih sati: "))
cijena_po_satu = float(input("Unesite iznos eura po satu: "))


ukupno = total_euro(radni_sati, cijena_po_satu)

print(f"Ukupno: {ukupno:.2f} eura")