from rest_framework import serializers
from .models import Notes


#this is serializer which help the models field. 
class NotesSerializer(serializers.ModelSerializer):
    audionotes = serializers.FileField()
    videonotes = serializers.FileField()
    
    class Meta:
        model = Notes
        fields = ['id','notes','audionotes','videonotes']
