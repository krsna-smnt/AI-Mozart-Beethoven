''' pg_midi_sound101.py
play midi music files (also mp3 files) using pygame
tested with Python273/331 and pygame192 by vegaseat
'''

import pygame as pg

def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return

    pg.mixer.music.play()
    # check if playback has finished
    while pg.mixer.music.get_busy():
        clock.tick(30)


def play(file): 
	music_file = "/home/abhay/Desktop/Django/MusicApp/" + file

	freq = 44100    # audio CD quality
	bitsize = -16   # unsigned 16 bit
	channels = 2    # 1 is mono, 2 is stereo
	buffer = 2048   # number of samples (experiment to get right sound)
	pg.mixer.init(freq, bitsize, channels, buffer)

	pg.mixer.music.set_volume(0.8)

	try:
	    play_music(music_file)
	except KeyboardInterrupt:
	    pg.mixer.music.fadeout(1000)
	    pg.mixer.music.stop()
	    # raise SystemExit