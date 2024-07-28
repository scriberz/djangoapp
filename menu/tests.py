from django.test import TestCase
from .models import Menu, MenuItem
from django.urls import reverse

class MenuTests(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(name="main_menu")
        self.menu_item = MenuItem.objects.create(menu=self.menu, name="Home", url="/")

    def test_menu_creation(self):
        self.assertEqual(self.menu.name, "main_menu")
        self.assertEqual(self.menu_item.name, "Home")

    def test_menu_item_url(self):
        self.assertEqual(self.menu_item.get_absolute_url(), "/")
