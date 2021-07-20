import folium
import branca

map = folium.Map(location=(-39.831178, -73.231723), zoom_start=14)

html = '<p>Sonido: Ladridos</p><p>Categoría: Animales</p><p>Duración: 0:06</p><p>Latitud: -39.831178</p><p>Longitud: -73.231723</p><audio src="sounds_wav/animal.wav" controls></audio>'
iframe1 = branca.element.IFrame(html=html, width=300, height=300)
sound1 = folium.Marker(
    location=(-39.831178, -73.231723),
    popup=folium.Popup(iframe1, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Explosión</p><p>Categoría: Mecánicos</p><p>Duración: 0:05</p><p>Latitud: -39.851870</p><p>Longitud: -73.255343</p><audio src="sounds_wav/explosion.wav" controls></audio>'
iframe2 = branca.element.IFrame(html=html, width=500, height=300)
sound2 = folium.Marker(
    location=(-39.851870, -73.255343),
    popup=folium.Popup(iframe2, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Estornudos</p><p>Categoría: Humanos</p><p>Duración: 0:03</p><p>Latitud: -39.832241</p><p>Longitud: -73.220442</p><audio src="sounds_wav/human.wav" controls></audio>'
iframe3 = branca.element.IFrame(html=html, width=500, height=300)
sound3 = folium.Marker(
    location=(-39.832241, -73.220442),
    popup=folium.Popup(iframe3, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Alarma</p><p>Categoría: Música</p><p>Duración: 0:12</p><p>Latitud: -39.824464</p><p>Longitud: -73.242242</p><audio src="sounds_wav/music.wav" controls></audio>'
iframe4 = branca.element.IFrame(html=html, width=500, height=300)
sound4 = folium.Marker(
    location=(-39.824464, -73.242242),
    popup=folium.Popup(iframe4, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Sirena</p><p>Categoría: Alertas</p><p>Duración: 0:37</p><p>Latitud: -39.810369</p><p>Longitud: -73.222786</p><audio src="sounds_wav/siren.wav" controls></audio>'
iframe5 = branca.element.IFrame(html=html, width=500, height=300)
sound5 = folium.Marker(
    location=(-39.810369, -73.222786),
    popup=folium.Popup(iframe5, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Motocicleta</p><p>Categoría: Vehículos</p><p>Duración: 0:09</p><p>Latitud: -39.849333</p><p>Longitud: -73.231452</p><audio src="sounds_wav/vehicle.wav" controls></audio>'
iframe6 = branca.element.IFrame(html=html, width=500, height=300)
sound6 = folium.Marker(
    location=(-39.849333, -73.231452),
    popup=folium.Popup(iframe6, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

html = '<p>Sonido: Viento</p><p>Categoría: Ambientales</p><p>Duración: 0:48</p><p>Latitud: -39.842560</p><p>Longitud: -73.217155</p><audio src="sounds_wav/wind.wav" controls></audio>'
iframe7 = branca.element.IFrame(html=html, width=500, height=300)
sound7 = folium.Marker(
    location=(-39.842560, -73.217155),
    popup=folium.Popup(iframe7, max_width=300, max_height=300),
    icon=folium.Icon(color="black")
)

sound1.add_to(map)
sound2.add_to(map)
sound3.add_to(map)
sound4.add_to(map)
sound5.add_to(map)
sound6.add_to(map)
sound7.add_to(map)


map.save("map.html")