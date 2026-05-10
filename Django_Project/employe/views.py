from django.shortcuts import render, redirect , get_object_or_404
from .models import *
from .forms import EmployeForms

def liste_employes(request):
    employes = employe.objects.all()
    return render(request, 'employe/list.html', {'employes' :employes})


def ajouter_employe(request):
    form = EmployeForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employe')
    return render(request, 'employe/formulaire.html', {'form' :form})
    
def modifier_employe(request, id):
    emp = get_object_or_404(employe, id=id)

    form = EmployeForms(request.POST or None, instance=emp)

    if form.is_valid():
        form.save()
        return redirect('liste_employe')

    return render(request, 'employe/formulaire.html', {'form': form})

def supprimer_employe(request, id):
    emp = get_object_or_404(employe, id=id)

    emp.delete()

    return redirect('liste_employe')