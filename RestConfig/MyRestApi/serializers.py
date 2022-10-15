from rest_framework import serializers
from MyRestApi.models import Contact

# class ContactSerializer(serializers.Serializer):
    
#     name = serializers.CharField(max_length=200)
#     title = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=30)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Contact.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Contact` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.title = validated_data.get('title', instance.title)
#         instance.email = validated_data.get('email', instance.email)

#         instance.save()
#         return instance


# python manage.py shell
# from MyRestApi.models import Contact
# from MyRestApi.serializers import ContactSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# a = Contact(name= 'JSON', title = 'Js', email ='json@gmail.com')
# a.save()

# serializer = ContactSerializer(a)
# serializer.data

# content = JSONRenderer().render(serializer.data)
# content



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']


# from MyRestApi.serializers import ContactSerializer
# serializer = ContactSerializer()
# print(repr(serializer))