from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet  # the model that will be serialized
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']  # the fields that will be serialized

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(
#         read_only=True)  # read_only=True means that the field is used when updating an instance, but is not required when creating an instance
#     title = serializers.CharField(required=False, allow_blank=True,
#                                   max_length=100)  # required=False means that the field is not required when updating an instance
#     code = serializers.CharField(style={
#         'base_template': 'textarea.html'})  # style={'base_template': 'textarea.html'} means that the field will be displayed as a HTML textarea element instead of the default input element
#     linenos = serializers.BooleanField(
#         required=False)  # required=False means that the field is not required when updating an instance
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
#                                        default='python')  # choices=LANGUAGE_CHOICES limits the choices to the ones we defined above
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,
#                                     default='friendly')  # choices=STYLE_CHOICES limits the choices to the ones we defined above
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         # instance.title = validated_data['title']  # same as above but without default value
#         instance.code = validated_data.get('code', instance.code)  # same as above but without default value
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()  # save the instance to the database
#         return instance  # return the updated instance
