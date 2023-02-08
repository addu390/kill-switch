from rest_framework.views import APIView
from .models import Rule
from .serializers import RuleSerializer
from rest_framework.response import Response
from rest_framework import status
import rule_engine


class ValidateRules(APIView):
    def post(self, request):
        identifier = request.data.get("identifier")
        rule_objects = Rule.objects.filter(identifier=identifier)
        rule_serializer = RuleSerializer(rule_objects, many=True)
        data = request.data.get("data")

        for rule in rule_serializer.data:
            conditions = rule_engine.Rule(rule['conditions'])
            if conditions.matches(data):
                return Response({"matches": True}, status=status.HTTP_200_OK)
        return Response({"matches": False}, status=status.HTTP_200_OK)
