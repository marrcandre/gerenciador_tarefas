from django.shortcuts import render

# Create your views here.


def listar_tarefas(request):
    nome_tarefa = "Assistir vídeo 1 do Curso de Python e Django"
    return render(request, 'tarefas/listar_tarefas.html', {'nome_tarefa': nome_tarefa})
