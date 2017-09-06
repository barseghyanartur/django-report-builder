import random

from factory import DjangoModelFactory, LazyAttribute

from demo_models.models import Foo

from .factory_faker import Faker

__all__ = (
    'FooFactory',
)


class BaseFooFactory(DjangoModelFactory):
    """Base author factory."""

    char_field = Faker('text', max_nb_chars=50)
    char_field2 = Faker('text', max_nb_chars=50)

    class Meta(object):
        """Meta class."""

        model = Foo
        abstract = True


class FooFactory(BaseFooFactory):
    """Foo factory."""

