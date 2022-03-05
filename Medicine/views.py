from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from Medicine.forms import CreateOrEditMedicine, CreateOrEditMedicinePlan , CreateOrEditMedicinePlanItem , CreateOrEditMedicineCategory
from Medicine.models import MedicinePlan, MedicinePlanItems, Medicine , MedicineCategory

# Create your views here.


class AddMedicine(LoginRequiredMixin, CreateView):
    form_class = CreateOrEditMedicine
    model = Medicine
    success_url = '/manage_medicine/AddMedicine/'
    template_name = 'Medicine/CreateNewMedicine.html'


class MedicineList(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = 'Medicine/MedicineList.html'
    context_object_name = 'AllFood'


class EditMedicine(LoginRequiredMixin, UpdateView):
    model = Medicine
    success_url = '/manage_medicine/'
    template_name = 'Medicine/EditMedicine.html'
    form_class = CreateOrEditMedicine


class DeleteMedicine(LoginRequiredMixin, DeleteView):
    model = Medicine
    success_url = '/manage_medicine/'
    template_name = 'Medicine/DeleteMedicine.html'


class AddMedicinePlan(LoginRequiredMixin, CreateView):
    model = MedicinePlan
    success_url = '/manage_food/AddFoodPlan/'
    template_name = 'Plans/FoodPlans/AddFoodPlan.html'
    form_class = CreateOrEditMedicinePlan


class MedicinePlanList(LoginRequiredMixin, ListView):
    model = MedicinePlan
    template_name = 'Plans/FoodPlans/FoodPlanList.html'
    context_object_name = 'AllFoodPlan'


class DeleteMedicinePlan(LoginRequiredMixin, DeleteView):
    model = MedicinePlan
    template_name = 'Plans/FoodPlans/DeleteFoodPlan.html'
    success_url = '/manage_food/FoodPlanList'


class EditMedicinePlan(LoginRequiredMixin, UpdateView):
    model = MedicinePlan
    template_name = 'Plans/FoodPlans/EditFoodPlan.html'
    success_url = '/manage_food/FoodPlanList'
    form_class = CreateOrEditMedicinePlan


class CreateMedicinePlanItems(LoginRequiredMixin , CreateView):
    model = MedicinePlanItems
    template_name = 'Plans/FoodPlans/FoodPlanItems/CreateFoodPlanItem.html'
    form_class = CreateOrEditMedicinePlanItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg)
        context['items'] = MedicinePlanItems.objects.filter(medicine_plan__athlete__id = id).order_by('medicine_category')
        return context


    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("CreateFoodPlanItems", kwargs={'pk': id})


class EditMedicinePlanItems(LoginRequiredMixin , UpdateView):
    model = MedicinePlanItems
    template_name = 'Plans/FoodPlans/FoodPlanItems/EditFoodPlanItem.html'
    form_class = CreateOrEditMedicinePlanItem
    pk_url_kwarg = 'pk'
    id_url_kwarg = 'id'

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.id_url_kwarg)
        return reverse("CreateMedicinePlanItems", kwargs={'pk': id})


class CreateMedicineCategory(LoginRequiredMixin , CreateView):
    model = MedicineCategory
    template_name = 'Medicine/MedicineCategory/CreateMedicineCategory.html'
    form_class = CreateOrEditMedicineCategory
    success_url = '/manage_medicine/CreateMedicineCategory/'



class EditExerciseCategory(LoginRequiredMixin , UpdateView):
    model = MedicineCategory
    template_name = 'Exercise/ExerciseCategory/EditMedicineCategory.html'
    form_class = CreateOrEditMedicineCategory
    success_url = '/manage_medicine/'