import fresh_tomatoes
import media

# create instances of the class Movie (Name of the movie, story line, poster link, youtube trailer)
love_actually = media.Movie("Love actually",
                            "Ten separate stories involving a wide variety of individuals",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Love_Actually_movie.jpg/220px-Love_Actually_movie.jpg",    
                            "https://www.youtube.com/watch?v=peiRtkXMYQ8&index=64&list=PLv3NVjHAFDOJJJCyRValh1VtCh4AHb6f6")

pride_and_prejudice = media.Movie("Pride and Prejudice",
                                  "Story of love and life among English gentility during the Georgian era",
                                  "http://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
                                  "https://www.youtube.com/watch?v=fJA27Jujzq4")

bad_teacher = media.Movie("Bad Teacher",
                          "Story about bad teacher",
                          "http://upload.wikimedia.org/wikipedia/en/b/b2/Bad_Teacher_Poster.jpg",
                          "https://www.youtube.com/watch?v=VihlsPKMh4U")

frozen = media.Movie("Frozen",
                     "Computer-animated musical fantasy–comedy film",
                     "http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

the_internship = media.Movie("The internship",
                             "Story about internship at Google",
                             "http://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
                             "https://www.youtube.com/watch?v=cdnoqCViqUo")

despicable_me = media.Movie("Despicable me",
                            "Story about Gru and his minions",
                            "http://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

# define list of movies
movies = [love_actually, pride_and_prejudice, bad_teacher, frozen, the_internship, despicable_me]

# call function "open movies page"
fresh_tomatoes.open_movies_page(movies)

