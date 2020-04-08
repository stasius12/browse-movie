import uuid

import pytest


@pytest.fixture
def create_user(db, django_user_model):
    """ Fixture returning method to create user
        It is possible than to add some custom kwargs
    """
    def make_user(**kwargs):
        kwargs['password'] = 'password'
        if not 'username' in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user
