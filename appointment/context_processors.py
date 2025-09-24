from django.utils import timezone
from .models import Reminder

def future_reminder_count(request):
    future_reminders = Reminder.objects.filter(reminder_date__gt=timezone.now()).count()
    return {
        'future_reminder_count': future_reminders
    }