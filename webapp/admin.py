from django.contrib import admin
from webapp.models import MCQ_Quiz, Results, True_False, Txt_Question
# Register your models here.
admin.site.register(MCQ_Quiz)
admin.site.register(Results)
admin.site.register(True_False)
admin.site.register(Txt_Question)