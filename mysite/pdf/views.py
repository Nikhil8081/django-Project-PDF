# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Profile
import pdfkit

# Form submission view
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        summary = request.POST.get("summary", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        skills = request.POST.get("skills", "")
        previous_work = request.POST.get("previous_work", "")
        degree = request.POST.get("degree", "")

        profile = Profile(
            name=name,
            email=email,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills,
            summary=summary,
            phone=phone
        )
        profile.save()

    return render(request, 'pdf/accept.html')


# Resume PDF generation view
def resume(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': profile})

    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8"
    }

    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response
