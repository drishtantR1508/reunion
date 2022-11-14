from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import PostSerializer,CommentsSerializer
from .models import Post
from django.core.files import File
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_post(self,pk):
        return Post.objects.get(pk=pk)
        
    def get(self,request,pk=None,format=None):
        if pk: #if user has passed pk in url that means he wants to get a specific user and we will use other function to achieve that
            data = self.get_post(pk=pk)
            serializer = PostSerializer(data)
            return Response(serializer.data)
        else:
            data = Post.objects.filter(written_by=request.user)
            serializer = PostSerializer(data, many=True)
            return Response(serializer.data)
        
    def post(self,request,format=None):
        json_data = request.data
        serializer = PostSerializer(data=json_data,partial=True,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Post Created Successfully',
            'data': serializer.data
        }
        return response
        
    def put(self,request,pk,format=None):
        print(pk)
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance = post,data=request.data,partial=True,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Post updated Successfully',
            'data': serializer.data
        }
        return response



    def delete(self, request,pk,format=None):
        Post.objects.get(pk=pk).delete()
        return Response({
            'message': 'Deleted Successfully'
        })


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk,format=None):
        json_data = request.data 
        serializer = CommentsSerializer(data=json_data,partial=True,context={'request':request,'pk':pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Comment Created Successfully',
            'data': serializer.data
        }
        return response


class PostLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk,format=None):
        post = get_object_or_404(Post,id=pk)
        response = Response()
        if post.like.filter(id=request.user.id).exists():
            response.data = {
                'message': 'Already Liked',
            }
        else:
            post.like.add(request.user)
            response.data = {
                'message': 'Successfully Liked',
            }

        return response
        

class PostUnlikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk,format=None):
        post = get_object_or_404(Post,id=pk)
        response = Response()
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            response.data = {
                'message': 'Successfully Unliked',
            }
        else:
            response.data = {
                'message': 'Already Unliked',
            }

        return response
        