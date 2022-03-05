from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from Food.forms import CreateOrEditFood, CreateOrEditFoodPlan , CreateOrEditFoodPlanItem , CreateOrEditFoodCategory
from Food.models import FoodPlan, FoodPlanItems, Foods , FoodCategory

# Create your views here.


class AddFood(LoginRequiredMixin, CreateView):
    form_class = CreateOrEditFood
    model = Foods
    success_url = '/manage_food/AddFood/'
    template_name = 'Food/CreateNewFood.html'


class FoodsList(LoginRequiredMixin, ListView):
    model = Foods
    template_name = 'Food/FoodList.html'
    context_object_name = 'AllFood'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AllCategory"] = FoodCategory.objects.all()
        return context

class EditFood(LoginRequiredMixin, UpdateView):
    model = Foods
    success_url = '/manage_food/'
    template_name = 'Food/EditFood.html'
    form_class = CreateOrEditFood


class DeleteFood(LoginRequiredMixin, DeleteView):
    model = Foods
    success_url = '/manage_food/'
    template_name = 'Food/DeleteFood.html'


class AddFoodPlan(LoginRequiredMixin, CreateView):
    model = FoodPlan
    success_url = '/manage_food/AddFoodPlan/'
    template_name = 'Plans/FoodPlans/AddFoodPlan.html'
    form_class = CreateOrEditFoodPlan


class FoodPlanList(LoginRequiredMixin, ListView):
    model = FoodPlan
    template_name = 'Plans/FoodPlans/FoodPlanList.html'
    context_object_name = 'AllFoodPlan'


class DeleteFoodPlan(LoginRequiredMixin, DeleteView):
    model = FoodPlan
    template_name = 'Plans/FoodPlans/DeleteFoodPlan.html'
    success_url = '/manage_food/FoodPlanList'


class EditFoodPlan(LoginRequiredMixin, UpdateView):
    model = FoodPlan
    template_name = 'Plans/FoodPlans/EditFoodPlan.html'
    success_url = '/manage_food/FoodPlanList'
    form_class = CreateOrEditFoodPlan


class CreateFoodPlanItems(LoginRequiredMixin , CreateView):
    model = FoodPlanItems
    template_name = 'Plans/FoodPlans/FoodPlanItems/CreateFoodPlanItem.html'
    form_class = CreateOrEditFoodPlanItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg)
        context['items'] = FoodPlanItems.objects.filter(food_plan__athlete__id = id).order_by('food_category')
        return context


    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("CreateFoodPlanItems", kwargs={'pk': id})


class EditFoodPlanItems(LoginRequiredMixin , UpdateView):
    model = FoodPlanItems
    template_name = 'Plans/FoodPlans/FoodPlanItems/EditFoodPlanItem.html'
    form_class = CreateOrEditFoodPlanItem
    pk_url_kwarg = 'pk'
    id_url_kwarg = 'id'

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.id_url_kwarg)
        return reverse("CreateFoodPlanItems", kwargs={'pk': id})



class CreateFoodCategory(LoginRequiredMixin , CreateView):
    model = FoodCategory
    template_name = 'Food/FoodCategory/CreateFoodCategory.html'
    form_class = CreateOrEditFoodCategory
    success_url = '/manage_food/CreateFoodCategory/'



class EditFoodCategory(LoginRequiredMixin , UpdateView):
    model = FoodCategory
    template_name = 'Food/FoodCategory/EditFoodCategory.html'
    form_class = CreateOrEditFoodCategory
    success_url = '/manage_food/'