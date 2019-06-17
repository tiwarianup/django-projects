from django.core.management.base import BaseCommand, CommandError
from shortner.models import ShortUrl

class Command(BaseCommand):
    help = "Refreshes all the URL Short Codes in the Database."

    def handle(self, *args, **kwargs):
        return ShortUrl.objects.refreshShortcodes()

