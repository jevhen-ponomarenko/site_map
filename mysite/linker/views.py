from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

ret = [
    {
        "link": "autodily-pomocna/skrbka-na-brambory.htm",
        "candidates": [
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
        ]

    },
    {
        "link": "autodily-pomocna/skrbka-na-brambory.htm",
        "candidates": [
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
        ]

    },
    {
        "link": "autodily-pomocna/skrbka-na-brambory.htm",
        "candidates": [
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
        ]

    },
    {
        "link": "autodily-pomocna/skrbka-na-brambory.htm",
        "candidates": [
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
            "autodily-pomocna/skrbka-na-brambory-45b.htm"
        ]

    }
]


def home(request):
    return HttpResponse('<h1> whatevs </h1>')


def about(request):
    context = {
        'objects': ret
    }
    return render(request, 'linker/about.html', context)
