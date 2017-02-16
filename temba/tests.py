from django.test import TestCase
from .models import ContactGroup
from django.core.urlresolvers import reverse

# Create your tests here.


class ContactGroupTest(TestCase):

    def create_contactgroup(self, group_name="group_name test", number_of_contacts=1):
        return ContactGroup.objects.create(group_name=group_name, number_of_contacts=number_of_contacts)

    def test_contactgroup_creation(self):
        g = self.create_contactgroup()
        self.assertTrue(isinstance(g, ContactGroup))
        self.assertEqual(g.__str__(), g.group_name)

    def test_contactgroups_were_saved_from_server(self):
        g = ContactGroup.save_groups('http://localhost:8000', '86728a20dd1d74aa02e7298b9b3e0c1478fb7b7d')
        self.assertIs(g, True)

    def test_contactgroup_index_view(self):
        g = self.create_contactgroup()
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(g.group_name, response.content)

