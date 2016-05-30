from django.contrib import admin

# Register your models here.

# accessing the documents for the admin 
from imagic.models import Document
admin.site.register(Document)
