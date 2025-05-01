class Blockbuster:
  def __init__(self):
    self.movie_db = {}

  def __repr__(self):
    return "Blockbuster Movie Database: {}".format(self.movie_db)

  def add_movie(self, movie):
    self.movie_db[movie.title] = {'year': movie.year, 'runtime': movie.runtime}


class Movie:
  mov_id_counter = 1  # attribute to keep track of the ID
  def __init__(self, title, year, runtime):
    self.movie_id = Movie.mov_id_counter  # assign the current counter value to the instance
    Movie.mov_id_counter += 1  # increment the counter for the next instance
    self.title = title
    self.year = year
    self.runtime = runtime
    self.lender = []

  def __repr__(self):
    return "Movie id_{0} description: \n  - Title:\t{1} \n  - Year:\t{2} \n  - Runtime:\t{3}".format(self.movie_id, self.title, self.year, self.runtime)
  


class User:
  id_counter = 1  # attribute to keep track of the ID
  def __init__(self, name):
    self.name = name
    self.id = User.id_counter  # assign the current counter value to the instance
    User.id_counter += 1  # increment the counter for the next instance
    self.movie_borrow = []

  def __repr__(self):
    return "User {} id_{} has borrowed {} movies".format(self.name, self.id, len(self.movie_borrow))

  def borrow_movie(self, blockbuster, movie_title):
    if movie_title in blockbuster.movie_db:
      self.movie_borrow.append(movie_title)
      print(f"{self.name} borrowed '{movie_title}'")
    else:
      print(f"'{movie_title}' is not available in the Blockbuster database.")
