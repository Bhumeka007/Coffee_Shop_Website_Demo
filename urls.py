from django.urls import path
#from . import views
from .views import home, submit_feedback, add_to_cart, subscribe_newsletter, register, submit_job_application, job_application_view, map_view, menu_page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('register/', register, name='register'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('submit_job_application/', submit_job_application, name='submit_job_application'),
    path('apply-job/', job_application_view, name='job_application'),
    path('map/', map_view, name='map'),
    path('menu/', menu_page, name='menu_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
