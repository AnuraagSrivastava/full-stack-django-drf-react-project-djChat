
from django.conf import settings
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    '''blank and null = True will allow to enter no description, its not 
    mandatory.'''
    description = models.TextField(blank=True, null=True)

# below function to identify different objects returned from DB
    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=100)

    '''In below line, if user from system(abstract user table) is deleted then the server associated to that user will also be deleted.'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="server_owner")

    '''below shows one to many relationship as 1 category can be related to 
    many servers - below shows one to many relationship'''
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="server_category")
    description = models.CharField(max_length=250,
                                   blank=True,
                                   null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # below function to identify different objects returned from DB
    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    # below is for who created the channel
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="channel_owner")
    topic = models.CharField(max_length=100)
    # multiple channels link to one server
    server = models.ForeignKey(Server,
                               on_delete=models.CASCADE,
                               related_name="channel_server")

    '''does not matter how data comes in form caps or small,will always be save as small.Thus, save method is override'''

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    # below function to identify different objects returned from DB
    def __str__(self):
        return self.name
