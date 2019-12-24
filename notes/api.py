from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    # permission_classes = [permissions.AllowAny, ]
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer


