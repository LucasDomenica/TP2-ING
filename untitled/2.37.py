def analizar_tendencias(hashtags, tendencias, umbral):
    frecuencia_tendencias = dict(tendencias)
    frecuencia_hashtags = {}
    for hashtag in hashtags:
        if hashtag in frecuencia_hashtags:
            frecuencia_hashtags[hashtag] += 1
        else:
            frecuencia_hashtags[hashtag] = 1
    hashtags_filtrados = []
    for hashtag, frecuencia in frecuencia_tendencias.items():
        if frecuencia > umbral:
            hashtags_filtrados.append(hashtag)

    return hashtags_filtrados
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
umbral = 100

resultados = analizar_tendencias(hashtags, tendencias, umbral)
print(resultados)
