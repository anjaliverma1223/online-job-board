from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import *
from .models import *
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.generic import ListView


def Home(request):
    qs = JobListing.objects.all().order_by('-published_on')  # Ensures queryset is ordered
    jobs = JobListing.objects.all().count()  # Total number of job listings
    user_count = User.objects.all().count()  # Total number of users
    company_name = JobListing.objects.filter(company_name__startswith='P').count()  # Count companies starting with 'P'

    paginator = Paginator(qs, 5)  # Show 5 jobs per page
    page = request.GET.get('page')

    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,  # The paginated queryset
        'job_qs': jobs,  # Total job count
        'company_name': company_name,  # Companies starting with 'P'
        'candidates': user_count  # Total user count
    }

    return render(request, "Home.html", context)

def about_us(request):
    return render(request, "jobs/about_us.html", {})


def service(request):
    return render(request, "jobs/services.html", {})
def service_single(request):
    return render(request, "jobs/service_single.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "jobs/contact.html", context)


@login_required
def job_listing(request):
    query = JobListing.objects.all().count()

    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query

    }
    return render(request, "jobs/job_listing.html", context)


@login_required
def job_post(request):
    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/jobs/job_listing/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_post.html", context)


def job_single(request, id):
    job_query = get_object_or_404(JobListing, id=id)

    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_single.html", context)


@login_required
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form,

    }
    return render(request, "jobs/job_apply.html", context)


class SearchView(ListView):
    model = JobListing
    template_name = 'jobs/search.html'
    context_object_name = 'job'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])
# from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, get_user_model, login, logout
# # from .forms import EmployeeRegistrationForm, EmployeeLoginForm


# def index(request):
#     return render(request,'index.html',{})

# def about(request):
#     return render(request,'about.html',{})

# def job_listings(request):
#     return render(request,'job_listings.html',{})
# def job_single(request):
#     return render(request,'job_single.html',{})
# def post_job(request):
#     return render(request,'post_job.html',{})
# def services(request):
#     return render(request,'services.html',{})
# def service_single(request):
#     return render(request,'service_single.html',{})
# def blog_single(request):
#     return render(request,'blog_single.html',{})
# def portfolio(request):
#     return render(request,'portfolio.html',{})
# def portfolio_single(request):
#     return render(request,'portfolio_single.html',{})
# def testimonials(request):
#     return render(request,'testimonials.html',{})
# def faq(request):
#     return render(request,'faq.html',{})
# def gallery(request):
#     return render(request,'gallery.html',{})
# def blog(request):
#     return render(request,'blog.html',{})
# def contact(request):
#     return render(request,'contact.html',{})
# def login(request):
#     return render(request,'login.html',{})

# def signup(request):
#     next = request.GET.get('next')
#     form = EmployeeRegistrationForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect('accounts:login')

#     context = {
#         'form': form,
#     }

#     return render(request, "login.html", context)


# def employee_login(request):
#     next = request.GET.get('next')
#     form = EmployeeLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 request.session.set_expiry(420)
#                 login(request, user)
#                 return redirect('/')
#     context = {
#         'form': form
#     }
#     return render(request, "login.html", context)


# def logout_view(request):
#     logout(request)
#     return redirect('accounts:login')

    
  
  
  
    



# # Create your views here.
