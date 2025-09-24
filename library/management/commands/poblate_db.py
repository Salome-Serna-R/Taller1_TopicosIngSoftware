from django.core.management.base import BaseCommand
from library.models import Content
import os
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import json

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        json_file_path = r'C:\Users\jhond\projectP1\WeCare\library\management\commands\content.json'
        
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            for content in data:
                mental_content = Content(
                    title=content['title'],
                    description=content['description'],
                    image=content['image'],
                    url=content['url'],
                    topic=content['topic']
                )
                mental_content.save()
                print(f'Content {mental_content.title} created')
                
        print('Database populated')
        
        