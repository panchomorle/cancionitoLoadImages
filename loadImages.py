import os
import requests

puerto = 8000
base_url = f"http://localhost:{puerto}/cancionitodb/"

songs = {}

anteriorTitulo = ""
for titulo in os.listdir("cancionitodb"):
    if titulo[:-6] != anteriorTitulo[:-6]:
        clave = titulo[:-6].replace("-"," ")
        songs[clave] = [] #creo nueva key
        anteriorTitulo = titulo #actualizo el titulo
    songs[clave].append(base_url+titulo)

print(songs)

#### PASO 2: LEVANTAR EL SERVER -> python -m http.server 8000
####--------PASO 3: Consumir la API----------####
route = "http://localhost:5024/api/"

# Recorremos el diccionario de canciones
for k, values in songs.items():
    # Datos del POST de la canción
    data = { "title": k }

    # Realizamos la solicitud POST para crear la canción
    print(f"/POST: {route+'songs'} - {data}")
    song_response = requests.post(route + "songs", json=data)

    if song_response.status_code == 201:  # Si la canción se creó correctamente
        song_id = song_response.json().get("id")  # Obtenemos el ID de la canción

        # Recorremos las URLs de imágenes asociadas a la canción
        for i, url in enumerate(values):
            # Datos del POST de la imagen
            img_data = {
                "songId": song_id,  # Asociamos la imagen con la canción
                "internalId": i,    # Identificador interno (opcional)
                "url": url          # URL de la imagen
            }
            # Realizamos la solicitud POST para agregar la imagen
            print(f"/POST: {route+'images'} - {img_data}")
            img_response = requests.post(route + "images", json=img_data)

            if img_response.status_code != 201:
                print(f"Error al subir la imagen: {img_data}, status code: {img_response.status_code}")
    else:
        print(f"Error al crear la canción: {data}, status code: {song_response.status_code}")