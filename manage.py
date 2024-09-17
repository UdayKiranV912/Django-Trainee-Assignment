import os
import sys
import django
from django.core.management import execute_from_command_line

def set_django_settings():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "signals_assessment.settings")

def check_django_import():
    try:
        import django
    except ImportError as exc:
        raise ImportError(
            "Django is not installed or not available on your PYTHONPATH. "
            "Ensure Django is installed and your virtual environment is activated."
        ) from exc

def main():
    set_django_settings()
    check_django_import()
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
