from django.test import TestCase
from django.urls import reverse, reverse, resolve

class APIsURLsTest(TestCase):
    def test_api_product_list_url_is_correct(self):
        url = reverse('api:produto-list')
        self.assertEqual(url, '/produtos/')

    def test_api_product_create_url_is_correct(self):
        url = reverse('api:produto-create')
        self.assertEqual(url, '/produtos/create/')

    def test_api_product_update_url_is_correct(self):
        url = reverse('api:produto-update', kwargs={'pk': 1})
        self.assertEqual(url, '/produtos/update/1/')

    def test_api_product_delete_url_is_correct(self):
        url = reverse('api:produto-delete', kwargs={'pk': 1})
        self.assertEqual(url, '/produtos/delete/1/')

    def test_api_product_sell_url_is_correct(self):
        url = reverse('api:vender_produto', kwargs={'pk': 1, 'qtd': 1})
        self.assertEqual(url, '/produtos/1/vender/1/')


class APIViewTest(TestCase):

    def test_api_product_list_returns_status_code_200_OK(self):
        response = self.client.get(reverse('api:produto-list'))
        self.assertEqual(response.status_code, 200)

