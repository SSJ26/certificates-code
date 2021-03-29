from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
import os
print('Base path',os.path.join(BASE_DIR,'dgcirt'))
def register(request):
    
    if request.method == 'POST':

        form = PersonForm(request.POST)
        print(form)
        if form.is_valid():
            form = form.save()
            print(form.firstName,form.secondName,form.course,form.course+ '_' + form.firstName + form.secondName + '.pdf')
            generate_certificate(form.firstName,form.secondName,form.course,form.course+ '_' + form.firstName + form.secondName + '.pdf')

            return render(request, 'download.html', {'data': form,'pdf':form.course+ '_' + form.firstName + form.secondName + '.pdf'})
        # else:
        #     return HttpResponse('Your Form is wrong')

    return render(request, 'register.html', {'forms': PersonForm()})



# def import_data(data_file):
#     attendee_data=csv.reader(open(data_file,"rb"))
#     for row in attendee_data:
#         last_name=row[0]
#         first_name=row[1]
#         course_name=row[2]
#         pdf_file_name=course_name+ ' ' + last_name + first_name + '.pdf'
#         generate_certificate(first_name, last_name, course_name, pdf_file_name)

def generate_certificate(first_name, last_name, course_name, pdf_file_name):
    attendee_name= first_name + ' '+ last_name
    c=canvas.Canvas('dgcirt/static/'+pdf_file_name, pagesize=landscape(letter))

    #header text
    c.setFont('Helvetica',48, leading=None)
    c.drawCentredString(415, 500, "Certification of Completion")
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(415, 450, "This certificate is presented to")

    # attendee name
    c.setFont('Helvetica-Bold',34, leading=None)
    c.drawCentredString(415, 395, attendee_name)

    # for completing the course
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(415, 350, 'for completion the following course:')
    
    #course name
    c.setFont('Helvetica',20, leading=None)
    c.drawCentredString(415, 310, course_name)

    # image of seal
    seal='seal.png'
    c.drawImage(seal, 350, 30, width=None, height=None)

    c.showPage()
    print('writing')
    c.save()

# import_data(data_file)


