from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from Medicine.forms import CreateOrEditMedicine, CreateOrEditMedicinePlan, EditMedicinePlanItem, CreateOrEditMedicineCategory , CreateMedicinePlanItem
from Medicine.models import MedicinePlan, MedicinePlanItems, Medicine, MedicineCategory

# Create your views here.


class AddMedicine(LoginRequiredMixin, CreateView):
    form_class = CreateOrEditMedicine
    model = Medicine
    success_url = '/manage_medicine/'
    template_name = 'Medicine/CreateNewMedicine.html'


class MedicineList(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = 'Medicine/MedicineList.html'
    context_object_name = 'AllMedicine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AllCategory"] = MedicineCategory.objects.all()
        return context


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
    success_url = '/manage_medicine/MedicinePlanList/'
    template_name = 'Plans/MedicinePlans/AddMedicinePlan.html'
    form_class = CreateOrEditMedicinePlan


class MedicinePlanList(LoginRequiredMixin, ListView):
    model = MedicinePlan
    template_name = 'Plans/MedicinePlans/MedicinePlanList.html'
    context_object_name = 'AllMedicinePlan'


class EditMedicinePlan(LoginRequiredMixin, UpdateView):
    model = MedicinePlan
    template_name = 'Plans/MedicinePlans/EditMedicinePlan.html'
    success_url = '/manage_medicine/MedicinePlanList/'
    form_class = CreateOrEditMedicinePlan


class CreateMedicinePlanItems(LoginRequiredMixin, CreateView):
    model = MedicinePlanItems
    template_name = 'Plans/MedicinePlans/MedicinePlanItems/CreateMedicinePlanItems.html'
    form_class = CreateMedicinePlanItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg)
        context['items'] = MedicinePlanItems.objects.filter(
            medicine_plan__athlete__id=id).order_by('medicine_category')
        return context

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("CreateMedicinePlanItems", kwargs={'pk': id})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['medicineplan'] = self.kwargs.get(self.pk_url_kwarg)
        return kwargs


class EditMedicinePlanItems(LoginRequiredMixin, UpdateView):
    model = MedicinePlanItems
    template_name = 'Plans/MedicinePlans/MedicinePlanItems/EditMedicinePlanItems.html'
    form_class = EditMedicinePlanItem
    pk_url_kwarg = 'pk'
    id_url_kwarg = 'id'

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.id_url_kwarg)
        return reverse("CreateMedicinePlanItems", kwargs={'pk': id})


class CreateMedicineCategory(LoginRequiredMixin, CreateView):
    model = MedicineCategory
    template_name = 'Medicine/MedicineCategory/CreateMedicineCategory.html'
    form_class = CreateOrEditMedicineCategory
    success_url = '/manage_medicine/CreateMedicineCategory/'


class EditMedicineCategory(LoginRequiredMixin, UpdateView):
    model = MedicineCategory
    template_name = 'Medicine/MedicineCategory/EditMedicineCategory.html'
    form_class = CreateOrEditMedicineCategory
    success_url = '/manage_medicine/'
