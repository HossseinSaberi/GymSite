from django.shortcuts import render
from django.views import View
from .models import Domain, Exercise, ExerciseCategory, ExercisePlan, ExercisePlanItems
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateOrEditDomain, CreateOrEditExercise, CreateOrEditExercisePlan, CreateExercisePlanItem, CreateOrEditExerciseCategory , EditExercisePlanItem
from django.urls import reverse
from django_tables2 import SingleTableView
from .tables import ExerciseTable
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

class ExerciseList(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'Exercise/ExerciseList.html'
    context_object_name = 'AllExercise'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["AllDomain"] = Domain.objects.all()
        context["AllCategory"] = ExerciseCategory.objects.all()
        return context


# class ExerciseList(SingleTableView):
#     model = Exercise
#     template_name = 'Exercise/ExerciseList.html'
#     table_class = ExerciseTable
#     context_object_name = 'AllExercise'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["AllDomain"] = Domain.objects.all()
#         context["AllCategory"] = ExerciseCategory.objects.all()
#         return context


class CreateExercise(LoginRequiredMixin, CreateView):
    model = Exercise
    template_name = 'Exercise/CreateNewExercise.html'
    form_class = CreateOrEditExercise
    success_url = '/manage_exercise/'


class EditExercise(LoginRequiredMixin, UpdateView):
    model = Exercise
    template_name = 'Exercise/EditExercise.html'
    form_class = CreateOrEditExercise
    success_url = '/manage_exercise/'


class ExercisePlanList(LoginRequiredMixin, ListView):
    model = ExercisePlan
    template_name = 'Plans/ExercisePlans/ExercisePlanList.html'
    context_object_name = 'AllExercisePlan'


class CreateExercisePlan(LoginRequiredMixin, CreateView):
    model = ExercisePlan
    template_name = 'Plans/ExercisePlans/CreateExercisePlan.html'
    form_class = CreateOrEditExercisePlan
    success_url = '/manage_exercise/ExercisePlan/'


class EditExercisePlan(LoginRequiredMixin, UpdateView):
    model = ExercisePlan
    template_name = 'Plans/ExercisePlans/EditExercisePlan.html'
    form_class = CreateOrEditExercisePlan
    success_url = '/manage_exercise/ExercisePlan/'


class CreateExercisePlanItems(LoginRequiredMixin, CreateView):
    model = ExercisePlanItems
    template_name = 'Plans/ExercisePlans/ExercisePlanItems/CreateExercisePlanItem.html'
    form_class = CreateExercisePlanItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg)
        context['items'] = ExercisePlanItems.objects.filter(
            exercise_plan__athlete__id=id).order_by('exercise_category')
        return context

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.pk_url_kwarg)
        return reverse("CreateExercisePlanItems", kwargs={'pk': id})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['exerciseplan'] = self.kwargs.get(self.pk_url_kwarg)
        return kwargs


class EditExercisePlanItems(LoginRequiredMixin, UpdateView):
    model = ExercisePlanItems
    template_name = 'Plans/ExercisePlans/ExercisePlanItems/EditExercisePlanItem.html'
    form_class = EditExercisePlanItem
    pk_url_kwarg = 'pk'
    id_url_kwarg = 'id'

    def get_success_url(self, **kwargs):
        id = self.kwargs.get(self.id_url_kwarg)
        return reverse("CreateExercisePlanItems", kwargs={'pk': id})


class CreateDomain (LoginRequiredMixin, CreateView):
    model = Domain
    template_name = 'Exercise/Domain/CreateDomain.html'
    form_class = CreateOrEditDomain
    success_url = '/manage_exercise/'


class EditDomain(LoginRequiredMixin, UpdateView):
    model = Domain
    template_name = 'Exercise/Domain/EditDomain.html'
    form_class = CreateOrEditDomain
    success_url = '/manage_exercise/'


class CreateExerciseCategory(LoginRequiredMixin, CreateView):
    model = ExerciseCategory
    template_name = 'Exercise/ExerciseCategory/CreateExerciseCategory.html'
    form_class = CreateOrEditExerciseCategory
    success_url = '/manage_exercise/'


class EditExerciseCategory(LoginRequiredMixin, UpdateView):
    model = ExerciseCategory
    template_name = 'Exercise/ExerciseCategory/EditExerciseCategory.html'
    form_class = CreateOrEditExerciseCategory
    success_url = '/manage_exercise/'
