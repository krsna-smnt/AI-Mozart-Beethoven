# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MusicForm
from .models import Music
from utilities import pyprgm
from django.http import HttpResponseRedirect

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

			# pyprgm.play(mdiurl)			     
			# song.delete()
	
	form = MusicForm()
	audios = Music.objects.all()

	if audios:
		song = audios[0]
	else:
		song = audios

	return render(request, 'Website/index.html', {'song': song, 'form': form})
