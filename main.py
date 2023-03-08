import openai
import config

openai.api_key = config.api_key

#contexto del asistente
messages = [{"role": "system", 
             "content": "Eres un asistente que haces recetas de comida."}]
print("Hola Soy tu asiste para tus recetas de comida! Que Opcion quieres elegir")
print("1-Recetas a partir de tus ingredientes")
print("2-Receta de lo que quieras cocinar")
print("")
opcion = input("Ingrese el numero de opcion: ")

if opcion == "1":
    print("")
    content = input("Que ingredientes tienes? ")
    while content != "no":
        print("")
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages=messages)

        response_content = response.choices[0].message.content
        messages.append({"role": "assistant","content": response_content})

        print(response_content)

        content = input("Quieres otra receta? ")
else:
    content = input("Que quieres cocinar? ")
    print("")

    while content != "no":
        
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages=messages)

        response_content = response.choices[0].message.content
        messages.append({"role": "assistant","content": response_content})

        print(response_content)

        content = input("Quieres otra receta? ")