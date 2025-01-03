meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "hmm" : "a visitor? indeed i have sleept long enough",
    "the kingdom of heavens" : "has long since forgoten my name, and im EAGER to make them remember",
    "however" : "the blood of minos stains your hands, and i must admit, im curious about your skills, weapon",
    "and so" : "before i tear down the cities and CRUSH the armies of heaven, you shall do as an apetizer",
    "come forth" : "child of man and DIE"
            }

prime=int(input("cuantas palabras quieres consultar?"))

for i in range(prime):

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no conozco eso...")
