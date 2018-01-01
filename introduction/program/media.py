import webbrowser

class Movie(object):
	"""Movie init: title, storyline, poster, youtube trailer link """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
		director, stars, release_date, runtime):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.trailer_url = trailer_youtube
		self.director = director
		self.stars = stars
		self.release_date = release_date
		self.runtime = runtime

	"""open movie trailer""" 
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)