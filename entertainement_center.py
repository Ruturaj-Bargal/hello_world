import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an Alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.show_trailer()

dangal = media.Movie("Dangal",
                     "Mhari choriya choro se kam hai ke",
                     "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouilePoster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

#dangal.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using Rock Music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=LqEszt5wG9I")

midnight_in_paris = media.Movie("Midnight in Paris",
                                 "Going back in time to meet the authors",
                                 "http://upload.wikimedia.org/wikipedia/en/1/13/Midnight_in_Paris_Poster.jpg",
                                 "https://www.youtube.com/watch?v=BYRWfS2s2v4")


hunger_games = media.Movie("Hunger Games",
                            "A really real reality show",
                            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, dangal, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)                                





