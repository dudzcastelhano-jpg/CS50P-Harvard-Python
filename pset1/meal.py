def main():
    tempo_str = input("What time is it? ").strip()
    
    # Chama a função de conversão
    horas = convert(tempo_str)
    
    # Verifica os intervalos (Inclusive)
    if 7.0 <= horas <= 8.0:
        print("breakfast time")
    elif 12.0 <= horas <= 13.0:
        print("lunch time")
    elif 18.0 <= horas <= 19.0:
        print("dinner time")

def convert(time):
    horas, minutos = time.split(":")
    return float(horas) + float(minutos) / 60

if __name__ == "__main__":
    main()