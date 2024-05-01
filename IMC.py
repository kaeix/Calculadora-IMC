def calcular_imc(peso, altura_cm):
    """Função para calcular o IMC."""
    altura_m = altura_cm / 100  # Convertendo altura de centímetros para metros
    imc = peso / (altura_m ** 2)
    return imc

def classificar_imc(imc):
    """Função para classificar o IMC."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    print("---------------------------------------------")
    peso = float(input("Digite o seu peso em kg: "))
    altura_cm = float(input("Digite a sua altura em centímetros: "))

    imc = calcular_imc(peso, altura_cm)
    print("Seu IMC é:", imc)
    print("Classificação:", classificar_imc(imc))

if __name__ == "__main__":
    main()
