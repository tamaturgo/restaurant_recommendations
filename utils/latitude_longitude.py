from math import radians, sin, cos, sqrt, atan2


def distance(lat1, lon1, lat2, lon2):
    # raio da Terra em metros
    R = 6371000

    # converter para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # diferenças de latitude e longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # cálculo da fórmula Haversine
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c

    # retorna a distância em km
    return d/1000
