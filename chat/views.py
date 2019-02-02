from typing import Any, Union, List
from django.db.models import QuerySet
from django.http import JsonResponse
from datetime import timedelta
from .models import Mes
from django.utils import timezone


def handler(request):
    how_many_days: int = 10
    lastid: int = request.GET.get('lastid', None)
    content: str = request.GET.get('content', None)
    Mes.objects.filter(created_at__lte=timezone.now() - timedelta(days=how_many_days)).delete()

    if lastid is not None and content is not None:
        new_item: Mes = Mes(
            id=lastid, name=request.GET.get('name'), content=content,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        new_item.save()

    if lastid is not None:
        filtered_data: QuerySet = Mes.objects.filter(id__gte=lastid).values()
        response_data: List = list(filtered_data.values())
        return JsonResponse(response_data, safe=False)
