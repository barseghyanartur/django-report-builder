from factory import DjangoModelFactory, LazyAttribute, post_generation

from demo_models.models import Bar

from .factory_faker import Faker
from .demo_models_foo import FooFactory

__all__ = (
    'BarFactory',
)


class BaseBarFactory(DjangoModelFactory):
    """Base Bar factory."""

    char_field = Faker('text', max_nb_chars=50)

    class Meta(object):
        """Meta class."""

        model = Bar
        abstract = True

    @post_generation
    def foos(obj, created, extracted, **kwargs):
        """Create `Foo` objects for the created `Bar` instance."""
        if created:
            # Create 4 `Foo` objects.
            foos = FooFactory.create_batch(4, **kwargs)
            obj.foos.add(*foos)


class BarFactory(BaseBarFactory):
    """Bar factory."""
