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

        form = request.POST
        issuedDate=request.POST['issuedate']
        print(issuedDate)
        # print(form)
        # if form.is_valid():
            # form = form.save()
        print(form['firstName'],form['secondName'],form['course'],form['course']+ '_' + form['firstName'] + form['secondName'] + '.pdf')
        generate_certificate(form['firstName'],form['secondName'],form['course'],form['courseDetails'],form['companyLink'],issuedDate,form['companyName'],form['ceoName'],form['course']+ '_' + form['firstName'] + form['secondName'] + '.pdf')

        return render(request, 'download.html', {'data': form,'issuedDate':issuedDate,'pdf':form['course']+ '_' + form['firstName'] + form['secondName'] + '.pdf'})
        # else:
        #     return HttpResponse('Your Form is wrong')

    return render(request, 'register.html', {'forms': PersonForm()})


def generate_certificate(first_name, last_name, course_name,course_details, company_link, date_field, company_name, ceo_name, pdf_file_name):
    attendee_name= first_name + ' '+ last_name
    c=canvas.Canvas('dgcirt/static/'+pdf_file_name, pagesize=landscape(letter))

    #header text
    c.setFont('Helvetica',48, leading=None)
    c.drawCentredString(400, 550, "Certification of Completion")
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(400, 500, "This certificate is presented to")

    # attendee name
    c.setFont('Helvetica-Bold',34, leading=None)
    c.drawCentredString(400, 450, attendee_name)

    # for completing the course
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(400, 400, 'for completion the following course:')
    
    #course name
    c.setFont('Helvetica-Bold',24, leading=None)
    c.drawCentredString(400, 360, course_name)
    
    #course Details
    c.setFont('Helvetica',12, leading=None)
    c.drawCentredString(400, 330, course_details)
    
    #Company Link
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(170, 270, 'Company Link')

    #Link
    c.setFont('Helvetica',12, leading=None)
    c.drawCentredString(170, 240, company_link)
    
    #Issued Date
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(620, 270, 'Issued Date')

    #Issued Date
    c.setFont('Helvetica',12, leading=None)
    c.drawCentredString(620, 240, date_field)

    #Issued BY
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(170, 115, 'Issued By:')
    
    #Company Name
    c.setFont('Helvetica',12, leading=None)
    c.drawCentredString(170, 85,company_name)

    # image of seal
    seal='seal.png'
    c.drawImage(seal, 340, 120, width=None, height=None)

    #Name of ceo
    c.setFont('Helvetica',24, leading=None)
    c.drawCentredString(620, 115, 'Name Of CEO')

    #Ceo Name
    c.setFont('Helvetica',12, leading=None)
    c.drawCentredString(620, 85, ceo_name)
    

    c.showPage()
    print('writing')
    c.save()



