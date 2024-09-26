import facebook

# Obtén la clave de acceso de Facebook
access_token = '[TU-CLAVE-DE-ACCESO]'

# Crea un objeto GraphAPI de Facebook
graph = facebook.GraphAPI(access_token)

# Obtén la información de la transmisión en vivo
live_video = graph.get_object('[VIDEO-ID]')

# Obtén la URL de la transmisión en vivo
live_video_url = live_video['live_video']['secure_stream_url']

# Imprime la URL de la transmisión en vivo
print(live_video_url)
