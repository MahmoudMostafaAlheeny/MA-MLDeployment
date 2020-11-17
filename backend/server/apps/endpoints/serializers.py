from rest_framework import serializers
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgo
from apps.endpoints.models import MLAlogStatus
from apps.endpoints.models import MLRequest

class EndpointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endpoint
		read_only_fields = ("id","name","owner","created_at")
		fields = read_only_fields

class MLAlgoSerializer(serializers.ModelSerializer):
	current_status = serializers.SerializerMethodField(read_only=True)

	def get_current_status(self,mlalgo):
		return MLAlgoStatus.objects.filter(parent_mlalgo=mlalgo)
	class Meta:
		model = MLAlgo
		read_only_fields = ("id","name","description","code",
			"verison","owner","created_at","parent_endpoint","current_status")
		fields = read_only_fields
class MLAlgoStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = MLAlogStatus
		read_only_fields = ("id","active")
		fields = ("id","active","status","created_by","created_at","parent_mlalgo")
class MLRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = MLAlgo
		read_only_fields = ("id","input_data","full_response","response",
			"created_at","parent_mlalgo")

		fields = ("id","input_data","full_response","feedback","response",
			"created_at","parent_mlalgo")



