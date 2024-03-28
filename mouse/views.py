from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MouseEvent
from django.utils.dateparse import parse_datetime
import json

def track_mouse_page(request):
    return render(request, 'mouse/track-mouse.html')

@csrf_exempt
def track_mouse(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # event_data = data.get('data')
        # event_type = data.get('type')
        
        # MouseEvent.objects.create(
        #     event_type=event_type,
        #     x=event_data['x'],
        #     y=event_data['y'],
        #     timestamp=parse_datetime(event_data['timestamp'])
        # )

        for event_data in data:
            MouseEvent.objects.create(
                event_type=event_data['type'],
                x=event_data['x'],
                y=event_data['y'],
                timestamp=parse_datetime(event_data['timestamp'])
            )
        
        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'error'}, status=400)

def view_mouse_events(request):
    events = MouseEvent.objects.all().order_by('-timestamp')[:10]  
    return render(request, 'mouse/view_events.html', {'events': events})

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import MouseEvent
# from django.utils.dateparse import parse_datetime
# from django.contrib.auth.decorators import login_required  # 로그인 필요
# import json

# def track_mouse_page(request):
#     return render(request, 'mouse/track-mouse.html')

# @csrf_exempt
# # @login_required  # 로그인한 사용자만 이 뷰에 접근 가능
# def track_mouse(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
        
#         # event_data = data.get('data')
#         # event_type = data.get('type')
        
#         # MouseEvent.objects.create(
#         #     event_type=event_type,
#         #     x=event_data['x'],
#         #     y=event_data['y'],
#         #     timestamp=parse_datetime(event_data['timestamp'])
#         # )

#         for event_data in data:
#             MouseEvent.objects.create(
#                 # user=request.user,  # 현재 로그인한 사용자와 연결
#                 event_type=event_data['type'],
#                 x=event_data['x'],
#                 y=event_data['y'],
#                 timestamp=parse_datetime(event_data['timestamp'])
#             )
        
#         return JsonResponse({'status': 'success'}, status=200)
#     return JsonResponse({'status': 'error'}, status=400)

# # @csrf_exempt
# # def track_keyboard(request):
# #     if request.method == 'POST':
# #         data = json.loads(request.body)
# #         KeyboardEvent.objects.create(
# #             key=data['key'],
# #             # timestamp=parse_datetime(data['timestamp'])
# #         )
# #         return JsonResponse({'status': 'success'}, status=200)
# #     return JsonResponse({'status': 'error'}, status=400)

# def view_mouse_events(request): # 최근 10개의 이벤트를 조회
#     events = MouseEvent.objects.all().order_by('-timestamp')[:10]  
#     return render(request, 'mouse/view_events.html', {'events': events})