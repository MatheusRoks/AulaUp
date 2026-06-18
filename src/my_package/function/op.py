import math

from my_package.verify_and_convert import convert_float


def recebe() -> list[str]:
    num1: str = input("Digite o primeiro número: ")
    num2: str = input("Digite o segundo número: ")
    lista: list[str] = [num1, num2]
    return lista


def soma() -> float | str:
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."
    try:
        new_number: list[float] = convert_float(*nums)
        resultado: float = new_number[0] + new_number[1]
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def sub() -> float | str:
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."
    try:
        new_numbers: list[float] = convert_float(*nums)
        resultado: float = new_numbers[0] - new_numbers[1]
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def mult() -> float | str:
    resp = "Valores inválido conta não pode ser executada."
    nums = recebe()
    try:
        new_numbers: list[float] = convert_float(*nums)
        resultado: float = new_numbers[0] * new_numbers[1]
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def div() -> float | str:
    numeros = recebe()
    resp = "Valores inválido conta não pode ser executada."

    try:
        nums: list[float] = convert_float(*numeros)
        if nums[1] == 0:
            return resp
        resultado: float = nums[0] / nums[1]
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def pot() -> float | str:
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."

    try:
        numbers: list[float] = convert_float(*nums)
        resultado: float = numbers[0] ** numbers[1]
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def raiz() -> str | float:
    num: str = input("Digite o número para extrair a raiz: ")
    resp = "Valores inválido conta não pode ser executada."
    try:
        num2: float = float(num)
        if num2 < 0:
            return resp
        return f"{math.sqrt(num2):.2f}"
    except (ValueError, TypeError):
        return resp


def raizcub() -> str | float:
    num: str = input("Digite o número para extrair a raiz: ")
    resp = "Valores inválido conta não pode ser executada."
    try:
        num2: float = float(num)
        return f"{math.cbrt(num2):.2f}"
    except (ValueError, TypeError):
        return resp


def fatorial() -> int | str:
    num = input("Digite o número que deseja o fatorial: ")
    resp = "Valores inválido conta não pode ser executada."
    resultado = 1

    try:
        number: int = int(num)
        if number < 0:
            return "Não existe fatorial"
        while number >= 1:
            resultado = resultado * number
            number -= 1
        return resultado  # noqa: TRY300
    except ValueError:
        return resp


def numprim() -> str:
    num = input("Digite um número: ")
    resp = "Valores inválido conta não pode ser executada."
    ep = "É primo"
    try:
        num2: int = int(num)
        if num2 < 2:
            return f"{num2} não é primo"
        for i in range(2, int(num2**0.5) + 1):
            if num2 % i == 0:
                return f"{num2} não é primo"
        return ep  # noqa: TRY300
    except (ValueError, TypeError):
        return resp


def decide(x: str, y: str, num: str, num2: str) -> str:

    if num.isdigit() and num2.isdigit():
        if int(num2) == 0:
            return "Divisão por 0"
        resultado: bool = int(num) % int(num2) == 0
        if resultado:
            return x
        return y
    return "Valores inválidos"


def ismult() -> str:
    print("Insira dois números e vou verificar se o PRIMEIRO é um multiplo do SEGUNDO")
    nums: list[str] = recebe()
    e_mult: str = f"{nums[0]} é um multiplo de {nums[1]}"
    notmult: str = f"{nums[0]} não é um multiplo de {nums[1]}"
    return decide(e_mult, notmult, nums[0], nums[1])


def isdivisor() -> str:
    print("Insira dois números e vou verificar se o SEGUNDO é um divisor do PRIMEIRO")
    nums: list[str] = recebe()
    divisor: str = f"{nums[1]} é um divisor de {nums[0]}"
    nao_divisor: str = f"{nums[1]} não é um divisor de {nums[0]}"
    return decide(divisor, nao_divisor, nums[0], nums[1])


def mdc() -> str:
    print("MDC de dois números INTEIROS")
    nums: list[str] = recebe()
    if nums[0].isdigit() and nums[1].isdigit():
        num: int = int(nums[0])
        num2: int = int(nums[1])
        while num2 != 0:
            resto: int = num % num2
            num = num2
            num2 = resto
        return f"O máximo divisor comum é {num}"
    return "Valores inválidos"


def mdc_interno(x: int, y: int) -> int:
    while y != 0:
        resto: int = x % y
        x = y
        y = resto
    return x


def mmc() -> str:
    print("MMC de dois números INTEIROS")
    nums: list[str] = recebe()
    if nums[0].isdigit() and nums[1].isdigit():
        num: int = int(nums[0])
        num2: int = int(nums[1])
        if num == 0 and num2 == 0:
            return "MMC indefinido para 0 e 0"
        resultado: int = (num * num2) // mdc_interno(num, num2)
        return f"O mmc de {num} e {num2} é {resultado}"
    return "Dados inválidos"


def media() -> str:
    print("Iremos realizar a média")
    cont: int = 0
    med: float = 0
    while True:
        a = input("Digite uma nota ou = para ver o resultado: ")
        if a == "=":
            if cont == 0:
                return "Média 0.0"
            med = med / cont
            return f"A média é {med:.2f}"
        try:
            a = float(a)
            med += a
            cont += 1
        except (ValueError, TypeError):
            return "Valores informados inconsistentes, encerrando o programa"


