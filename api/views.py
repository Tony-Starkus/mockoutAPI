from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MockoutAPISerializer
from .factory import *


class MockoutAPI(APIView):
    serializer_class = MockoutAPISerializer

    def get(self, request):
        response = None
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.data['total_data'] == 0:
                Response(status=200)
            elif serializer.data['total_data'] == 1:
                Response(status=200)
            else:
                response = []
                for i in range(serializer.data['total_data']):
                    data = {}
                    for field in serializer.data['fields']:
                        if field['type'] == 'string':
                            data.update({field['field_name']: build_string("", "")})

                        print(field)
                        response.append(data)
                return Response(data={"data": response}, status=200)

        return Response(data={"teste": "ok"}, status=200)
