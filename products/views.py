from django.contrib import messages
from django.core.mail import mail_managers
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import Category, Product, SiteSettings, Testimonial


def home(request):
    settings = SiteSettings.objects.first()
    featured = Product.objects.filter(is_featured=True).select_related("category")[:8]
    categories = Category.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            try:
                mail_managers(
                    f"New enquiry from {contact.name}",
                    f"Email: {contact.email}\nPhone: {contact.phone or 'Not provided'}\n\n{contact.message}",
                )
            except Exception:
                # Saving the enquiry is sufficient; email is optional for local deployments.
                pass
            messages.success(request, "Thank you! Your message has been received.")
            form = ContactForm()
        else:
            messages.error(request, "Please correct the highlighted fields.")
    else:
        form = ContactForm()

    return render(request, "home.html", {
        "site_settings": settings,
        "featured_products": featured,
        "categories": categories,
        "testimonials": testimonials,
        "contact_form": form,
    })


def privacy(request):
    return render(request, "privacy.html")


def terms(request):
    return render(request, "terms.html")
