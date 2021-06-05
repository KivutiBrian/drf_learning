from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
from .models import Post


# Create your views here.
class PostView(APIView):

    permission_classes = (IsAuthenticated, )

    # get posts
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # add new post
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        # validate the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # raise an error if invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        