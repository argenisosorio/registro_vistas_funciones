
# -*- coding: utf-8 -*-from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from registro.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'cedula']


def Consultar(request, template_name='registro/consultar.html'):
    persona = Persona.objects.all()
    data = {}
    data['object_list'] = persona
    return render(request, template_name, data)


def Registrar(request, template_name='registro/registrar.html'):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})


def Editar(request, pk, template_name='registro/registrar.html'):
    persona= get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save()
        return redirect('registro:consultar')
    return render(request, template_name, {'form':form})


def Borrar(request, pk, template_name='registro/borrar.html'):
    persona= get_object_or_404(Persona, pk=pk)    
    if request.method=='POST':
        persona.delete()
        return redirect('registro:consultar')
    return render(request, template_name, {'object':persona})
