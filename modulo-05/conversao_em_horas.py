def s_para_h(segundos):
    hora = s // 3600
    minutos = (s % 3600) % 60
    segundos = s % 60

    return f"{formatar_tempo(hora)}:{formatar_tempo(minutos)}:{formatar_tempo(segundos)}"

def formatar_tempo(tempo):
    if tempo < 10:
        return f"0{tempo}"

    return tempo

s = 3661
print(s_para_h(s))