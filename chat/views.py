from django.shortcuts import render
from .models import Chat_post
from django.contrib import messages
#from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.decorators import login_required
from django.views.generic import (
    #ListView,
    #DetailView,
    CreateView,
    #UpdateView,
    #DeleteView,
)

def home(request):
    return render(request, 'chat/index.html')


class Chat_View(LoginRequiredMixin, CreateView):
    model = Chat_post
    #success_url = reverse_lazy('')
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Chat'
        return context

    def get_template_names(self):
        if  self.request.user.profile.user_level > 3:
            template_name = 'chat/chat_view.html'
        else:
            template_name = 'chat/chat_view.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_type = 'Topic'
        messages.add_message(self.request, messages.INFO, 'Yours new message has been saved!')
        return super().form_valid(form)