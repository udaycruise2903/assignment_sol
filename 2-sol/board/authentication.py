from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    A custom account adapter that inherits from the DefaultAccountAdapter class.
    """

    def get_login_redirect_url(self, request):
        """
        redirects the user to home URL upon successful login
        """
        return reverse_lazy('home')
