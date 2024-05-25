
import sys
from django.shortcuts import HttpResponse
import subprocess
import os

from Scripts.main import some_function

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
if script_path not in sys.path:
    sys.path.append(script_path)




def some_view(request):
    result = some_function()
    return HttpResponse(result)




def users(request):
    script_path = r'Scripts\main.py'
    if not os.path.exists(script_path):
        return HttpResponse(f"Error: File not found at {script_path}")

    try:
        subprocess.Popen(['python', script_path],shell=False)
        return HttpResponse("<h1>Tkinter application started</h1>.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")