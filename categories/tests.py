from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_name(self):
        self.assertEqual(str(self.category), 'Test Category')

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=100,
            category=self.category,
            available=True
        )

    def test_product_name(self):
        self.assertEqual(str(self.product), 'Test Product - Test Category')

    def test_product_description(self):
        self.assertEqual(self.product.description, 'This is a test product')

    def test_product_price(self):
        self.assertEqual(self.product.price, 100)

    def test_product_availability(self):
        self.assertTrue(self.product.available)

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)
