# from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# # class SnippetSerializer(serializers.Serializer):
# #     id = serializers.IntegerField(read_only=True)
# #     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# #     code = serializers.CharField(style={'base_template': 'textarea.html'})
# #     linenos = serializers.BooleanField(required=False)
# #     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# #     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# owner = serializers.ReadOnlyField(source='owner.username')

# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets', 'owner',]    

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.ModelSerializer):

class SnippetSerializer(serializers.HyperlinkedModelSerializer): # Hyperlink
    owner = serializers.ReadOnlyField(source='owner.username') # new
    
    highlight = serializers.HyperlinkedIdentityField( # Hyperlink
        view_name='snippet-highlight', format='html')

    # class Meta:
    #     model = Snippet
    #     fields = ('id', 'title', 'code', 'linenos',
    #               'language', 'owner','style', ) # new 
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos',
                  'language', 'style', 'owner',) # Hyperlink

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

class UserSerializer(serializers.HyperlinkedModelSerializer): # Hyperlink
    snippets = serializers.HyperlinkedRelatedField( # Hyperlink
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets') # Hyperlink