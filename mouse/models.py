from django.db import models
# from django.contrib.auth.models import User

class MouseEvent(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 필드 추가
    TYPE_CHOICES = [
        ('click', 'Click'),
        ('move', 'Move'),
    ]
    event_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.DateTimeField()

# class KeyboardEvent(models.Model):
#     key = models.CharField(max_length=100)  # 키보드 입력값 저장
#     timestamp = models.DateTimeField(auto_now_add=True)  # 이벤트 발생 시간

#     def __str__(self):
#         return f"{self.key} at {self.timestamp}"