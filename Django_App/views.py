
from django.shortcuts import HttpResponse, render
import subprocess
import os
from django.conf import settings


# def users(request):
#     script_path = r'Scripts\main.py'
#     if not os.path.exists(script_path):
#         return HttpResponse(f"Error: File not found at {script_path}")

#     try:
#         subprocess.Popen(['python', script_path],shell=False)
#         return HttpResponse("<h1>Tkinter application started</h1>.")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")



# def users(request):
#     # Construct the absolute path to the script
#     script_path = os.path.join(settings.BASE_DIR, 'Scripts', 'main.py')
    
#     # Check if the script exists at the specified path
#     if not os.path.exists(script_path):
#         return HttpResponse(f"Error: File not found at {script_path}")

#     try:
#         # Start the subprocess
#         subprocess.Popen(['python', script_path], shell=False)
#         return HttpResponse("Script Is starting")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}",status=500)
    


def run_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'Scripts', 'main.py')
    if not os.path.exists(script_path):
        return HttpResponse(f"Error: File not found at {script_path}")

    try:
        #Start the subprocess
        subprocess.Popen(['python', script_path],)
        return HttpResponse("<h1>Script Is starting</h1>")
    except Exception as e:
        return HttpResponse(f"Error: {e}")




def index01Pgae(request):
    return render(request,'index01.html')
