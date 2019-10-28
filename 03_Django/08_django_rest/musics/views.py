from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerailizer

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # serializer : musics(queryset) -> json
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerailizer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(requset):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    #request.data -> 사용자가 HTTP body에 담아 날린 댓글(content) 내용
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)

    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(requset, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    # PUT
    if requset.method == 'PUT':
        serializer = CommentSerializer(data=requset.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'message': 'Comment has been updated!!'})
    # DELETE
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted!!'})


@api_view(['GET'])
def comment_list(requset):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)