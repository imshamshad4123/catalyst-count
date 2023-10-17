from django.contrib import admin

# Register your models here.
from .models import Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'domain',
                    'year_founded', 'industry','size_range')


admin.site.register(Company, CompanyAdmin)