from django.contrib import admin

# Register your models here.
from django.contrib import admin

from myapp.models import Emp0, Dept0


class DeptAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'location')
    ordering = ('no', )


class EmpAdmin(admin.ModelAdmin):

    list_display = ('no', 'name', 'job', 'mgr', 'sal', 'comm', 'dept0')
    search_fields = ('name', 'job')


admin.site.register(Dept0, DeptAdmin)
admin.site.register(Emp0, EmpAdmin)