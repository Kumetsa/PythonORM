import os
from datetime import date

import django

# Set up Django
from django.db.models import Q, F, Count


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import VideoGame, BillingInfo, Invoice, Technology, Project, Programmer, Task, Exercise






