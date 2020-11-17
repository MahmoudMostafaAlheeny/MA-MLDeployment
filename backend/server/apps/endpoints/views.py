from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgo 
from apps.endpoints.serializers import MLAlgoSerializer

from apps.endpoints.models import MLAlogStatus
from apps.endpoints.serializers import MLAlgoStatusSerializer

from apps.endpoints.models import MLRequest 
from apps.endpoints.serializers import MLRequestSerializer
# Create your views here.

class EndpointViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = EndpointSerializer
	queryset = Endpoint.objects.all()

class MLAlgoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = MLAlgoSerializer
	queryset = MLAlgo.objects.all()

def deactivate_other_statuses(instance):
	old_statuses = MLAlgoStatus.objects.filter(parent_mlalgo = instance.parent_mlalgo,
                                                  created_at__lt= instance.created_at,
                                                        active=True)
	for i in range(len(old_statuses)):
		old_statuses[i].active = False
	MLAlgoStatus.objects.bulk_update(old_statuses,["active"])

class MLAlgoStatusSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, 
	viewsets.GenericViewSet, mixins.CreateModelMixin):

	serializer_class = MLAlgoStatusSerializer
	queryset = MLAlogStatus.objects.all()

	def perform_create(self,serializer):
		try:
			with transaction.atomic():
				instance = serializer.save(active=True)
				deactivate_other_statuses(instance)
		except Exception as e:
			raise APIException(str(e))

class MLRequestViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
	viewsets.GenericViewSet,mixins.UpdateModelMixin):
	
	serializer_class = MLRequestSerializer
	queryset = MLRequest.objects.all()


