from django.contrib.auth.models import User, Group
from app.models import Request
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer, RequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user's search requests to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
