# tasks/views.py

from django.shortcuts import render, redirect
from .forms import TaskForm

def task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # or any other URL after successful form submission
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})
