from rest_framework import serializers
from .models import Vendor, Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'vendor', 'amount', 'date', 'description')