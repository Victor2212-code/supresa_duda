from django.shortcuts import render, redirect
from django.urls import reverse

usuarios = {'maritor': '210723'}

def verificar_login(usuario, senha):
    return usuario in usuarios and usuarios[usuario] == senha

def fazer_login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        if verificar_login(usuario, senha):
            return redirect(reverse('pergunta', args=[0]))
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha incorretos'})
    return render(request, 'login.html')

perguntas = [
    {'pergunta': 'O que essa foto te traz?', 'imagem': 'img/dia_especial.jpg', 'opcoes': ['Raiva', 'Amor para Vida Toda', 'Odio', 'Ou quer matar alguém'], 'resposta': 'Amor para Vida Toda'},
    {'pergunta': 'O que aconteceu nesse dia?', 'imagem': 'img/aniversario_juntos.jpg', 'opcoes': ['Aniversário da sua prima', 'Nada de interessante', 'Mostra coisas Horriveis', 'Mostra nosso sentimento bandido'], 'resposta': 'Aniversário da sua prima'},
    {'pergunta': 'Sabe o que aconteceu nesse dia aqui?', 'imagem': 'img/aniversario_da_edna.jpg', 'opcoes': ['Brigamos', 'Discutimos', 'Você ficou chateada com minhas vestes', 'Me bateu'], 'resposta': 'Você ficou chateada com minhas vestes e discutimos brevemente'},
    {'pergunta': 'O que aconteceu antes dessa foto?', 'imagem': 'img/foto_aleatoria.jpg', 'opcoes': ['Peguei seu celular do nada', 'Brigamos', 'Dormi', 'Morena'], 'resposta': 'Peguei seu celular do nada'},
    {'pergunta': 'O que fizemos nesse dia?', 'imagem': 'img/moro_do_gaviao.jpg', 'opcoes': ['Brigamos', 'Dormi', 'Fomos Passear no moro do gavião'], 'resposta': 'Fomos Passear no moro do gavião'},
    {'pergunta': 'Onde fomos nesse dia?', 'imagem': 'img/seu_aniversario.jpg', 'opcoes': ['Bella roma comemorar seu aniversário', 'Dormir', 'Correr atrás de balas'], 'resposta': 'Bella roma comemorar seu aniversário'},
    {'pergunta': 'Onde fomos nesse dia?', 'imagem': 'img/casal_lindo.jpg', 'opcoes': ['Fomos ao cinema pela primeira vez', 'Andar', 'Comer'], 'resposta': 'Fomos ao cinema pela primeira vez'},
    {'pergunta': 'O que fomos comer?', 'imagem': 'img/dia_juntos.jpg', 'opcoes': ['Comida Japonesa (o que mais gostamos ksksks)', 'Beber', 'No pagode'], 'resposta': 'Comida Japonesa (o que mais gostamos ksksks)'},
    {'pergunta': 'O que estava acontecendo nessa foto?', 'imagem': 'img/mesversario.jpg', 'opcoes': ['Nosso mês versário', 'Foto aleatória', 'No museu'], 'resposta': 'Nosso mês versário'},
    {'pergunta': 'O que tinha acontecido nesse dia memorável?', 'imagem': 'img/dia_moto.jpg', 'opcoes': ['Escapou a corrente da moto', 'Choramos juntos', 'No boteco'], 'resposta': 'Nosso mês versário'},
    {'pergunta': 'O que está acontecendo na foto?', 'imagem': 'img/passeio_juntos.jpg', 'opcoes': ['Victor Hugo no museu seu lugar', 'Fomos na balada', 'No boteco'], 'resposta': 'Victor Hugo no museu seu lugar'},
]

def pergunta(request, pergunta_id):
    pergunta_id = int(pergunta_id)
    if request.method == 'POST':
        resposta = request.POST.get('resposta')
        if resposta == perguntas[pergunta_id]['resposta']:
            request.session['score'] = request.session.get('score', 0) + 1
            if pergunta_id + 1 < len(perguntas):
                return redirect(reverse('pergunta', args=[pergunta_id + 1]))
            else:
                return redirect('resultado')
        else:
            return redirect(reverse('erro', args=[pergunta_id]))
    return render(request, 'pergunta.html', {'pergunta': perguntas[pergunta_id], 'pergunta_id': pergunta_id})

def erro(request, pergunta_id):
    return render(request, 'erro.html', {'pergunta_id': pergunta_id})

def resultado(request):
    score = request.session.get('score', 0)
    return render(request, 'resultado.html', {'score': score})

def index(request):
    return redirect('login')
