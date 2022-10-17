from django.shortcuts import render
from .models import Chat_post
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import (
    #ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    dic_x = {
        'title': 'home',
        'title_page' : 'Home'
    }
    return render(request, 'chat/index.html', dic_x)


@login_required
def jsonChat(request):
    data = Chat_post.objects.all().values().order_by('-date_posted')
    messages_in_chat_tmp = request.user.profile.messages_in_chat_page
    if messages_in_chat_tmp > 49:
        messages_in_chat_int = 50
    elif messages_in_chat_tmp < 50 and messages_in_chat_tmp > 0:
        messages_in_chat_int = messages_in_chat_tmp
    else:
        messages_in_chat_int = 1
    paginator = Paginator(data, messages_in_chat_int)
    page_number = request.POST.get('page')
    if page_number == None:
        page_number_fix = 1
    else:
        page_number_fix = page_number
    page_data = paginator.get_page(page_number)
    json_page = {
        'chat_context' : list(page_data),
        'num_of_pages' : paginator.num_pages,
        'page_number' : page_number_fix,
        'page_range' : list(paginator.page_range)
    }
    return JsonResponse(json_page, safe=False)


def jsonProfile(request):
    json_profile = {}
    return JsonResponse(json_profile, safe=False)


class Chat_View(LoginRequiredMixin, CreateView):
    model = Chat_post
    success_url = reverse_lazy('chat-view')
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'chat'
        context["title_page"] = 'Chat'
        return context

    def get_template_names(self):
        if  self.request.user.profile.user_level > 3:
            template_name = 'chat/chat_view.html'
        else:
            template_name = 'chat/forbidden.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.author_name = str(self.request.user)
        form.instance.post_type = 'Chat'
        messages.add_message(self.request, messages.INFO, 'Yours new message has been saved!')
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView): #Show selected user information
    model = Chat_post
    template_name = 'chat/user_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'user info'
        context["title_page"] = 'User info'
        return context


class ChatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chat_post
    success_url = reverse_lazy('chat-view')
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'edit chat'
        context["title_page"] = 'Edit chat'
        return context

    def get_template_names(self):
        if  self.request.user.profile.user_level > 3:
            template_name = 'chat/chat_edit.html'
        else:
            template_name = 'chat/forbidden.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.author_name = str(self.request.user)
        form.instance.post_type = 'Chat[edit]'
        info = 'Your chat has been updated!'
        messages.add_message(self.request, messages.INFO, info)
        return super().form_valid(form)

    def test_func(self):
        Chat_post = self.get_object()
        if self.request.user == Chat_post.author:
            return True
        return False


class ChatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chat_post
    success_url = reverse_lazy('chat-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'delete chat'
        context["title_page"] = 'Delete chat'
        return context

    def test_func(self):
        Chat_post = self.get_object()
        if self.request.user == Chat_post.author and self.request.user.profile.user_level > 4:
            return True
        return False 