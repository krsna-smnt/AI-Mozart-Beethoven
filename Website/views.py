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
			# command = "timidity " + song.audio.url + " -Ow out.mp3"

	return render(request, 'Website/index.html', {})

def play_it(request):
	os.system("th sample.lua cv/epoch")
	os.system("ruby txt_to_midi.rb ip.txt")

	urll = ""

	return render(request, 'Website/play_it.html', {'urll': urll})
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
