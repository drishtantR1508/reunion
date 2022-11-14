from rest_framework import serializers
from .models import Post,Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

    def create(self,validated_data):
        print(self.context)
        user =  self.context['request'].user
        post = Post.objects.get(pk=self.context['pk'])
        comment = Comments.objects.create(
            post = post,
            written_by = user,
            **validated_data
        )
        return comment  

class PostSerializer(serializers.ModelSerializer):
    no_of_likes = serializers.CharField(source='count_likes')
    comments = CommentsSerializer(many=True,read_only=True) #I used Nested serializers because they are customisable. 
    class Meta:
        model = Post
        fields = "__all__" 

    def create(self,validated_data):
        print(self.context)
        user =  self.context['request'].user
        # prin
        post = Post.objects.create(
            written_by=user, 
            **validated_data
        )
        return post              

   