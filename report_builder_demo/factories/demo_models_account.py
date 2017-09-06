from factory import DjangoModelFactory, LazyAttribute

from demo_models.models import Account

from .factory_faker import Faker

__all__ = (
    'AccountFactory',
)


class BaseAccountFactory(DjangoModelFactory):
    """Base Account factory."""

    name = Faker('first_name')
    balance = Faker('pydecimal', left_digits=8, right_digits=2, positive=True)
    budget = Faker('pydecimal', left_digits=16, right_digits=4, positive=True)

    class Meta(object):
        """Meta class."""

        model = Account
        abstract = True


class AccountFactory(BaseAccountFactory):
    """Account factory."""
