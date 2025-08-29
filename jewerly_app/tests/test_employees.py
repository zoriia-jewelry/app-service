from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from jewerly_app.models.employees import Employee


class EmployeeTests(APITestCase):
    def setUp(self):
        self.active_employee = Employee.objects.create(
            full_name='Недашківська Валерія Віталіївна',
            phone_number='+380933571694',
            is_archived=False
        )
        self.archived_employee = Employee.objects.create(
            full_name='Панов Максим Ігорович',
            phone_number='+380964269211',
            is_archived=True
        )

        self.list_url = reverse('employee-list')
        self.detail_url = reverse('employee-detail', kwargs={'pk': self.active_employee.pk})

    def test_get_employee_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 2)

    def test_filter_active_employees(self):
        response = self.client.get(self.list_url, {'is_archived': 'True'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['full_name'], self.archived_employee.full_name)

    def test_create_employee(self):
        new_employee = {
            'full_name': 'Коваленко Андрій Петрович',
            'phone_number': '+380631234567',
        }
        response = self.client.post(self.list_url, new_employee, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 3)
        self.assertEqual(response.data['full_name'], new_employee['full_name'])

    def test_get_employee_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], self.active_employee.full_name)

    def test_get_nonexistent_employee_detail(self):
        response = self.client.get(reverse('employee-detail', kwargs={'pk': 1414}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        updated_data = {
            'full_name': 'Недашківська Валерія Віталіївна (оновлено)',
            'phone_number': '+380501112233',
            'is_archived': True
        }
        response = self.client.put(self.detail_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.active_employee.refresh_from_db()

        self.assertEqual(self.active_employee.full_name, updated_data['full_name'])
        self.assertEqual(self.active_employee.phone_number, updated_data['phone_number'])
        self.assertTrue(self.active_employee.is_archived)

    def test_partially_update_employee(self):
        response = self.client.patch(self.detail_url, {'is_archived': True}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.active_employee.refresh_from_db()
        self.assertTrue(self.active_employee.is_archived)


class EmployeeInvalidDataTests(APITestCase):
    def setUp(self):
        self.list_url = reverse('employee-list')

    def test_create_employee_without_full_name(self):
        data = {
            'phone_number': '+380671112233'
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('full_name', response.data)

    def test_create_employee_without_phone_number(self):
        data = {
            'full_name': 'Мельник Олена Вікторівна'
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('phone_number', response.data)

    def test_create_employee_with_empty_strings(self):
        data = {
            'full_name': '',
            'phone_number': ''
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('full_name', response.data)
        self.assertIn('phone_number', response.data)
