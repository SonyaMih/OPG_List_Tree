class Uzol:
    def __init__(self, data):
        self.data = data
        self.dalsi = None

class LinkedList:
    def __init__(self):
        self.hlava = None
        self.dlzka = 0

    def vypis_zoznam(self):
        aktualny = self.hlava
        print("Zaciatok ->", end=" ")
        while aktualny:
            print(aktualny.data, end=" - ")
            aktualny = aktualny.dalsi
        print("Koniec")

    def dlzka_zozname(self):
        return self.dlzka

    def ziskaj_podla_indexu(self, index):
        if index < 0 or index >= self.dlzka:
            raise IndexError("Index mimo rozsahu")
        aktualny = self.hlava
        for _ in range(index):
            aktualny = aktualny.dalsi
        return aktualny.data

    def nastav_podla_indexu(self, index, hodnota):
        if index < 0 or index >= self.dlzka:
            raise IndexError("Index mimo rozsahu")
        aktualny = self.hlava
        for _ in range(index):
            aktualny = aktualny.dalsi
        aktualny.data = hodnota

    def najdi_ukazovatel_podla_hodnoty(self, hodnota):
        aktualny = self.hlava
        while aktualny:
            if aktualny.data == hodnota:
                return aktualny
            aktualny = aktualny.dalsi
        return None

    def najdi_index_podla_hodnoty(self, hodnota):
        aktualny = self.hlava
        index = 0
        while aktualny:
            if aktualny.data == hodnota:
                return index
            aktualny = aktualny.dalsi
            index += 1
        return -1

    def najdi_ukazovatel_podla_indexu(self, index):
        if index < 0 or index >= self.dlzka:
            raise IndexError("Index mimo rozsahu")
        aktualny = self.hlava
        for _ in range(index):
            aktualny = aktualny.dalsi
        return aktualny

    def najdi_index_podla_ukazovatel(self, ukazovatel):
        aktualny = self.hlava
        index = 0
        while aktualny:
            if aktualny == ukazovatel:
                return index
            aktualny = aktualny.dalsi
            index += 1
        return -1

    def pridaj_na_zaciatok(self, data):
        novy_ukazovatel = Uzol(data)
        novy_ukazovatel.dalsi = self.hlava
        self.hlava = novy_ukazovatel
        self.dlzka += 1

    def pridaj_na_koniec(self, data):
        novy_ukazovatel = Uzol(data)
        if not self.hlava:
            self.hlava = novy_ukazovatel
        else:
            aktualny = self.hlava
            while aktualny.dalsi:
                aktualny = aktualny.dalsi
            aktualny.dalsi = novy_ukazovatel
        self.dlzka += 1

    def vloz_po_indexe(self, index, data):
        ukazovatel = self.najdi_ukazovatel_podla_indexu(index)
        return self.vloz_po_ukazovateli(ukazovatel, data)

    def vloz_pred_indexom(self, index, data):
        if index == 0:
            self.pridaj_na_zaciatok(data)
            return
        predchadzajuci = self.najdi_ukazovatel_podla_indexu(index - 1)
        return self.vloz_po_ukazovateli(predchadzajuci, data)

    def vloz_po_ukazovateli(self, ukazovatel, data):
        if not ukazovatel:
            return
        novy_ukazovatel = Uzol(data)
        novy_ukazovatel.dalsi = ukazovatel.dalsi
        ukazovatel.dalsi = novy_ukazovatel
        self.dlzka += 1

    def vloz_pred_ukazovatelom(self, ukazovatel, data):
        if not ukazovatel:
            return
        if ukazovatel == self.hlava:
            self.pridaj_na_zaciatok(data)
            return
        aktualny = self.hlava
        while aktualny.dalsi != ukazovatel:
            aktualny = aktualny.dalsi
        novy_ukazovatel = Uzol(data)
        novy_ukazovatel.dalsi = ukazovatel
        aktualny.dalsi = novy_ukazovatel
        self.dlzka += 1

    def odstran_podla_indexu(self, index):
        if index < 0 or index >= self.dlzka:
            raise IndexError("Index mimo rozsahu")
        if index == 0:
            self.hlava = self.hlava.dalsi
        else:
            predchadzajuci = self.najdi_ukazovatel_podla_indexu(index - 1)
            predchadzajuci.dalsi = predchadzajuci.dalsi.dalsi
        self.dlzka -= 1

    def odstran_podla_ukazovatel(self, ukazovatel):
        if not ukazovatel:
            return
        if ukazovatel == self.hlava:
            self.hlava = self.hlava.dalsi
        else:
            index = self.najdi_index_podla_ukazovatel(ukazovatel)
            if index != -1:
                self.odstran_podla_indexu(index)

    def odstran_podla_hodnoty(self, hodnota):
        ukazovatel = self.najdi_ukazovatel_podla_hodnoty(hodnota)
        if ukazovatel:
            self.odstran_podla_ukazovatel(ukazovatel)


zoznam = LinkedList()

zoznam.pridaj_na_koniec(5)
zoznam.pridaj_na_koniec(10)
zoznam.pridaj_na_koniec(15)
zoznam.pridaj_na_koniec(20)
zoznam.vypis_zoznam()

zoznam.pridaj_na_zaciatok(1)
zoznam.pridaj_na_koniec(16)
zoznam.vypis_zoznam()

print("Dlzka zoznamu:", zoznam.dlzka_zozname())
print("Hodnota na indexe 2:", zoznam.ziskaj_podla_indexu(2))

zoznam.nastav_podla_indexu(2, 9)
zoznam.vypis_zoznam()

ukazovatel = zoznam.najdi_ukazovatel_podla_hodnoty(9)
print(f"Index ukazovatela :", zoznam.najdi_index_podla_ukazovatel(ukazovatel))

zoznam.vloz_po_ukazovateli(ukazovatel, 35)
zoznam.vypis_zoznam()

zoznam.odstran_podla_ukazovatel(ukazovatel)
zoznam.vypis_zoznam()
