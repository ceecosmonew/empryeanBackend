from rest_framework import serializers

from .models import StudentInfo
class StudentInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentInfo
        fields = '__all__'

