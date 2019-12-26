from empresa.views import EmpresaList
from notes.api import NoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empresas', EmpresaList)
router.register('notes', NoteViewSet)