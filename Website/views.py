# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MusicForm
from .models import Music
from utilities import pyprgm
from django.http import HttpResponseRedirect
import os

# Create your views here.

def index(request):
	audios = Music.objects.all()
	audios.delete()

	if request.method == 'POST':
		form = MusicForm(request.POST, request.FILES)
		if form.is_valid():
			# form.save()
			song = Music(audio = request.FILES['audio'])

			# mdiurl = 'media/'
			# mdiurl += song.audio.url
			# mdiurl = mdiurl.replace("/media/", "", 1)

			song.save()

			new_url = song.audio.url[1:len(song.audio.url)]
			# command = "timidity " + song.audio.url + " -Ow out.mp3"
			command = "timidity " + new_url + ' -Ow -o media/out.mp3'
			os.system(command)

			# pyprgm.play(mdiurl)			     
			# song.delete()
	
	form = MusicForm()
	audios = Music.objects.all()

	# urll = "/home/abhay/Desktop/Django/AI-Mozart-Beethoven/media/out.mp3"

	if audios:
		print song.audio.url
		song = audios[0]
	else:
		song = audios

	urll = '/media/out.mp3'
	# print urll
	return render(request, 'Website/index.html', {'song': song, 'urll': urll, 'form': form})
