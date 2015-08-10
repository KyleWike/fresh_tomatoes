import fresh_tomatoes
import media

#Create the different objects from the class in media.py
how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
                        "A story of a boy who befriends a dragon",
                        "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                        "https://www.youtube.com/watch?v=oKiYuIsPxYk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
                     
die_hard = media.Movie("Die Hard",
                       "A cop gets pulled into a terrorist plot",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Die_hard.jpg/220px-Die_hard.jpg",
                       "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

#combine the objects into a list                       
movies = [die_hard,avatar,how_to_train_your_dragon]

#call the list using the fresh_tomatoes.py program to generate the webpage
fresh_tomatoes.open_movies_page(movies)
