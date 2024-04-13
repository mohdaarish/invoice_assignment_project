from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import APIClient
from .models import Invoice, InvoiceDetails

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-04-13', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.detail_data = {'invoice': self.invoice.id, 'description': 'Test Description', 'quantity': 1, 'unit_price': 10.00, 'price': 10.00}
        self.detail = InvoiceDetails.objects.create(**self.detail_data)

    def test_create_invoice(self):
        url = reverse('invoice_list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual = (response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice(self):
        url = reverse('invoice_detail', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], self.invoice_data['customer_name'])