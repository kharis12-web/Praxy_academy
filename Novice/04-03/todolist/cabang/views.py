from django.shortcuts import render, redirect
from . import models

def index(req):
    if req.POST:
        models.Task.objects.create(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/cabang')

    tasks = models.Task.objects.all()
    return render(req, 'cabang/index.html',{
        'data': tasks,
    })


def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'cabang/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/task')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(name=req.POST['namaobat'], 
        jenisobat=req.POST['jenisobat'], quantity=req.POST['quantity'])
        return redirect('/cabang')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'cabang/update.html', {
        'data': task,
    })
