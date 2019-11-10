from django.contrib.auth.models import User, Group
from app.models import Request, StopWord, Word, TotalIndex, WordInRequest, WordPositionsInRequest, RequestResponse
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer, RequestSerializer, StopWordSerializer, WordSerializer, \
    TotalIndexSerializer, WordInRequestSerializer, WordPositionsInRequestSerializer, RequestResponseSerializer

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


class StopWordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stop words to be viewed or edited.
    """
    queryset = StopWord.objects.all()
    serializer_class = StopWordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows words from all requests to be viewed or edited.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class TotalIndexViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows words total index to be viewed or edited.
    """
    queryset = TotalIndex.objects.all()
    serializer_class = TotalIndexSerializer


class WordInRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows words in request to be viewed or edited.
    """
    queryset = WordInRequest.objects.all()
    serializer_class = WordInRequestSerializer


class WordPositionsInRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows word position in request to be viewed or edited.
    """
    queryset = WordPositionsInRequest.objects.all()
    serializer_class = WordPositionsInRequestSerializer


class RequestResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows word position in request to be viewed or edited.
    """
    queryset = RequestResponse.objects.all()
    serializer_class = RequestResponseSerializer
