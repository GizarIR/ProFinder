from django.shortcuts import render

def projects(request):
    projectsList = [
        {'pk':'1',
         'title':'Онлайн-кинотеатр',
         'description':'Кинотеатр с самой полной библиотекой фильмов.'
         },
        {'pk':'2',
         'title':'Платформа с ИТ-курсами',
         'description':'Курсы по фронтенду, бэкенду и мобильной разработке.'
         },
        {'pk':'3',
         'title':'Рекрутинговый портал','description':'Вакансии для специалистов экстра-класса.'
         },
    ]
    return render(request, 'projects.html', {'projects': projectsList})

def project(request, pk):
    return render(request, 'single-project.html')