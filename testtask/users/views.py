from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

def home_page(request):
    return render(request, 'users/base.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user.html', {'users': users})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'users/group.html', {'groups': groups})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    groups = Group.objects.all()
    return render(request, 'users/add_user.html', {'form': form, 'groups': groups})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form})

def delete_user(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('user_list')

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'users/add_group.html', {'form': form})

def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'users/edit_group.html', {'form': form})

def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    users_in_group = User.objects.filter(group=group)
    if users_in_group.exists():
        messages.error(request, 'Cannot delete a group '+group.name+' with users assigned to it.')
    else:
        group.delete()

    return redirect('group_list')


