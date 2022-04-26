import mimetypes
import os
from django.http import Http404, HttpResponse
from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER

from app.models import Assignment

# abstracted logic for downloading files from specific folders
def download_file(asignmentId, folder):
    # find the current assignment in database
    assignment = Assignment.objects.get(id=asignmentId)

    # get fileName from current assignment
    if folder == TEMPLATES_FOLDER:
        fileName = os.path.basename(assignment.assignmentTemplate.name)
    if folder == SOLUTIONS_FOLDER:
        fileName = os.path.basename(assignment.solutionFile.name)

    #fileName should not be None
    if fileName == None:
        return Http404()

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the full file path
    filepath = BASE_DIR + '/media/'+ folder +'/' + fileName

    # Open the file for reading content
    path = open(filepath, 'rb')

    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)

    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)

    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % fileName

    # Return the response value
    return response