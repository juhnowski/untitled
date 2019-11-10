import re

from django.db import models
import hashlib


class Request(models.Model):
    """
    Class for user's search requests
    """
    original = models.CharField(
        max_length=250,
        unique=True,
        null=False,
        blank=False,
    )

    purified = models.CharField(
        max_length=250,
        default=None,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.id = int(hashlib.sha256(self.text).hexdigest(), 16)

        self.purified = self.original
        pattern = re.compile('[\W_]+')
        self.purified = pattern.sub(' ', self.original.lower())
        self.purified = re.sub(r'[\W_]+', '', self.purified)

        # words = self.purified.split()

        super(Request, self).save(*args, **kwargs)


class Word(models.Model):
    """
        Class for words in the request
    """
    word = models.CharField(
        max_length=10,
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.id = int(hashlib.sha256(self.text).hexdigest(), 16)
        pattern = re.compile('[\W_]+')
        self.text = pattern.sub(' ', self.text.lower())


class StopWord(Word):
    """
    Class for ignored words in the request
    """


class TotalIndex(models.Model):
    """
    Class for Total Index of Words in the Requests and it's positions in the request
    """
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


class WordInRequest(models.Model):
    """
    Words in Request
    """
    totalIndex = models.ForeignKey(TotalIndex, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


class WordPositionsInRequest(models.Model):
    """
    Word Positions In Request
    """
    position = models.IntegerField()
    wordInRequest = models.ForeignKey(WordInRequest, on_delete=models.CASCADE)


class RequestResponse(models.Model):
    """
        Class for responses proposals of similar requests
    """
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    # proposal = models.ForeignKey(Request, on_delete=models.CASCADE)
