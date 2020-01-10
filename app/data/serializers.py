from rest_framework import serializers

from core.models import Family # importing model


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['index', 'index_exp', 'folio',  'ingreso',
                  'fe', 'np', 'gasto',  'ingreso_disp', 'ptge_gasto']
