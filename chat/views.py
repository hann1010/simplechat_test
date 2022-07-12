from django.shortcuts import render
from .models import Chat_post
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.decorators import login_required
from django.views.generic import (
    #ListView,
    DetailView,
    CreateView,
    #UpdateView,
    #DeleteView,
)

def home(request):
    return render(request, 'chat/index.html')


class Chat_View(LoginRequiredMixin, CreateView):
    model = Chat_post
    success_url = reverse_lazy('chat-view')
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items_in_page_int = self.request.user.profile.items_in_page
        db_data = Chat_post.objects.all().order_by('-date_posted')
        paginator = Paginator(db_data, items_in_page_int)
        page_number = self.request.GET.get('page')
        page_data = paginator.get_page(page_number)
        context["chat_context"] = page_data
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
        form.instance.post_type = 'Chat'
        messages.add_message(self.request, messages.INFO, 'Yours new message has been saved!')
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView): #Show selected user information
    model = Chat_post
    template_name = 'chat/user_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'User info'
        return context