from django.contrib import admin
from .models import Alumno
from .models import Profesor
from .models import Asistencia
from .models import Curso
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Asistencia)
admin.site.register(Curso)