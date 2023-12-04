KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukon_alkiot = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.joukon_alkiot[:self.alkioiden_lkm]


    def lisaa(self, n):    
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm >= len(self.joukon_alkiot):
        
            paivitetty_koko = len(self.joukon_alkiot) + self.kasvatuskoko
            paivitetty_joukko = [0] * paivitetty_koko
            for i in range(self.alkioiden_lkm):
                paivitetty_joukko[i] = self.joukon_alkiot[i]
            self.joukon_alkiot = paivitetty_joukko

    
        self.joukon_alkiot[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.joukon_alkiot[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.joukon_alkiot[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.joukon_alkiot[j]
                self.joukon_alkiot[j] = self.joukon_alkiot[j + 1]
                self.joukon_alkiot[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.joukon_alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for num in a.to_int_list():
            x.lisaa(num)
        for num in b.to_int_list():
            x.lisaa(num)
        return x


    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                y.lisaa(i)
        return y

    @staticmethod
    
    def erotus(a, b):
        z = IntJoukko()
        for n in a.to_int_list():
            if not b.kuuluu(n):
                z.lisaa(n)
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        alkiot = []
        for i in range(self.alkioiden_lkm):
            alkiot.append(str(self.joukon_alkiot[i]))

        return "{" + ", ".join(alkiot) + "}"