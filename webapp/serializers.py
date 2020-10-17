from rest_framework import serializers
from webapp.models import Inscription


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = "__all__"
        #fields = ['id', 'id_curso', 'id_usuario', 'max_activity']