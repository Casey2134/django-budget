from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from budget.categories.models import Category
from budget.categories.forms import CategoryForm


def category_list(request, model_class=Category, template_name='budget/categories/list.html'):
    """
    A list of category objects.

    Templates: ``budget/categories/list.html``
    Context:
        categories
            paginated list of category objects
        paginator
            A Django Paginator instance
        page
            current page of category objects
    """
    categories_list = model_class.active.all()
    try:
        paginator = Paginator(categories_list, getattr(settings, 'BUDGET_LIST_PER_PAGE', 50))
        page = paginator.page(request.GET.get('page', 1))
        categories = page.object_list
    except InvalidPage:
        raise Http404('Invalid page requested.')
    return render(request, template_name, {
        'categories': categories,
        'paginator': paginator,
        'page': page,
    })


def category_add(request, form_class=CategoryForm, template_name='budget/categories/add.html'):
    """
    Create a new category object.

    Templates: ``budget/categories/add.html``
    Context:
        form
            a category form
    """
    if request.POST:
        form = form_class(request.POST)

        if form.is_valid():
            category = form.save()
            return HttpResponseRedirect(reverse('budget_category_list'))
    else:
        form = form_class()
    return render(request, template_name, {
        'form': form,
    })


def category_edit(request, slug, model_class=Category, form_class=CategoryForm, template_name='budget/categories/edit.html'):
    """
    Edit a category object.

    Templates: ``budget/categories/edit.html``
    Context:
        category
            the existing category object
        form
            a category form
    """
    category = get_object_or_404(model_class.active.all(), slug=slug)
    if request.POST:
        form = form_class(request.POST, instance=category)

        if form.is_valid():
            category = form.save()
            return HttpResponseRedirect(reverse('budget_category_list'))
    else:
        form = form_class(instance=category)
    return render(request, template_name, {
        'category': category,
        'form': form,
    })


def category_delete(request, slug, model_class=Category, template_name='budget/categories/delete.html'):
    """
    Delete a category object.

    Templates: ``budget/categories/delete.html``
    Context:
        category
            the existing category object
    """
    category = get_object_or_404(model_class.active.all(), slug=slug)
    if request.POST:
        if request.POST.get('confirmed') == 'Yes':
            category.delete()
        return HttpResponseRedirect(reverse('budget_category_list'))
    return render(request, template_name, {
        'category': category,
    })