def valor(x: str, z: float, y: float, msg1: str, msg2: str) -> str:
    if z == y:
        return f"{z} e {y} possuem o mesmo valor"
    if x == ">":
        return msg1 if z > y else msg2
    if x == "<":
        return msg1 if z < y else msg2
    return msg2


def maior() -> str:
    print("Definindo o maior de dois números")
    try:
        z, y = convert_float(*recebe())
        msg1: str = f"{z} é maior que {y}"
        msg2: str = f"{y} é maior que {z}"
        resp: str = valor(">", z, y, msg1, msg2)
        return resp  # noqa: TRY300
    except (ValueError, TypeError):
        return "Valores inconsistentes, tente novamente"


def menor() -> str:
    print("Definindo o menor de dois números")
    try:
        z, y = convert_float(*recebe())
        msg1: str = f"{z} é menor que {y}"
        msg2: str = f"{y} é menor que {z}"
        resp: str = valor("<", z, y, msg1, msg2)
        return resp  # noqa: TRY300
    except (ValueError, TypeError):
        return "Valores inconsistentes, tente novamente"


def bhask() -> str:
    print("Executaremos a formula de báscara")
    a: str = input("Valor de a: ")
    b: str = input("Valor de b: ")
    c: str = input("Valor de c: ")

    try:
        a1, b1, c1 = float(a), float(b), float(c)
        raquis: float = b1**2 - 4 * a1 * c1
        if a1 == 0:
            return "a não pode ser zero"
        if raquis < 0:
            return "raiz negativa"
        x1 = (-b1 + math.sqrt(raquis)) / (2 * a1)
        x2 = (-b1 - math.sqrt(raquis)) / (2 * a1)
        return f"As respostas são: x1={x1:.2f} e x2={x2:.2f}"  # noqa: TRY300
    except (ValueError, TypeError):
        return "Valores inconsistentes"


def pitagoras() -> str:  # noqa: C901
    print(
        "----------Pitágoras-----------\n"
        "1 - Possui o valor dos dois catetos\n"
        "2 - Possui 1 cateto e a hipotenusa\n"
        "3 - Calcular usando o seno\n"
        "4 - Calcular usando o cosseno\n"
        "5 - Calcular usando a tangente\n"
    )
    option: str = input("Digite a opção: ")
    if option == "1":
        try:
            ca: float = float(input("Digite o valor do 1 cateto: "))
            co: float = float(input("Digite o valor do 2 cateto: "))
            resultado: float = math.sqrt(ca**2 + co**2)
            return f"O valor da hipotenusa é {resultado:.2f}"  # noqa: TRY300
        except (ValueError, TypeError):
            return "Valores inválidos"
    elif option == "2":
        try:
            co: float = float(input("Digite o valor do cateto: "))
            h: float = float(input("Digite o valor da hipotenusa: "))
            if h < co:
                return "A hipotenusa deve ser maior ou igual ao cateto"
            resultado: float = math.sqrt(h**2 - co**2)
            return f"O valor do cateto é {resultado:.2f}"  # noqa: TRY300
        except (ValueError, TypeError):
            return "Valores inválidos"
    elif option == "3":
        try:
            co: float = float(input("Digite o valor do cateto oposto: "))
            ang: str = input("Digite o ângulo (30, 45 ou 60): ")
            match ang:
                case "30":
                    x: float = 1 / 2
                case "45":
                    x: float = math.sqrt(2) / 2
                case "60":
                    x: float = math.sqrt(3) / 2
                case _:
                    return "Ângulo inválido"
            resultado: float = co / x
            return f"O valor da hipotenusa é {resultado:.2f}"  # noqa: TRY300
        except (ValueError, TypeError):
            return "Valores inválidos"
    elif option == "4":
        try:
            ca: float = float(input("Digite o valor do cateto adjacente: "))
            ang: str = input("Digite o ângulo (30, 45 ou 60): ")
            match ang:
                case "30":
                    x: float = math.sqrt(3) / 2
                case "45":
                    x: float = math.sqrt(2) / 2
                case "60":
                    x: float = 1 / 2
                case _:
                    return "Ângulo inválido"
            resultado: float = ca / x
            return f"O valor da hipotenusa é {resultado:.2f}"  # noqa: TRY300
        except (ValueError, TypeError):
            return "Valores inválidos"
    elif option == "5":
        try:
            ca: float = float(input("Digite o valor do cateto adjacente: "))
            ang: str = input("Digite o ângulo (30, 45 ou 60): ")
            match ang:
                case "30":
                    x: float = math.sqrt(3) / 3
                case "45":
                    x: float = 1
                case "60":
                    x: float = math.sqrt(3)
                case _:
                    return "Ângulo inválido"
            resultado: float = ca * x
            return f"O valor do cateto oposto é {resultado:.2f}"  # noqa: TRY300
        except (ValueError, TypeError):
            return "Valores inválidos"
    return "Opção inválida"
