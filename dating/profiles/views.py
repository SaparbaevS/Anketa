from django.shortcuts import render

from profiles.models import Profile


def show_profiles(request):
    context = {"profiles": Profile.objects.all()}
    return render(request, "index.html", context=context)

def show_profile(request, profile_id):
    context = {"profile": Profile.objects.get(pk=profile_id)}
    return render(request, "profile.html", context=context)


def register(request):
    if request.method == "POST":
        name = request.GET.get("name")
        surname = request.GET.get("surname")
        age = request.GET.get("age")
        status = request.GET.get("status")
        salary = request.GET.get("salary")
        description = request.GET.get("description")

        Profile.objects.get(name=name,
                            surname=surname,
                            age=age,
                            status=status,
                            salary=salary,
                            description=description)
    return render(request, "add.html")
