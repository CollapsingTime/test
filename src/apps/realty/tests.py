import pytest
from apps.realty.models import Flat
from apps.developers.models import Developer


@pytest.mark.django_db
def test_dev_model():
    title = "test dev"
    developer = Developer.objects.create(
            title = title
        )
    
    assert isinstance(developer, Developer)
    assert developer.title == title

@pytest.mark.django_db
def test_flat_model():
    article = "test article"
    area = 10
    price = 5

    developer = Developer.objects.create(
            title = "Test developer"
        )

    flat = Flat.objects.create(
        article=article,
        area=area,
        price=price,
        developer=developer
    )

    assert isinstance(flat, Flat)
    assert flat.article == article
    assert flat.area == area
    assert flat.price == price
    assert flat.developer == developer