import os
from .scripts.linker.compare import find_candidates_for_file
from .scripts.linker.parser import parse_file
from .scripts.linker.parser import save_file

from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



def home(request):
    return HttpResponse('<h1> whatevs </h1>')


def about(request):

    module_dir = os.path.dirname(__file__)  # get current directory
    new_file = parse_file(os.path.join(module_dir, 'scripts/linker/new.csv'))
    old_file = parse_file(os.path.join(module_dir, 'scripts/linker/old.csv'))
    ret = {'objects': find_candidates_for_file(new_file, old_file)}
    return render(request, 'linker/about.html', ret)

@csrf_exempt
def save(request):
    if request.method == "POST":
        ret_array = []

        for index, item in enumerate(request.POST.items()):
            ret_array.append(item[1])
            # for data in item:
            #     if index % 2 != 0:
            #         print('old link', data)
            #     else:
            #         print('new link', data)

        save_file(ret_array)

    return render(request, 'linker/base.html')



