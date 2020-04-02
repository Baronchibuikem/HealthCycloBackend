from rest_framework import serializers
from accounts.models import ContactUs, Subscribe


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("email", "subject", "content",)
        # read_only_fields = ("sent_date",)


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"