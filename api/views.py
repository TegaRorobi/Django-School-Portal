from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubjectSerializer
from main.models import Subject

@api_view(['GET'])
def getRoutes(request):
	routes = [
		'GET /api/',
		'GET /api/subjects/',
	]
	return Response(routes)

@api_view(['GET'])
def getSubjects(request):
	subjects = Subject.objects.all()
	serializer = SubjectSerializer(subjects, many=True)
	return Response(serializer.data)