from django.contrib import messages
from urllib import response
from django.shortcuts import render  , redirect
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth import authenticate , login , logout
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import CreateOrEditAthlete, LoginForm
from Users.models import Athlete
from Food.models import FoodCategory, FoodPlan, FoodPlanItems, Foods
from Medicine.models import Medicine, MedicineCategory, MedicinePlan, MedicinePlanItems
from Exercise.models import Domain, Exercise, ExerciseCategory, ExercisePlan, ExercisePlanItems
from django.http import Http404, HttpResponse
from django.utils.translation import gettext as _
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
class MainPage(LoginRequiredMixin , TemplateView):
    template_name = 'StartPage.html'

class AthleteList (LoginRequiredMixin, ListView):
    model = Athlete
    template_name = 'Athlete/AthleteList.html'
    context_object_name = 'AllAthlete'


class DeleteAthlete (LoginRequiredMixin, DeleteView):
    model = Athlete
    success_url = '/manage_athlete/'
    template_name = 'Athlete/DeleteAthlete.html'



class CreateAthlete(LoginRequiredMixin , CreateView):
    model = Athlete
    success_url = '/manage_athlete/'
    template_name = 'Athlete/CreateNewAthlete.html'
    form_class = CreateOrEditAthlete


class EditAthlete(LoginRequiredMixin, UpdateView):
    model = Athlete
    success_url = '/manage_athlete/'
    template_name = 'Athlete/EditAthlete.html'
    form_class = CreateOrEditAthlete


class AthleteDetails(LoginRequiredMixin, DetailView):

    model = Athlete
    context_object_name = 'AthleteContext'
    template_name = 'Athlete/AthleteDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get(self.pk_url_kwarg)
        context["food_plan"] = FoodPlanItems.objects.filter(
            food_plan__athlete_id=id)
        context["medicine_plan"] = MedicinePlanItems.objects.filter(
            medicine_plan__athlete_id=id)
        context["exercise_plan"] = ExercisePlanItems.objects.filter(
            exercise_plan__athlete_id=id)
        context["all_day"] = ['SATURDAY' , 'SUNDAY' , 'MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY']
        return context



class DeleteConfirm(LoginRequiredMixin , DeleteView):
    template_name = 'DeleteConfirm.html'
    athlete_id_kwargs = 'athleteid'
    domain_id_kwargs = 'domainid'
    exercise_category_id_kwargs = 'exercisecategoryid'
    exercise_id_kwargs = 'exerciseid'
    exercise_plan_id_kwargs = 'exerciseplanid'
    exercise_plan_item_id_kwargs = 'exerciseplanitemid'
    food_id_kwargs = 'foodid'
    food_plan_id_kwargs = 'foodplanid'
    food_plan_item_id_kwargs = 'foodplanitemid'
    food_category_id_kwargs = 'foodcategoryid'
    medicine_category_id_kwargs = 'medicinecategoryid'
    medicine_plan_item_id_kwargs = 'medicineplanitemid'
    medicine_plan_id_kwargs = 'medicineplanid'
    medicine_id_kwargs = 'medicineid'


    def get_object(self, queryset=None):
        athlete_id = self.kwargs.get(self.athlete_id_kwargs)
        domain_id = self.kwargs.get(self.domain_id_kwargs)
        exercise_category_id = self.kwargs.get(self.exercise_category_id_kwargs)
        exercise_id = self.kwargs.get(self.exercise_id_kwargs)
        exercise_plan_id = self.kwargs.get(self.exercise_plan_id_kwargs)
        exercise_plan_item_id = self.kwargs.get(self.exercise_plan_item_id_kwargs)
        food_id = self.kwargs.get(self.food_id_kwargs)
        food_category_id = self.kwargs.get(self.food_category_id_kwargs)
        food_plan_id = self.kwargs.get(self.food_plan_id_kwargs)
        food_plan_item_id = self.kwargs.get(self.food_plan_item_id_kwargs)
        medicine_plan_item_id = self.kwargs.get(self.medicine_plan_item_id_kwargs)
        medicine_plan_id = self.kwargs.get(self.medicine_plan_id_kwargs)
        medicine_id = self.kwargs.get(self.medicine_id_kwargs)
        medicine_category_id = self.kwargs.get(self.medicine_category_id_kwargs)


        if athlete_id is not None:
            queryset = Athlete.objects.filter(pk = athlete_id)
            self.success_url = '/manage_athlete/'
            
            
        elif domain_id is not None:
            queryset = Domain.objects.filter(pk = domain_id)
            self.success_url = '/manage_exercise/'

        elif food_id is not None:
            queryset = Foods.objects.filter(pk = food_id)
            self.success_url = '/manage_food/'

        elif exercise_category_id is not None:
            queryset = ExerciseCategory.objects.filter(pk = exercise_category_id)
            self.success_url = '/manage_exercise/'

        elif exercise_id is not None:
            queryset = Exercise.objects.filter(pk = exercise_id)
            self.success_url = '/manage_exercise/'

        elif exercise_plan_id is not None:
            queryset = ExercisePlan.objects.filter(pk = exercise_plan_id)
            self.success_url = '/manage_exercise/ExercisePlan/'
            
        elif food_category_id is not None:
            queryset = FoodCategory.objects.filter(pk = food_category_id)
            self.success_url = '/manage_food/'
            
        elif medicine_category_id is not None:
            queryset = MedicineCategory.objects.filter(pk = medicine_category_id)
            self.success_url = '/manage_medicine/'

        elif medicine_plan_item_id is not None:
            queryset = MedicinePlanItems.objects.filter(pk = medicine_plan_item_id)
            id = queryset.last().medicine_plan.id
            self.success_url = reverse("CreateMedicinePlanItems", kwargs={'pk': id})

        elif medicine_plan_id is not None:
            queryset = MedicinePlan.objects.filter(pk = medicine_plan_id)
            self.success_url = '/manage_medicine/MedicinePlanList/'

        elif medicine_id is not None:
            queryset = Medicine.objects.filter(pk = medicine_id)
            self.success_url = '/manage_medicine/'

        elif exercise_plan_item_id is not None:
            queryset = ExercisePlanItems.objects.filter(pk = exercise_plan_item_id)
            id = queryset.last().exercise_plan.id
            self.success_url = reverse("CreateExercisePlanItems", kwargs={'pk': id})
            """get plan id and get back to that id"""

        elif food_plan_id is not None:
            queryset = FoodPlan.objects.filter(pk = food_plan_id)
            self.success_url = '/manage_food/FoodPlanList/'

        elif food_plan_item_id is not None:
            queryset = FoodPlanItems.objects.filter(pk = food_plan_item_id)
            id = queryset.last().food_plan.id
            self.success_url = reverse("CreateFoodPlanItems", kwargs={'pk': id})
            """get plan id and get back to that id"""


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj



