from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html') 
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        
    if senha != confirmar_senha:
        # As senhas não coincidem
        return redirect('/auth/cadastro')
    
    if senha <= 5:
        # Sua senha precisa ter 6 ou mais caracteres
        return redirect('/auth/cadastro')
    
    if len(username.strip() == '') or len(senha.strip() == '') or len(confirmar_senha.strip() == ''):
        # Preencha todos os campos
        return redirect('/auth/cadastro')
    
    user = User.objects.filter(username=username)
    
    if user.exists():
        # Esse usuário já existe
        return redirect('/auth/cadastro')
    
    try:
        user = User.objects.create_user(username=username, senha=senha, confirmar_senha=confirmar_senha)
        
        user.save()
        # cadastro realizado com sucesso
        return redirect('/auth/logar')
    except:
        # Erro interno no sistema
        return redirect('auth/cadastro')

def logar(request):
    return HttpResponse('Olá, você está no logar')

