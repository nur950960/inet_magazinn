from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Products 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import PostSerializer, PostListSerializer
from .permissons import  IsOwnerorReadOnly




class PostViewSet( ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields=['title']


    def get_serializer_class(self):
        if self.action =='list':
            return PostListSerializer
        return self.serializer_class
    
    def get_serializer_context(self):
        return {'request':self.request}


    def get_permissions(self):
            if self.action in ['list', 'retrieve']:
                self.permission_classes = [AllowAny]
            elif self.action in ['create']:
                self.permission_classes = [IsAuthenticated]
            elif self.action in ['update', 'partial_update', 'destroy']:
                self.permission_classes = [IsOwnerorReadOnly]
            return [permission() for permission in self.permission_classes]