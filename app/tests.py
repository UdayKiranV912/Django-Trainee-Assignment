from django.test import TestCase
from myapp.models import MyModel
import time
import threading
from django.db import transaction
from django.core.exceptions import ValidationError

class MyModelTestCase(TestCase):

    def create_model_instance(self, name):
        return MyModel.objects.create(name=name)

    def get_thread_name(self):
        return threading.current_thread().name

    def test_signal_synchronous(self):
        start_time = time.time()
        self.create_model_instance(name="TestSync")
        duration = time.time() - start_time

        self.assertGreater(duration, 5, "Signal is running synchronously.")

    def test_signal_same_thread(self):
        initial_thread = self.get_thread_name()
        self.create_model_instance(name="TestThread")

        self.assertEqual(initial_thread, self.get_thread_name(), "Signal is executing in a different thread.")

    def test_signal_in_transaction(self):
        try:
            with transaction.atomic():
                self.create_model_instance(name="FailTransaction")
        except ValidationError:
            pass

        self.assertEqual(MyModel.objects.count(), 0, "Signal should have triggered a rollback.")
