import datetime

from portal.models import WebsiteName

def get_current_year_to_context(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_year': current_datetime.year
    }

def get_Website_Name(request):
    websitename = WebsiteName.objects.get(id=1)
    return {
        "WebsiteName": websitename
    }