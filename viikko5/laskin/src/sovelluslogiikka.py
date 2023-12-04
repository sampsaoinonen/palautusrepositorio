class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.historia = []

    def miinus(self, operandi):
        self.lisaa_historia()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.lisaa_historia()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.lisaa_historia()
        self._arvo = 0

    def aseta_arvo(self, arvo):        
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def lisaa_historia(self):
        self.historia.append(self._arvo)

    def edellinen(self):
        if self.historia:
            self.aseta_arvo(self.historia.pop())
        else:
            pass