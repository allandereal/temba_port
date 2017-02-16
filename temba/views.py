from django.shortcuts import render
from temba.models import ContactGroup

# Create your views here.


def index(request):
    all_groups = ContactGroup.objects.all()
    groups = []
    for this_group in all_groups:
        groups.append((this_group.group_name, this_group.number_of_contacts))
    context = {'all_groups_list': groups}
    return render(request, 'temba/index.html', context)
