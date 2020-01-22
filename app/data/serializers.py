from rest_framework import serializers
from core.models import Family, Expense, People  # importing model


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['index', 'index_exp', 'folio',  'ingreso',
                  'fe', 'np', 'gasto',  'ingreso_disp', 'ptge_gasto']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        field = ['g', 'c1', 'c2', 'c3', 'c4',
                 'c5', 'c6', 'c7', 'c8', 'c9',
                 'c10', 'c11', 'c12', 'ahorro_deuda', 'ingreso']


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        field = ['folio', 'inga_hd', 'fe', 'persona',
                 'npersonas', 'edad', 'ingreso_hd', 'ingreso_pc']
