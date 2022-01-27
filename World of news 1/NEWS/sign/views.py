from django.contrib.auth.models import User
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me1(request):
    user = request.user
    group = Group.objects.get(name='common')
    if not request.user.groups.filter(name='common').exists():
        group.user_set.add(user)
    return redirect('/')


def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')


def upgrade_me2(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        group.user_set.add(user)
    return redirect('/')



class MyView(PermissionRequiredMixin,CreateView):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

    class AddProduct(PermissionRequiredMixin, CreateView):
        permission_required = ('shop.add_product')