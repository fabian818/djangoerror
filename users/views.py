from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
from django.utils import timezone
from users.models import User

@api_view(['POST'])
def test(request):
    print('test')
    user = User.objects.first()
    first_day = user.created_at - timedelta(days=user.created_at.weekday())
    diff = int(((timezone - first_day).days / 7) + 1)
    data = {"msg": diff}
    return JsonResponse(data, safe=False)