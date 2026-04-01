def ex5_media_aprovacao(notas: list[float]) -> dict[str, float | str]:


    if not notas:
        return {"media": 0.0, "status": "Sem notas"}
    
    soma_notas = 0.0
    for nota in notas:
        soma_notas += nota

    media = soma_notas / len(notas)


    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"


    return {
        "media": round(media, 2),
        "status": status
    }

resultado = ex5_media_aprovacao([7.5, 8.0, 6.5])
print(resultado)