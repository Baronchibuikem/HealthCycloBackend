from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status
from data.Api_v1.serializers.requestdata_serializers import RequestDataSerializer
from data.models import RequestData

# Initialize the APIClient app
client = Client()


class RequestDataTest(TestCase):
    """ Test case for requestData"""

    def setUp(self):
        RequestData.objects.create(
            prefix="Mr",
            first_name="John",
            last_name="Doe",
            designation='Principal Officer',
            affilation="World Health",
            address="Gimbiya",
            zip_code="12345",
            country="Nigeria",
            email="test@gmail.com",
            phone_number="07037541482",
            purpose="analysis",
            description="test case 1"
        )

    def test_can_get_all_requested_data(self):
        """ used to test the api endpoint to get all requested data """
        response = client.get(reverse("data:requestdata-list"))
        # get data from db
        requested_data = RequestData.objects.all()
        serializer = RequestDataSerializer(requested_data, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRequestDataTest(TestCase):
    def setUp(self):
        self.data = RequestData.objects.create(
            prefix="Mr",
            first_name="John",
            last_name="Doe",
            designation='Principal Officer',
            affilation="World Health",
            address="Gimbiya",
            zip_code="12345",
            country="Nigeria",
            email="test@gmail.com",
            phone_number="07037541482",
            purpose="analysis",
            description="test case 1"
        )

    def test_get_valid_single_request_data(self):
        response = client.get(
            reverse("data:requestdata-detail", kwargs={'pk': self.data.pk}))
        requested_data = RequestData.objects.get(pk=self.data.pk)
        serializer = RequestDataSerializer(requested_data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Claim(self):
        response = client.get(
            reverse("data:requestdata-detail", kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def CreateNewRequestDataTest(TestCase):
    """ Test case for inserting a new request data instance """

    def setUp(self):
        self.valid_payload = {
            prefix: "Mr",
            first_name: "John",
            last_name: "Doe",
            designation: 'Principal Officer',
            affilation: "World Health",
            address: "Gimbiya",
            zip_code: "12345",
            country: "Nigeria",
            email: "test@gmail.com",
            phone_number: "07037541482",
            purpose: "analysis",
            description: "test case 1"
        }
        self.invalid_payload: {
            prefix: "Mr",
            first_name: "",
            last_name: "",
            designation: 'Principal Officer',
            affilation: "World Health",
            address: "Gimbiya",
            zip_code: "12345",
            country: "Nigeria",
            email: "test@gmail.com",
            phone_number: "07037541482",
            purpose: "analysis",
            description: "test case 1"
        }

    def test_create_valid_Claim(self):
        response = client.post(
            reverse('data:requestdata-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_Claim(self):
        response = client.post(
            reverse('data:requestdata-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class updateSingleRequestDataTest(TestCase):
    """Test module for updating an existing request data instance"""

    def setUp(self):
        self.new_request = RequestData.objects.create(
            prefix="Mr",
            first_name="John",
            last_name="Doe",
            designation='Principal Officer',
            affilation="World Health",
            address="Gimbiya",
            zip_code="12345",
            country="Nigeria",
            email="test@gmail.com",
            phone_number="07037541482",
            purpose="analysis",
            description="test case 1"
        )

        self.valid_payload = {
            "prefix": "Mr",
            "first_name": "John",
            "last_name": "Doe",
            "designation": 'Principal Officer',
            "affilation": "World Health",
            "address": "Gimbiya",
            "zip_code": "12345",
            "country": "Nigeria",
            "email": "test@gmail.com",
            "phone_number": "07037541482",
            "purpose": "analysis",
            "description": "test case 1"
        }
        self.invalid_payload = {
            "prefix": "Mr",
            "first_name": "",
            "last_name": "",
            "designation": 'Principal Officer',
            "affilation": "World Health",
            "address": "Gimbiya",
            "zip_code": "12345",
            "country": "Nigeria",
            "email": "test@gmail.com",
            "phone_number": "07037541482",
            "purpose": "analysis",
            "description": "test case 1"
        }

    def test_valid_update_claim(self):
        response = client.put(
            reverse('data:requestdata-detail',
                    kwargs={'pk': self.new_request.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_claim(self):
        response = client.put(
            reverse('data:requestdata-detail',
                    kwargs={'pk': self.new_request.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRequestDataTest(TestCase):
    """ Test module for deleting an existing Request data instance"""

    def setUp(self):
        self.new_request = RequestData.objects.create(
            prefix="Mr",
            first_name="John",
            last_name="Doe",
            designation='Principal Officer',
            affilation="World Health",
            address="Gimbiya",
            zip_code="12345",
            country="Nigeria",
            email="test@gmail.com",
            phone_number="07037541482",
            purpose="analysis",
            description="test case 1"
        )

    def test_valid_delete_claim(self):
        response = client.delete(
            reverse('data:requestdata-detail', kwargs={'pk': self.new_request.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_claim(self):
        response = client.delete(
            reverse('data:requestdata-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
