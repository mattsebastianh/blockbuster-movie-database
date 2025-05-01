# tests/test_blockbuster.py
import pytest
import sys
sys.path.append('..')
from blockbuster import Blockbuster, Movie, User

def test_blockbuster_init():
    blockbuster = Blockbuster()
    assert blockbuster.movie_db == {}

def test_blockbuster_add_movie():
    blockbuster = Blockbuster()
    movie = Movie("The Shawshank Redemption", 1994, 142)
    blockbuster.add_movie(movie)
    assert blockbuster.movie_db == {"The Shawshank Redemption": {"year": 1994, "runtime": 142}}

def test_blockbuster_repr():
    blockbuster = Blockbuster()
    movie = Movie("The Shawshank Redemption", 1994, 142)
    blockbuster.add_movie(movie)
    expected = "Blockbuster Movie Database: {'The Shawshank Redemption': {'year': 1994, 'runtime': 142}}"
    assert repr(blockbuster) == expected

def test_movie_init():
    movie = Movie("The Shawshank Redemption", 1994, 142)
    assert movie.title == "The Shawshank Redemption"
    assert movie.year == 1994
    assert movie.runtime == 142
    assert movie.lender == []

def test_movie_repr():
    movie = Movie("The Shawshank Redemption", 1994, 142)
    assert repr(movie) == "Movie id_1 description: \n  - Title:\tThe Shawshank Redemption \n  - Year:\t1994 \n  - Runtime:\t142"

def test_user_init():
    user = User("John Doe")
    assert user.name == "John Doe"
    assert user.id == 1
    assert user.movie_borrow == []

def test_user_repr():
    user = User("John Doe")
    assert repr(user) == "User John Doe id_1 has borrowed 0 movies"

def test_user_borrow_movie():
    blockbuster = Blockbuster()
    movie = Movie("The Shawshank Redemption", 1994, 142)
    blockbuster.add_movie(movie)
    user = User("John Doe")
    user.borrow_movie(blockbuster, "The Shawshank Redemption")
    assert user.movie_borrow == ["The Shawshank Redemption"]

def test_user_borrow_movie_not_available():
    blockbuster = Blockbuster()
    user = User("John Doe")
    with pytest.raises(AssertionError):
        user.borrow_movie(blockbuster, "The Shawshank Redemption")