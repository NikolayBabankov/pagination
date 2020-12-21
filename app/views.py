from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import csv
from django.conf import settings
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    results = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as File:
        reader = csv.DictReader(File)
        for row in reader:
            tmp = {}
            tmp.setdefault('Name',row['Name'])
            tmp.setdefault('Street',row['Street'])
            tmp.setdefault('District',row['District'])
            results.append(tmp)
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(results, settings.ADRESS_PER_PAGES)
    page_obj = paginator.get_page(current_page)
    if page_obj.has_next():
        next_page_url = reverse('bus_stations') + f'?page={page_obj.next_page_number()}'
    else:
        next_page_url = None
    if not page_obj.has_previous():
        prev_page_url = None
    else:
        prev_page_url = reverse('bus_stations') + f'?page={page_obj.previous_page_number()}'
    list_name = [x['Name'] for x in page_obj.object_list]
    list_street = [x['Street'] for x in page_obj.object_list]
    list_dist = [x['District'] for x in page_obj.object_list]
    return render(request, 'index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

