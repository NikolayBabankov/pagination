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
    next_page_url = reverse('bus_stations') + f'?page={page_obj.next_page_number()}'
    # print(page_obj.num_pages())
    if current_page == 1:
        prev_page_url = None
    else:
        prev_page_url = reverse('bus_stations') + f'?page={page_obj.previous_page_number()}'
    list_name = [x['Name'] for x in page_obj.object_list]
    list_street = [x['Street'] for x in page_obj.object_list]
    list_dist = [x['District'] for x in page_obj.object_list]
    return render(request, 'index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
                         {'Name': list_name[0], 'Street': list_street[0] , 'District': list_dist[0]},
                         {'Name': list_name[1], 'Street': list_street[1] , 'District': list_dist[1]},
                         {'Name': list_name[2], 'Street': list_street[2] , 'District': list_dist[2]},
                         {'Name': list_name[3], 'Street': list_street[3] , 'District': list_dist[3]},
                         {'Name': list_name[4], 'Street': list_street[4] , 'District': list_dist[4]},
                         {'Name': list_name[5], 'Street': list_street[5] , 'District': list_dist[5]},
                         {'Name': list_name[6], 'Street': list_street[6] , 'District': list_dist[6]},
                         {'Name': list_name[7], 'Street': list_street[7] , 'District': list_dist[7]},
                         {'Name': list_name[8], 'Street': list_street[8] , 'District': list_dist[8]},
                         {'Name': list_name[9], 'Street': list_street[9] , 'District': list_dist[9]}
                         ],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

    # return HttpResponse(page_obj.object_list)
# words = ['end', 'nend']
# print('\n'.join(words))

