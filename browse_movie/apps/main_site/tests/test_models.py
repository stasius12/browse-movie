import pytest

from browse_movie.apps.main_site.models import WatchList


@pytest.mark.django_db
@pytest.mark.parametrize('movie,added_movie', [
    ('movie1', 'movie1'),
    ('movie2 ', 'movie2'),
    (' movie3', 'movie3')
])
def test_add_remove_movie_different(create_user, movie, added_movie):
    watchlist = WatchList.objects.create(user=create_user())

    watchlist.add_movie(movie)
    assert len(watchlist.movies_id) == 1
    assert added_movie in watchlist.movies_id

    watchlist.remove_movie(movie)
    assert len(watchlist.movies_id) == 0
    assert not added_movie in watchlist.movies_id


def test_add_remove_movie(create_user):
    watchlist = WatchList.objects.create(user=create_user())

    watchlist.add_movie('movie1')
    assert len(watchlist.movies_id) == 1
    assert 'movie1' in watchlist.movies_id

    watchlist.add_movie('movie2')
    assert len(watchlist.movies_id) == 2
    assert 'movie2' in watchlist.movies_id

    watchlist.remove_movie('movie2')
    assert len(watchlist.movies_id) == 1
    assert not 'movie2' in watchlist.movies_id
    assert 'movie1' in watchlist.movies_id
