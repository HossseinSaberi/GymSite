from django.contrib import messages
from urllib import response
from django.shortcuts import render  , redirect 
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , login , logout
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
from io import BytesIO, StringIO

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
        context["all_day"] = ['شنبه' , 'یکشنبه' , 'دوشنبه' , 'سه شنبه' , 'چهارشنبه' , 'پنج شنبه' , 'جمعه']
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



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.athlete_id is not None:
            context["address"] = 'DeleteConfirmAthlete'

        elif self.domain_id is not None:
            context["address"] = 'DeleteConfirmDomain'

        elif self.food_id is not None:
            context["address"] = 'DeleteConfirmFood'

        elif self.exercise_category_id is not None:
            context["address"] = 'DeleteConfirmExerciseCat'

        elif self.exercise_id is not None:
            context["address"] = 'DeleteConfirmExercise'

        elif self.exercise_plan_id is not None:
            context["address"] = 'DeleteConfirmExercisePlan'
            
        elif self.food_category_id is not None:
            context["address"] = 'DeleteConfirmFoodCat'
   
        elif self.medicine_category_id is not None:
            context["address"] = 'DeleteConfirmMedicineCat'

        elif self.medicine_plan_item_id is not None:
            context["address"] = 'DeleteConfirmMedicinePlanItem'

        elif self.medicine_plan_id is not None:
            context["address"] = 'DeleteConfirmMedicinePlan'

        elif self.medicine_id is not None:
            context["address"] = 'DeleteConfirmMedicine'

        elif self.exercise_plan_item_id is not None:
            context["address"] = 'DeleteConfirmExercisePlanItem'

        elif self.food_plan_id is not None:
            context["address"] = 'DeleteConfirmFoodPlan'

        elif self.food_plan_item_id is not None:
            context["address"] = 'DeleteConfirmFoodPlanItem'

        return context
        
    def get_object(self, queryset=None):
        self.athlete_id = self.kwargs.get(self.athlete_id_kwargs)
        self.domain_id = self.kwargs.get(self.domain_id_kwargs)
        self.exercise_category_id = self.kwargs.get(self.exercise_category_id_kwargs)
        self.exercise_id = self.kwargs.get(self.exercise_id_kwargs)
        self.exercise_plan_id = self.kwargs.get(self.exercise_plan_id_kwargs)
        self.exercise_plan_item_id = self.kwargs.get(self.exercise_plan_item_id_kwargs)
        self.food_id = self.kwargs.get(self.food_id_kwargs)
        self.food_category_id = self.kwargs.get(self.food_category_id_kwargs)
        self.food_plan_id = self.kwargs.get(self.food_plan_id_kwargs)
        self.food_plan_item_id = self.kwargs.get(self.food_plan_item_id_kwargs)
        self.medicine_plan_item_id = self.kwargs.get(self.medicine_plan_item_id_kwargs)
        self.medicine_plan_id = self.kwargs.get(self.medicine_plan_id_kwargs)
        self.medicine_id = self.kwargs.get(self.medicine_id_kwargs)
        self.medicine_category_id = self.kwargs.get(self.medicine_category_id_kwargs)


        if self.athlete_id is not None:
            queryset = Athlete.objects.filter(pk = self.athlete_id)
            self.success_url = '/manage_athlete/'
            
            
        elif self.domain_id is not None:
            queryset = Domain.objects.filter(pk = self.domain_id)
            self.success_url = '/manage_exercise/'

        elif self.food_id is not None:
            queryset = Foods.objects.filter(pk = self.food_id)
            self.success_url = '/manage_food/'

        elif self.exercise_category_id is not None:
            queryset = ExerciseCategory.objects.filter(pk = self.exercise_category_id)
            self.success_url = '/manage_exercise/'

        elif self.exercise_id is not None:
            queryset = Exercise.objects.filter(pk = self.exercise_id)
            self.success_url = '/manage_exercise/'

        elif self.exercise_plan_id is not None:
            queryset = ExercisePlan.objects.filter(pk = self.exercise_plan_id)
            self.success_url = '/manage_exercise/ExercisePlan/'
            
        elif self.food_category_id is not None:
            queryset = FoodCategory.objects.filter(pk = self.food_category_id)
            self.success_url = '/manage_food/'
            
        elif self.medicine_category_id is not None:
            queryset = MedicineCategory.objects.filter(pk = self.medicine_category_id)
            self.success_url = '/manage_medicine/'

        elif self.medicine_plan_item_id is not None:
            queryset = MedicinePlanItems.objects.filter(pk = self.medicine_plan_item_id)
            id = queryset.last().medicine_plan.athlete.id
            self.success_url = reverse("CreateMedicinePlanItems", kwargs={'pk': id})

        elif self.medicine_plan_id is not None:
            queryset = MedicinePlan.objects.filter(pk = self.medicine_plan_id)
            self.success_url = '/manage_medicine/MedicinePlanList/'

        elif self.medicine_id is not None:
            queryset = Medicine.objects.filter(pk = self.medicine_id)
            self.success_url = '/manage_medicine/'

        elif self.exercise_plan_item_id is not None:
            queryset = ExercisePlanItems.objects.filter(pk = self.exercise_plan_item_id)
            id = queryset.last().exercise_plan.athlete.id
            self.success_url = reverse("CreateExercisePlanItems", kwargs={'pk': id})
            """get plan id and get back to that id"""

        elif self.food_plan_id is not None:
            queryset = FoodPlan.objects.filter(pk = self.food_plan_id)
            self.success_url = '/manage_food/FoodPlanList/'

        elif self.food_plan_item_id is not None:
            queryset = FoodPlanItems.objects.filter(pk = self.food_plan_item_id)
            id = queryset.last().food_plan.athlete.id
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
    days = ['شنبه' , 'یکشنبه' , 'دوشنبه' , 'سه شنبه' , 'چهارشنبه' , 'پنج شنبه' , 'جمعه']
    context = {"exercise_plan_items" : exercise_plan_item , "all_day" : days , "user" : user}


    html = template.render(context)
    pisa.pisaDocument(html.encode("UTF-8")  , dest=response)

    return response


def ExportF_Pdf(request , pk):
    user = Athlete.objects.get(id = pk)
    response = HttpResponse(content_type = "application/pdf")
    response["content-Disposition"]=\
        'attachment;filename='+user.username+'_FoodPlan.pdf'

    template_path="Pdf/FoodPdf.html"
    template = get_template(template_path)

    food_plan_item = FoodPlanItems.objects.filter(food_plan__athlete = pk)
    days = ['شنبه' , 'یکشنبه' , 'دوشنبه' , 'سه شنبه' , 'چهارشنبه' , 'پنج شنبه' , 'جمعه']
    context_dict = {"food_plan_item" : food_plan_item , "all_day" : days , "user" : user}
    # context = Context(context_dict)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def ExportM_Pdf(request , pk):
    user = Athlete.objects.get(id = pk)
    response = HttpResponse(content_type = "application/pdf")
    response["content-Disposition"]=\
        'attachment;filename='+user.username+'_MedicinePlan.pdf'

    template_path="Pdf/MedicinePdf.html"
    template = get_template(template_path)

    medicine_plan_item = MedicinePlanItems.objects.filter(medicine_plan__athlete = pk)
    days = ['شنبه' , 'یکشنبه' , 'دوشنبه' , 'سه شنبه' , 'چهارشنبه' , 'پنج شنبه' , 'جمعه']
    context = {"medicine_plan_item" : medicine_plan_item , "all_day" : days , "user" : user}

    html = template.render(context)
    pisa.pisaDocument(html , dest=response)

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