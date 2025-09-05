from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from jewerly_app.models.products_materials import Product


class TestsProduct(APITestCase):
    def setUp(self):
        self.active_product = Product.objects.create(
            name='Обручка з діамантом',
            article_code='ZOR-159-2434',
            photo_url='https://cdn.mpanov.com/diamond-ring.webp',
            is_archived=False
        )
        self.archived_product = Product.objects.create(
            name='Сережки "Світанок',
            article_code='ZOR-229-1414',
            photo_url='https://cdn.mpanov.com/diamond-ring.webp',
            is_archived=True
        )

        self.list_url = reverse('product-list')
        self.detail_url = reverse('product-detail', kwargs={'pk': self.active_product.pk})

    def test_get_product_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 2)

    def test_filter_archived_products(self):
        response = self.client.get(self.list_url, {'isArchived': 'True'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], self.archived_product.name)

    def test_create_product(self):
        new_product_data = {
            'name': 'Браслет',
            'article': 'ZOR-155-5555',
            'pictureUrl': 'https://cdn.mpanov.com/diamond-ring.webp'
        }
        response = self.client.post(self.list_url, new_product_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(response.data['name'], new_product_data['name'])
        self.assertEqual(response.data['article'], new_product_data['article'])
        self.assertEqual(response.json()['pictureUrl'], new_product_data['pictureUrl'])

    def test_create_product_without_photo(self):
        new_product_data = {
            'name': 'Кольє',
            'article': 'ZOR-155-6666'
        }
        response = self.client.post(self.list_url, new_product_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(response.data['name'], new_product_data['name'])
        self.assertEqual(response.data['article'], new_product_data['article'])
        self.assertIsNone(response.data.get('pictureUrl'))

    def test_get_product_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.active_product.name)

    def test_get_nonexistent_product_detail(self):
        response = self.client.get(reverse('product-detail', kwargs={'pk': 1414}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product(self):
        updated_data = {
            'name': 'Обручка з діамантом (оновлено)',
            'article': 'ZOR-159-2444',
            'pictureUrl': 'https://cdn.mpanov.com/diamond-ring.webp',
            'isArchived': True
        }
        response = self.client.put(self.detail_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.active_product.refresh_from_db()

        self.assertEqual(self.active_product.name, updated_data['name'])
        self.assertEqual(self.active_product.article_code, updated_data['article'])
        self.assertEqual(self.active_product.photo_url, updated_data['pictureUrl'])
        self.assertTrue(self.active_product.is_archived)

    def test_partially_update_product(self):
        response = self.client.patch(self.detail_url, {'isArchived': True}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.active_product.refresh_from_db()
        self.assertTrue(self.active_product.is_archived)


class TestsProductInvalidData(APITestCase):
    def setUp(self):
        self.list_url = reverse('product-list')

    def test_create_product_without_name(self):
        data = {'article': '"ZOR-159-2222'}
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_create_product_without_article(self):
        data = {'name': 'Кулон'}
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('article', response.data)

    def test_create_product_with_empty_strings(self):
        data = {'name': '', 'article': ''}
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('article', response.data)
