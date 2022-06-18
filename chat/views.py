from django.shortcuts import render

def home(request):
    return render(request, 'chat/index.html')


def chat_view(request):
    return render(request, 'chat/chat_view.html')
