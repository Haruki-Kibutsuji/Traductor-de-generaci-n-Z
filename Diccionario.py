import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Aesthetic": "Se refiere a que algo es estetico, o bonito",
            "WDYM": "What do you mean? que en español significa: que quieres decir o a que te refieres?",
            "nvm": "Never mind, en español se le conoceria como la tipica frase: Olvidalo",
            "Gore": "Se refiere a que algo tiene mucha sangre",
            "nsfw": "Contenido no apropiado para todos, conteniendo gore o 18+",
            "random": "Algo que no tiene sentido o contexto en la situacion, algo que es aleatorio",
            "POV": "Point of view o punto de vista, se usa para mostrar algo desde ese punto de vista",
            "CC": "Palabra utilizada para decir como cuando, y colocar alguna situacion"
            }
            
palabra = input ("¿Que palabra no entendiste?")

if palabra in meme_dict:
    print (palabra, meme_dict[palabra])
    
else:
    print("No tengo esa palabra, pero puedo mostrarte otra:")
    clave = random.choice(meme_dict.keys())
    print (clave + ":", meme_dict[clave])
