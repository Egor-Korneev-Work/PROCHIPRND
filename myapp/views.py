from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def services(request):
    services_list = [
        {"name": "Чип-тюнинг двигателей", "desc": "От 3000 ₽"},
        {"name": "Компьютерная диагностика", "desc": "От 1000 ₽"},
        {"name": "Отвязка мочевины(AdBlue)", "desc": "От 10000 ₽ "},
        {"name": "Регулировка фар", "desc": "От 700 ₽"},
        {"name": "Замена ламп", "desc": "От 1000 ₽"},
        {"name": "Промывка форсунок", "desc": "От 1600 ₽"},
        {"name": "Замена форсунок", "desc": "От 1000 ₽"},


    ]
    return render(request, 'services.html', {'services': services_list})

def portfolio(request):
    projects = [
        {
            "title": "Прошивка stage1 Opel",
            "image": "% static 'images/1.jpg' %",
            "description": "Прошивка двигателя stage1. Увеличение мощности на 20%.\n\nУлучшена реакция педали газа, оптимизирован расход топлива на 7%."
        },
        {
            "title": "Регулировка фар",
            "image": "% static 'images/2.jpg' %",
            "description": "Настроили фары по спец. прибору теперь водитель чуствует себя на много комфортнее в темное время суток на дороге"
        },
        {
            "title": "Отстрелы popcorn",
            "image": "video/IMG_4544.MP4",
            "description": "Прошивка благодаря, которой ваш автомобиль звучит по новому",
        },
        {
            "title": "Прошивка stage1 Chery",
            "image": "images/3.jpg",
            "description": "Прошивка двигателя stage1. Увеличение мощности на 20%.\n\nУлучшена реакция педали газа, оптимизирован расход топлива на 7%."
        },
        {
            "title": "Перопрограмирование блока ЭБУ",
            "image": "images/4.jpg",
            "description": "Увеличение мощности двигателя.\n\nУлучшена реакция педали газа, снижен расход топлива."
        },
        {
            "title": "Отстрелы глушителя",
            "image": "video/IMG_4548.MP4",
            "description": "Новый интересный звук вашего выхлопа",
        }
    ]
    return render(request, 'portfolio.html', {'projects': projects})
def portfolio_detail(request, project_id):
    projects = [
        {
            "id": 1,
            "title": "Прошивка stage1",
            "image": "images/1.jpg",
            "description": "Прошивка двигателя stage1. Увеличение мощности на 20%.\n\nУлучшена реакция педали газа, оптимизирован расход топлива на 7%."
        },
        {
            "id": 2,
            "title": "Регулировка фар",
            "image": "images/2.jpg",
            "description": "Настроили фары по спец. прибору теперь водитель чуствует себя на много комфортнее в темное время суток на дороге"
        },
        {
            "id": 3,
            "title": "Отстрелы popcorn",
            "image": "video/IMG_4544.MP4",  #
            "description": "Прошивка благодаря, которой ваш автомобиль звучит по новому",
        },
        {
            "id": 4,
            "title": "Прошивка stage1",
            "image": "images/3.jpg",
            "description": "Прошивка двигателя stage1. Увеличение мощности на 20%.\n\nУлучшена реакция педали газа, оптимизирован расход топлива на 7%."
        },
        {
            "id": 5,
            "title": "Перопрограмирование блока ЭБУ",
            "image": "images/4.jpg",
            "description": "Увеличение мощности двигателя.\n\nУлучшена реакция педали газа, снижен расход топлива."
        },
        {
            "id": 6,
            "title": "Отстрелы глушителя",
            "image": "video/IMG_4548.MP4",
            "description": "Новый интересный звук вашего выхлопа",
        },
    ]

    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        project = projects[0]  # fallback

    return render(request, 'portfolio_detail.html', {'project': project})

def contacts(request):
    return render(request, 'contacts.html')