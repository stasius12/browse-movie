import pytest
from django import urls


@pytest.mark.django_db
def test_home_page(client):
    """
    Verify that home page is not accessible without loging in and properly redirects to login page
    """
    url = urls.reverse('main_site:home_page')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == urls.reverse('account_login') + '?next=/'

    response = client.get(url, follow=True)
    assert response.status_code == 200


def test_home_page_admin(admin_client):
    """
    Verify that home page is accessible for admin
    """
    url = urls.reverse('main_site:home_page')
    response = admin_client.get(url)
    assert response.status_code == 200
