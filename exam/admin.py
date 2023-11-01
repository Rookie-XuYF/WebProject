from django.contrib import admin
from exam.models import Question, Answer, Chapter, Unit, Knowledge_point

# Register your models here.


admin.site.register(Chapter)
admin.site.register(Unit)
admin.site.register(Knowledge_point)
admin.site.register(Question)
admin.site.register(Answer)
