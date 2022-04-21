import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Script only for creation superuser on Elastic Beanstalk.
    TODO: Should be removed in future (Alternatively make dump with a superuser locally and load him on stage/prod)
    """

    def handle(self, *args, **options):
        admin_username = os.getenv('DEFAULT_ADMIN_USERNAME', 'admin')
        admin_email = os.getenv('DEFAULT_ADMIN_EMAIL', 'admin@admin.com')
        admin_password = os.getenv('DEFAULT_ADMIN_PASSWORD', 'qwerty123')

        if not get_user_model().objects.filter(username=admin_username).exists():
            get_user_model().objects.create_superuser(admin_username,
                                                      admin_email,
                                                      admin_password)
            print('Superuser was created successfully')
            return

        print('Superuser exists already')
