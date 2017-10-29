# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MusicForm
from .models import Music
from utilities import pyprgm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = MusicForm(request.POST, request.FILES)
		if form.is_valid():
			# form.save()
			song = Music(audio = request.FILES['audio'])

			mdiurl = 'media/'
			mdiurl += song.audio.url
			mdiurl = mdiurl.replace("/media/", "", 1)

			song.save()
			pyprgm.play(mdiurl)
			song.delete()
	
	form = MusicForm()
	audios = Music.objects.all()

	return render(request, 'Website/index.html', {'audios': audios, 'form': form})


# def play(request, songid):
# 	song = Music.objects.get(pk=songid)
	
# 	link = song.audio.url.replace("/media/", "", 1)
	
# 	print link

# 	pyprgm.play(link)

# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
