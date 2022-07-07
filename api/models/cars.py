from django.db import models
from rest_framework import serializers
import uuid
# const
EMPTY = {'null': True, 'blank': True}



# Model [DB Driver]
class Car(models.Model):
    # fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    carbrand = models.CharField(max_length=50, **EMPTY)
    patent   = models.CharField(max_length=100, **EMPTY)
    owner    = models.CharField(max_length=50, **EMPTY)
    email    = models.EmailField(max_length=50, **EMPTY)
    
    # methods
    def __str__(self):
        return str(self.username)



# Schemas [serializer] [endpoints]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['carbrand', 'patent', 'owner', 'email'] # fields= '__all__'