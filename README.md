# Subir imágenes masivamente a la API
1. Las imágenes deben estar en la raiz de la carpeta cancionitodb, la cual se debe crear en la raíz del proyecto.
2. La API debe estar levantada y lista para consumir, reemplazar su URL global en la variable "route"
3. Abrir una terminal y ejecutar el siguiente comando: *-m http.server 8000* (esto levantará un servidor http local)
4. Sin cerrar la terminal, abrir otra y, habiendo iniciado sesión en ngrok, ejecutar *ngrok http 8000* (esto hará un tunel para nuestro servidor local y lo hará público para que cloudinary pueda consumirlo)
5. Sin cerrar ninguna terminal, abrir otra y ejecutar *python LoadImages.py*
