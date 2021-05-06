from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    """ Serializer converts data inputs to python objects and vice-versa"""
    name = serializers.CharField(max_length=10)
