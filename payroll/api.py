from rest_framework import viewsets
from rest_framework.response import Response

from payroll.models import Unit, Department, Person
from payroll import serializers


class IndexViewSet(viewsets.ViewSet):
    serializer_class = serializers.IndexSerializer

    def list(self, request):
        '''
        TODO: Should this be retrieve? Want to keep API consistent across Index
        and entity-related views.
        '''
        try:
            data_year = request.query_params['data_year']
        except KeyError:
            return Response({})
        else:
            serializer = serializers.IndexSerializer(instance=data_year)
            return Response(serializer.data)


class ReadOnlyModelViewSetWithDataYear(viewsets.ReadOnlyModelViewSet):

    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        try:
            data_year = request.query_params['data_year']
        except KeyError:
            return Response({})
        else:
            serializer = self.serializer_class(instance=self.get_object(),
                                               context={'data_year': data_year})
            return Response(serializer.data)


class UnitViewSet(ReadOnlyModelViewSetWithDataYear):
    serializer_class = serializers.UnitSerializer
    queryset = Unit.objects.all()


class DepartmentViewSet(ReadOnlyModelViewSetWithDataYear):
    serializer_class = serializers.DepartmentSerializer
    queryset = Department.objects.all()

class PersonViewSet(ReadOnlyModelViewSetWithDataYear):
    serializer_class = serializers.PersonSerializer
    queryset = Person.objects.all()
