from rest_framework import serializers
from .models import Music, Artist, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', )

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', )

#ArtistDetail 과 로직이 동일!
class MusicDetailSerailizer(MusicSerializer):
    comments = CommentSerializer(source="comment_set", many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments', )

class ArtistDetailSerializer(ArtistSerializer):
    musics= MusicDetailSerailizer(source="music_set", many=True)
    musics_count = serializers.IntegerField(source='music_set.count')
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count', )
