# Libs
from core.models import BaseCommand
from core.mapping import Mapping


class ProviderList(BaseCommand):
    command = 'provider ls'
    def run(self):
        providers = len(Mapping().get_providers())
        print(f"\nProviders installed : {providers}")
