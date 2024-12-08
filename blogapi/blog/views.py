from rest_framework import viewsets, permissions, status, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	@action(detail=True)
	def like(self, request, pk=None):
		blogpost = self.get_object()
		blogpost.likes = blogpost.likes + 1
		blogpost.save()

		return Response(
			{
				'status': f'{blogpost.title} just got a like.',
				'likes': f'{blogpost.likes}',
			},
			status = status.HTTP_200_OK,
		)

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def read(self, request, pk=None):
		blogpost = self.get_object()
		return Response(blogpost.body)

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer