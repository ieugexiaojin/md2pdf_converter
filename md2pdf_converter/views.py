from django.http import HttpResponse
from md2pdf.core import md2pdf
from django.shortcuts import render


def upload_and_convert(request):
    print("Function called")  # 添加这一行
    if request.method == 'POST':
        print("POST request received")  # 添加这一行
        uploaded_file = request.FILES['document']
        md_content = uploaded_file.read().decode('utf-8')
        
        pdf_path = "output.pdf"
        md2pdf(pdf_path, md_content=md_content)
        
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()
        
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response





def index(request):
    return render(request, 'index.html')
