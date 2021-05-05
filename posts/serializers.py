from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """Serializer class for posts.
    I ask the author by name so that as a result of the request
    I get a nickname, not an id.
    I do not declare the fields of the model in the view through '__all__',
    I think more will be added, but on the other hand, in the end,
    api should probably put them in a tuple, for a list.
    - - - Deal with pub_date, whether it is worth putting it in read_only =
    """

    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'image']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer class for Comment."""

    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
