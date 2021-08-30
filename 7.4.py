from faker import Faker
fake=Faker()
import random
from datetime import date

class movie():
    def __init__(self, title, release_date, genre, views):
        self.title=title
        self.release_date=release_date
        self.genre=genre
        self.views=views
    
    def __str__(self):
        return f'{self.title} ({self.release_date})'

    def play(self, step=1):
        self.views+=step

    def get_movies():
        movies=[]
        for i in library:
            if isinstance(i,series) == False:
                movies.append(i)
        movies_sorted=sorted(movies, key=lambda movie: (movie.title, movie.release_date))
        return movies_sorted

    def random_movie_generator():
        all_movie_genres=["comedy", "horror", "criminal", "romance"]
        random_movie_names=["Hunter Of The Past", "Angel From Outer Space", "Agents Of Earth", "Creators On My Ship", "Soldiers And Aliens",
        "Puzzle Of The Titans", "Armies Of Destruction", "Wolf Of Stone", "Heirs Of Bad News","Red Fairy","Lights of Swords"]
        movie_title=random.choice(random_movie_names)
        release_year=random.randint(1950,2021)
        movie_genre=random.choice(all_movie_genres)
        generated_movie=movie(title=movie_title, release_date=release_year, genre=movie_genre, views=0)
        return generated_movie


class series(movie):
    def __init__(self,episode_number, season_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number=episode_number
        self.season_number=season_number
    
    def play(self, step=1):
        self.views+=step

    def __str__(self):
        season='{:02.0f}'.format(self.season_number)
        eposode='{:02.0f}'.format(self.episode_number)
        return f'{self.title} S{season}E{eposode}'


    def get_series():
        shows=[]
        for i in library:
            if isinstance(i,series) == True:
                shows.append(i)
        shows_sorted=sorted(shows, key=lambda series: (series.title, series.season_number, series.episode_number))
        return shows_sorted

# Funkcja która liczy wszystkie odcinki danego serialu
    # def episode_counter():
    #     show_name=input("Which series are you looking for?")
    #     no_episodes=0
    #     for i in library:
    #         if isinstance(i, series)==True and i.title==show_name:
    #             no_episodes+=1
    #     return no_episodes

    def random_series_generator():
        all_series_genres=["comedy", "horror", "criminal", "romance"]
        random_series_names=["Broken Dragon", "The Bare Snow", "Woman of Destruction", "The Slave's Time", "The Person of the Willow",
        "The Misty's River", "The Lover of the Star", "The Weeping Witch", "Thorns of Darkness"]
        series_title=random.choice(random_series_names)
        release_year=random.randint(1950,2021)
        series_genre=random.choice(all_series_genres)
        no_episode=random.randint(1,25)
        no_season=random.randint(1,5)
        generated_series=series(title=series_title, release_date=release_year, genre=series_genre, views=0, episode_number=no_episode,season_number=no_season)
        return generated_series


library=[]


#Funkcja która wyszukuje film/serial po nazwie
def search():
    search=input("What movie or series are you looking for?")
    for i in library:
        if search==i.title:
            print(i)




# for i in series.get_series():
#     print(i)

# Funkcja która pozwala użytkownikowi wygenerować spersonalizowaną toplistę
# def top_titles():
#     content_type=input("Are you looking for series or a movie?")
#     content_amount=input("How many recomendations would you like to see?")
#     content_amount_int=int(content_amount)
#     if content_type=="movie":
#         movies=[]
#         for i in library:
#             if isinstance(i, series)==False:
#                 movies.append(i)
#         movies_popularity=sorted(movies, key=lambda movie: movie.views, reverse=True)
#         return movies_popularity[:content_amount_int]
#     elif content_type=="series":
#         shows=[]
#         for i in library:
#             if isinstance(i, series)==True:
#                 shows.append(i)
#         shows_popularity=sorted(shows, key=lambda series: series.views, reverse=True)
#         return shows_popularity[:content_amount_int]

# Funkcja która dodaje pełne sezony serialu do biblioteki
# def series_creator():  
#     show_list=[]
#     show_title=input("Name of the show:")
#     no_season=input("Which season?")
#     no_episodes=input("How many episodes?")
#     no_season_int=int(no_season)
#     no_episodes_int=int(no_episodes)
#     release_year=input("When was it released?")
#     show_genre=input("What genre is it?")
#     for i in range(no_episodes_int):
#         show_list.append(series(title=show_title, release_date=release_year, genre=show_genre, views=0, episode_number=i+1, season_number=no_season_int))
#     return show_list
# library+=(series_creator())

def top_movies(amount):
    movies=[]
    for i in library:
        if isinstance(i, series)==False:
            movies.append(i)
    movies_popularity=sorted(movies, key=lambda movie: movie.views, reverse=True)
    return movies_popularity[:amount]

def top_series(amount):
    shows=[]
    for i in library:
        if isinstance(i, series)==True:
            shows.append(i)
    shows_popularity=sorted(shows, key=lambda series: series.views, reverse=True)
    return shows_popularity[:amount]

def generate_views():
    random_selection=random.choice(library)
    for i in range(random.randint(1,100)):
        random_selection.play()


# print(series.episode_counter())

def library_generator():
    generated_content=[]
    amount_movies=random.randint(5,10)
    for i in range(amount_movies):
        generated_content.append(movie.random_movie_generator())
    amount_series=random.randint(5,15)
    for i in range(amount_series):
        generated_content.append(series.random_series_generator())
    return generated_content
library+=(library_generator())


print("Biblioteka filmów:")
for i in movie.get_movies():
    print(i)
for i in series.get_series():
    print(i)

for i in range(10):
    generate_views()
day=date.today()
print(f"Najpopularnijsze filmy i seriale dnia {day.strftime('%d/%m/%Y')}:")
print("Filmy:")
for i in (top_movies(3)):
    print(i)
print("Seriale:")
for i in (top_series(3)):
    print(i)