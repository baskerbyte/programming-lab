def formata_tempo(sec):
    hours = sec // 3600
    min = (sec % 3600) // 60
    sec = sec % 60

    return f"{hours}:{min}:{sec}"
