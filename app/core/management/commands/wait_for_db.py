"""
Django command to wait for the db to be available (before app begins).
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""
    
    def handle(self, *args, **options):
        pass
