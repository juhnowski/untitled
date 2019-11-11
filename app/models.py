import re
from django.db import models, transaction
import hashlib

from django.db.models.signals import post_save
from django.dispatch import receiver


class Request(models.Model):
	"""
	Class for user's search requests
	"""
	id = models.CharField(
		max_length=100,
		primary_key=True)

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
		self.purified = self.original
		pattern = re.compile('[\W_]+')
		self.purified = pattern.sub(' ', self.original.lower())
		self.purified = self.original.lower()
		self.purified = re.sub(r'[\W_]+', '', self.purified)
		self.id = int(hashlib.sha256(self.purified.encode('utf-8')).hexdigest(), 16)
		super(Request, self).save(*args, **kwargs)

		words = self.original.split()
		position_idx = 0
		for w in words:
			the_word = Word(word=w)
			the_word.save()
			total_index = TotalIndex(word=the_word)
			total_index.save()

			word_in_request = WordInRequest(totalIndex=total_index, request_id=self.id)
			word_in_request.save()

			word_positions_in_request = WordPositionsInRequest(position=position_idx, wordInRequest=word_in_request)
			word_positions_in_request.save()

			try:
				ti = TotalIndex.objects.get(word=w)
				wir = WordInRequest.objects.get(total_index=ti)
				for wi in wir:
					request_response = RequestResponse(request_id=self.id, proposal=wi.request)
					request_response.save()
			except:
				request_response = RequestResponse(request_id=self.id, proposal_id=self.id)
				request_response.save()

			position_idx += 1


class Word(models.Model):
	"""
	   Class for words in the request
	"""
	id = models.CharField(
		max_length=100,
		primary_key=True)

	word = models.CharField(
		max_length=10,
		unique=True,
	)

	def save(self, *args, **kwargs):
		utf8s = self.word.__str__()
		self.id = int(hashlib.sha256(utf8s.encode('utf-8')).hexdigest(), 16)
		pattern = re.compile('[\W_]+')
		self.word = pattern.sub(' ', utf8s.lower())
		super(Word, self).save(*args, **kwargs)

# @receiver(post_save, sender=Request)
# def create_word(sender, instance, created, **kwargs):
# 	if created:
#
# 		words = instance.original.split()
# 		position_idx = 0
# 		for w in words:
# 			# the_word = Word.objects.create(word=w)
# 			# the_word.save()
# 			the_word = StopWord(word=w)
# 			the_word.save()
# 			print("-----------create_word-------------------")
# 			print(w)
# 			print(the_word.id)
# 			print("------------------------------")
#
#
# @receiver(post_save, sender=Request)
# def save_word(sender, instance, **kwargs):
#
# 	words = instance.original.split()
# 	position_idx = 0
# 	for w in words:
# 		# the_word = Word.objects.create(word=w)
# 		# the_word.save()
# 		the_word = StopWord(word=w)
# 		the_word.save()
# 		print("------------save_word------------------")
# 		print(w)
# 		print(the_word.id)
# 		print("------------------------------")


class StopWord(models.Model):
	"""
	   Class for ignored words in the request
	"""
	id = models.CharField(
		max_length=100,
		primary_key=True,
	)

	word = models.CharField(
		max_length=10,
		unique=True,
	)

	def save(self, *args, **kwargs):
		utf8s = self.word.__str__()
		self.id = int(hashlib.sha256(utf8s.encode('utf-8')).hexdigest(), 16)
		pattern = re.compile('[\W_]+')
		self.word = pattern.sub(' ', utf8s.lower())
		super(StopWord, self).save(*args, **kwargs)


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
	request = models.ForeignKey(Request,
	                            related_name='request1_request_id',
	                            on_delete=models.CASCADE)

	proposal = models.ForeignKey(Request,
	                             related_name='proposal_request_id',
	                             on_delete=models.CASCADE,
	                             default=None,
	                             blank=True,
	                             null=True)
