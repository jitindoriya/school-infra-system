from django.shortcuts import render


# Create your views here.
def index(request):
    '''
    Function return index.html from template dir
    :param request:
    :return:
    '''
    return render(request, 'schoolmanagement/index.html', {"admin_name": "schoolinfra"})


def thanks(request):
	render_to_response('schoolmanagement/thanks.html')

