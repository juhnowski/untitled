from django.contrib.auth.models import User, Group
from rest_framework import serializers

from app.models import Request, StopWord, TotalIndex, WordInRequest, WordPositionsInRequest, Word, RequestResponse

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ['original', 'purified']


class StopWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StopWord
        fields = ['word']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['word']


class RequestResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestResponse
        fields = ['request', 'proposal']


class TotalIndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TotalIndex
        fields = ['word']


class WordInRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordInRequest
        fields = ['totalIndex', 'request']


class WordPositionsInRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordPositionsInRequest
        fields = ['position', 'wordInRequest']