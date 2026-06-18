
def novo(id: str, name:str, number:str):
    return{
        id:{
            "Nome: ": name,
            "Numero: ": number,
        },
    }

agenda:dict[str, dict[str, str]] = {
    # "id1":{
    #     "Nome:" : "Matheus",
    #     "Número:": "1111111",
    # },
}
adc = novo("1", "joão", "22222222")
adc2 = novo("2", "aefae", "22222222")
agenda.update(adc)
agenda.update(adc2)
agenda.popitem(adc)
print(agenda)