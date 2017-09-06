from factory import DjangoModelFactory, LazyAttribute

from demo_models.models import Place

from .factory_faker import Faker

__all__ = (
    'PlaceFactory',
)


class BasePlaceFactory(DjangoModelFactory):
    """Base Place factory."""

    name = Faker('first_name')
    address = Faker('address')

    class Meta(object):
        """Meta class."""

        model = Place
        abstract = True


class PlaceFactory(BasePlaceFactory):
    """Place factory."""
