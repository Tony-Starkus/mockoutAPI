from rest_framework import serializers


class MockoutAPISerializer(serializers.Serializer):
    total_data = serializers.IntegerField()
    fields = serializers.ListField()
