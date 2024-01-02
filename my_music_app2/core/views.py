from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView

from my_music_app2.albums.models import Album
from my_music_app2.users.models import Profile


class IndexView(View):
    # template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        profile = self.get_profile()

        if profile is None:
            return CreateProfileView.as_view()(request)

        # context = {
        #     'albums': Album.objects.all(),
        # }
        return HomePageNoProfile.as_view()(request)
        # return render(request, 'core/home-with-profile.html', context)

    def get_profile(self):
        try:
            return Profile.objects.get()
        except Profile.DoesNotExist:
            return None

class CreateProfileView(CreateView):
    model = Profile
    fields = "__all__"
    template_name = 'core/home-no-profile.html'
    success_url = '/'  # Replace with your actual URL

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     return response
    #
    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     return response
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class HomePageNoProfile(ListView):
    model = Album
    template_name = "core/home-with-profile.html"
