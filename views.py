from django.shortcuts import render, redirect
from .models import CoffeeItem, Feedback
from .forms import FeedbackForm, NewsletterForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.contrib import messages

def home(request):
    coffees = CoffeeItem.objects.all()
    best_sellers = CoffeeItem.objects.filter(is_best_seller=True)
    feedback_form = FeedbackForm()
    newsletter_form = NewsletterForm()

    context = {
        'coffees': coffees,
        'best_sellers': best_sellers,
        'feedback_form': feedback_form,
        'newsletter_form': newsletter_form
    }
    return render(request, 'Kohi/homepage.html', context)

def menu_page(request):
    return render(request, 'Kohi/menu.html')

def map_view(request):
    return render(request, 'Kohi/map.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'Kohi/register.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')

def add_to_cart(request, item_id):
    print("Adding item to cart:", item_id)
    return redirect('home')

def job_application_view(request):
    return render(request, 'Kohi/job_application.html')

def submit_job_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        resume = request.FILES.get('resume')  # Optional

        subject = f'New Job Application - {position}'
        body = f'''
        Name: {name}
        Email: {email}
        Position: {position}
        '''

        email_message = EmailMessage(
            subject,
            body,
            to=['sumaiyabhuts.1996@gmail.com'],  # your receiving email
            from_email='your_email@gmail.com'
        )

        if resume:
            email_message.attach(resume.name, resume.read(), resume.content_type)

        email_message.send()

        messages.success(request, "Your application has been sent successfully!")
        return redirect('home')  # redirect as you prefer

    return redirect('home')