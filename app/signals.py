from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from app.models import MyModel
import time
import threading

def handle_sync_signal(instance):
    if instance.name == "TestSync":
        time.sleep(5)

def handle_transaction_signal(instance):
    if instance.name == "FailTransaction":
        raise ValidationError("Triggering rollback in transaction.")

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for {instance.name} in thread: {threading.current_thread().name}")
    
    handle_sync_signal(instance)
    handle_transaction_signal(instance)
    
    print("Signal processing completed.")