def ExportE_Pdf(request , pk):
    user = Athlete.objects.get(id = pk)
    response = HttpResponse(content_type = "application/pdf")
    response["content-Disposition"]=\
        'attachment;filename='+user.username+'_ExercisePlan.pdf'


    template_path="Pdf/ExercisePdf.html"
    template = get_template(template_path)

    exercise_plan_item = ExercisePlanItems.objects.filter(exercise_plan__athlete = pk)
    days = ['SATURDAY' , 'SUNDAY' , 'MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY']
    context = {"exercise_plan_items" : exercise_plan_item , "all_day" : days , "user" : user}


    html = template.render(context)
    pisa.CreatePDF(html  , dest=response)

    return response


def ExportF_Pdf(request , pk):
    user = Athlete.objects.get(id = pk)
    response = HttpResponse(content_type = "application/pdf")
    response["content-Disposition"]=\
        'attachment;filename='+user.username+'_FoodPlan.pdf'

    template_path="Pdf/FoodPdf.html"
    template = get_template(template_path)

    food_plan_item = FoodPlanItems.objects.filter(food_plan__athlete = pk)
    days = ['SATURDAY' , 'SUNDAY' , 'MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY']
    context = {"food_plan_item" : food_plan_item , "all_day" : days , "user" : user}

    html = template.render(context)
    pisa.CreatePDF(html , dest=response)

    return response


def ExportM_Pdf(request , pk):
    user = Athlete.objects.get(id = pk)
    response = HttpResponse(content_type = "application/pdf")
    response["content-Disposition"]=\
        'attachment;filename='+user.username+'_MedicinePlan.pdf'

    template_path="Pdf/MedicinePdf.html"
    template = get_template(template_path)

    medicine_plan_item = MedicinePlanItems.objects.filter(medicine_plan__athlete = pk)
    days = ['SATURDAY' , 'SUNDAY' , 'MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY']
    context = {"medicine_plan_item" : medicine_plan_item , "all_day" : days , "user" : user}

    html = template.render(context)
    pisa.CreatePDF(html , dest=response)

    return response


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username , password = password)
            if user:
                login(request , user)
                return redirect(reverse('MainPage'), {'request': request})
            else:
                messages.error(request , "the username or password is wrong" , extra_tags = 'danger')

    else:
        form = LoginForm()
    return render(request,'Login.html' , {'form' : form})


def Logout(request):
    logout(request)
    return redirect(reverse('Login'))