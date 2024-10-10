from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('job_post/', job_post, name='job_post'),
    path('job_listing/', job_listing, name='job_listing'),
    path('job_single/<int:id>/', job_single, name='job_single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('service_single/',service_single, name='service_single'),

]
    # path('index/', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('job_listings/', views.job_listings, name='job_listings'),
    # path('job_single/', views.job_single, name='job_single'),
    # path('post_job/', views.post_job, name='post_job'),
    # path('services/', views.services, name='services'),
    # path('service_single/', views.service_single, name='service_single'),
    # path('blog_single/', views.blog_single, name='blog_single'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    # path('portfolio_single', views.portfolio_single, name='portfolio_single'),
    # path('testimonials/', views.testimonials, name='testimonials'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('faq/', views.faq, name='faq'),
    # path('blog/', views.blog, name='blog'),
    # path('contact/', views.contact, name='contact'),
    # path('login/', views.login, name='login'),   
    