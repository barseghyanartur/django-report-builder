from factory import DjangoModelFactory, SubFactory, LazyAttribute

from demo_models.models import Restaurant

from .factory_faker import Faker

__all__ = (
    'RestaurantFactory',
)


class BaseRestaurantFactory(DjangoModelFactory):
    """Base Restaurant factory."""

    place = SubFactory('factories.demo_models_place.PlaceFactory')
    serves_hot_dogs = Faker('pybool')
    serves_pizza = Faker('pybool')

    class Meta(object):
        """Meta class."""

        model = Restaurant
        abstract = True


class RestaurantFactory(BaseRestaurantFactory):
    """Restaurant factory."""
