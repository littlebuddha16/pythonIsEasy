"""
	Homework Assignment #2
	Functions
	Favourite Song
							"""
melody = 'Nagumomu Ganaleni' 
classification = 'Carnatic'
speech = 'Telugu'
composedBy = 'Tyagaraja'
singer = 'Tyagaraja'
releaseDate = 1800 # A rough estimate

def Song():
	return melody

def Genre():
	return classification

def Artist():
	return singer

# You could use below function to check the genre of the music

def genreCheck(music):
	return music.lower() == classification.lower()