import pytest

from django.urls import reverse


@pytest.amrk.django_db
def tesr_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200