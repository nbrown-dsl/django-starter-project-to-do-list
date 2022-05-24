from __future__ import print_function
from docx import Document
import os

from mailmerge import MailMerge
from datetime import date
from django.conf import settings

def mailmergeDoc(years,studentObject):
    template_1 = "dwight-transcript.docx"
    

    # Show a simple example
    document_3 = MailMerge(template_1)
    print("Fields included in {}: {}".format(template_1,
                                         document_3.get_merge_fields()))
    # Merge in the values
    student= {
    'firstName' :studentObject['first_name'],
    'secondName':studentObject['last_name'],
    }
   
    terms=[]
    for year in years[0]:
        for term in year['terms']:
            terms.append({ 'year': year['yearName'],'term': term['termName'], 'subject_name':term['classGrades']})

    print (terms)

    document_3 = MailMerge(template_1)
    document_3.merge(**student)
    document_3.merge_templates(terms, separator='continuous_section')
    filename = studentObject['first_name']+' transcript.docx'
    # filepath = str(settings.DOWNLOAD_FILES[0])+'/'+ filename
    filepath = os.path.join(settings.DOWNLOAD_FILES[0], filename)
    document_3.write(filepath)

    return filepath

