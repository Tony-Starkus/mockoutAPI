from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MockoutAPISerializer
from .factory.string import build_string
from .factory.cpf import build_cpf
from .factory.integer import build_integer
from .factory.date import build_date


class MockoutAPI(APIView):
    serializer_class = MockoutAPISerializer

    def get(self, request):
        response = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.data['total_data'] == 0:
                Response(status=200)
            elif serializer.data['total_data'] == 1:
                Response(status=200)
            else:

                # Start interation using total data to return
                for i in range(serializer.data['total_data']):

                    # Object data
                    data = {}

                    # Start iteration over object fields
                    for field in serializer.data['fields']:
                        if field['type'] == 'string':
                            data.update({field['field_name']: build_string(field)})
                        elif field['type'] == 'int':
                            data.update({field['field_name']: build_integer(field)})
                        elif field['type'] == 'cpf':
                            data.update({field['field_name']: build_cpf(field)})
                        elif field['type'] == 'date':
                            data.update({field['field_name']: build_date(field)})

                    response.append(data)

                return Response(data={"data": response}, status=200)

        return Response(data={"teste": "ok"}, status=200)
