from rest_framework.views import APIView
from rest_framework.response import Response

"""List of HTTP status code"""
from rest_framework import status

from profiles_api import serializer

from rest_framework import viewsets


class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializer.HelloSerializer

	def get(self, request, format=None):
		"""Return a list of APIView features"""
		an_apiview = [
			'Use HTTP methods as function (get, post, patch, put, delete',
			'Is similar to a traditional Django View',
			'Gives you the most control over you application logic',
			'Is mapped manually to URLs',
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})

	def post(self, request):
		"""Create a message with our name"""
		serializer = self.serializer_class(data=request.data)

		# Validate the serializer
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			# f'' insert variable into string
			message = f'Hello {name}'
			return Response({'message': message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	def put(self, request, pk=None):
		# pk is ID of object to update by put request
		"""Handle updating an object"""
		return Response({'method': 'PUT'})

	def patch(self, request, pk=None):
		"""Handle partial update of an object"""
		return Response({'method': 'PATCH'})

	def delete(self, request, pk=None):
		"""Delete an object"""
		return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""
	serializer_class = serializer.HelloSerializer

	def list(self, request):
		"""Return a hello message"""
		a_viewset = [
			'Uses action (list, create, retrieve, update, partial_update',
			'Teomoney',
			'I want to make a website',
		]
		return Response({'message': 'Hello', 'a_viewset': a_viewset})

	def create(self, request):
		"""Create a new hello massage"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

	def retrieve(self, request, pk=None):
		"""Handling getting an object by its ID"""
		return Response({'http_method': 'GET'})

	def update(self, request, pk=None):
		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		return Response({'http_method': 'DELETE'})