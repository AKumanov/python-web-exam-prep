from django.shortcuts import render, redirect
from .models import Expense
from .common import get_profile, calculate_budget_left
from .forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm, \
    EditProfileForm, DeleteProfileForm


def home_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    if not profile:
        return redirect('create-profile')
    budget_left = calculate_budget_left(profile, expenses)
    print('BUDGET LEFT --> ', budget_left)
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def home_no_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-with-profile')

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def create_expense(request):
    form = CreateExpenseForm()

    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-with-profile')

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home-with-profile')
    form = EditExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        expense.delete()
        return redirect('home-with-profile')

    form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = calculate_budget_left(profile, expenses)
    number_of_items = expenses.count()
    context = {
        'profile': profile,
        'budget_left': budget_left,
        'number_of_items': number_of_items,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            profile.delete()
            Expense.objects.all().delete()
            return redirect('home-with-profile')
    form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
