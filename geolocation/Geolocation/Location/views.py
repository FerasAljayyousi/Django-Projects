from django.shortcuts import render
import  requests
import json
def Index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    idata = json.loads(ip.text)
    res = requests.get('https://geoip.maxmind.com/geoip/v2.1/country/'+ idata['ip'])
    data = res.text
    location_data = json.loads(data)
    return render(request, 'index.html', {'data':location_data })

# Create your views here.
