from rest_framework import serializers
from .models import Pizzeria


class PizzeriaSerializer(serializers.ModelSerializer):
    model = Pizzeria
    class Meta:
        fields=[
            "id",
            "pizzeria_name",
            "logo_image",
            "street",
            "zip_code"
        ]

        model =Pizzeria


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            "id",
            "pizzeria_name",
            "logo_image",
            "street",
            "zip_code",
            "email",
            "website",
            "state"
        ]

        model=Pizzeria


