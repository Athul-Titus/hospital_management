from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import departments, doctors, booking

def index(request):
    return HttpResponse("Hello")
def data(request):
    return HttpResponse("Homepage")

def home(request):
    student = {
        "name": "Dev",
        "Age": 32,
        "Place":"Tvm"
    }
    return render(request,"home.html",student)

def about(request):
    return render(request,"about.html")

def details(request):
    services = [
        {"title": "Cardiology", "desc": "Heart care, diagnostic testing, treatment, and cardiac rehabilitation.", "icon": "❤️"},
        {"title": "Emergency Care", "desc": "24/7 immediate care for acute illnesses and traumatic injuries.", "icon": "🚑"},
        {"title": "Radiology", "desc": "X-Rays, MRI, CT scans, and ultrasounds with state-of-the-art imaging.", "icon": "🩻"},
        {"title": "Neurology", "desc": "Expert diagnostics and care for brain, spine, and nervous system disorders.", "icon": "🧠"},
        {"title": "Pediatrics", "desc": "Comprehensive medical care specifically tailored for infants, children, and teens.", "icon": "👶"},
        {"title": "General Surgery", "desc": "Advanced surgical procedures using minimally invasive techniques.", "icon": "🔪"}
    ]
    return render(request, "details.html", {"services": services})

def booking_view(request):
    success_msg = None
    if request.method == "POST":
        name = request.POST.get('p_name')
        phone = request.POST.get('p_phone')
        email = request.POST.get('p_email')
        doc_id = request.POST.get('doc_name')
        date = request.POST.get('booking_date')
        
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        
        if name and phone and email and doc_id and date:
            try:
                doc = doctors.objects.get(id=doc_id)
                booking.objects.create(
                    p_name=name,
                    p_phone=phone,
                    p_email=email,
                    doc_name=doc,
                    booking_date=date
                )
                msg = f"Thank you, {name}! Your appointment has been booked successfully."
                if is_ajax:
                    return JsonResponse({"success": True, "message": msg})
                success_msg = msg
            except (doctors.DoesNotExist, ValueError):
                if is_ajax:
                    return JsonResponse({"success": False, "message": "Selected doctor does not exist."})
        else:
            if is_ajax:
                return JsonResponse({"success": False, "message": "All fields are required."})
                
    all_doctors = doctors.objects.all()
    return render(request, "booking.html", {"doctors": all_doctors, "success_msg": success_msg})

def bookings_list_view(request):
    all_bookings = booking.objects.select_related('doc_name', 'doc_name__dep_name').order_by('booking_date')
    return render(request, "bookings_list.html", {"bookings": all_bookings})

def departments_view(request):
    if request.method == "POST":
        name = request.POST.get('dept_name')
        desc = request.POST.get('dep_description')
        if name and desc:
            departments.objects.create(dept_name=name, dep_description=desc)
    all_departments = departments.objects.all()
    return render(request, "departments.html", {"departments": all_departments})

def doctors_view(request):
    if request.method == "POST":
        name = request.POST.get('doc_name')
        spec = request.POST.get('doc_spec')
        dep_id = request.POST.get('dep_name')
        image = request.FILES.get('doc_image')
        if name and spec and dep_id:
            try:
                dept = departments.objects.get(id=dep_id)
                doctors.objects.create(doc_name=name, doc_spec=spec, dep_name=dept, doc_image=image)
            except (departments.DoesNotExist, ValueError):
                pass
    all_doctors = doctors.objects.select_related('dep_name').all()
    all_departments = departments.objects.all()
    return render(request, "doctors.html", {"doctors": all_doctors, "departments": all_departments})
