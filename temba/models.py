from django.db import models
from temba_client.v2 import TembaClient


# Create your models here.
class ContactGroup(models.Model):
    group_name = models.CharField(max_length=200)
    number_of_contacts = models.IntegerField(default=0)

    def __str__(self):
        return self.group_name

    @classmethod
    def save_groups(cls, domain_name, token_id):
        client = TembaClient(domain_name, token_id)
        for groups in client.get_groups().iterfetches(retry_on_rate_exceed=True):
            for this_group in groups:
                cls.objects.create(group_name=this_group.name, number_of_contacts=this_group.count)
        return True

contact_groups = ContactGroup.save_groups('http://localhost:8000', '86728a20dd1d74aa02e7298b9b3e0c1478fb7b7d')