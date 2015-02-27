Summary: This application reads entertainment_center.py for favorite movie data, defined by class in
	media.py and uses fresh_tomatoes.py to format the data into HTML and opens in a browser window.


Files:
	fresh_tomatoes.py: provided which contains code to render data into HTML file and open in browser
		Edited to display Release Year and MPAA Rating
	media.py: contains class definitions for movie
	entertainment_center.py: contains my favorite movie data


Instructions:
	Extract all files to the same folder

	Edit entertainment_center.py file to contain your favorite movies and be sure to add the movie 
	instance variable to the List of movies to call (movies =..." string.

	Run the entertainment_center.py module to generate the HTML and launch the browser.


Format:
	<<movie_instance>> = media.Movie(<<Movie title string>>, 
					 <<Movie description string>>, 
					 <<URL string for movie box art image>>,
					 <<URL string for trailer on youtube>>,
					 <<String for year released>>,
					 <<String for MPAA movie rating>>
					 )
	movies = [<<movie instance variable 1>>, <<movie instance variable 2>>, <<movie instance variable 3>>...]
