from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.contrib.auth.models import User
from rest_auth.registration.views import SocialLoginView
from rest_framework.views import APIView
from rest_framework.response import Response


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class CurrentUser(APIView):
    def get(self, request):
        user = request.user
        return Response(user.username)

