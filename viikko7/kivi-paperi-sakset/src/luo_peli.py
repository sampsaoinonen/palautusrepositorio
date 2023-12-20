from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


def luo_peli(vastaus):
    if vastaus.endswith("a"):
        return KPSPelaajaVsPelaaja()
    
    if vastaus == 'b':
        return KPSTekoaly()
    
    if vastaus == 'c':
        return KPSParempiTekoaly()


    

