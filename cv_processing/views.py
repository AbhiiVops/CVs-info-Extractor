from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .utils import process_cvs
import os

def upload_cv(request):
    if request.method == 'POST':
        cv_files = request.FILES.getlist('cv_files')
        output_file = 'output_{}.xlsx'.format(os.urandom(8).hex())
        output_path = os.path.join('media', output_file)
        process_cvs(cv_files, output_path)
        return redirect('download_excel', filename=output_file)
    request.session['uploaded_files'] = []
    
    return render(request, 'upload.html')

def download_excel(request, filename):
    file_path = os.path.join('media', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        return HttpResponse('File not found.')