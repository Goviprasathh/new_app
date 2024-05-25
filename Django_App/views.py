
from django.shortcuts import HttpResponse
import subprocess
import os




def users(request):
    script_path = r'Scripts\main.py'
    if not os.path.exists(script_path):
        return HttpResponse(f"Error: File not found at {script_path}")

    try:
        subprocess.Popen(['python', script_path],shell=False)
        return HttpResponse("<h1>Tkinter application started</h1>.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")