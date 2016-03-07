from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
class TagInline(admin.TabularInline):	#内联显示
	model = Tag
	
class ContactAdmin(admin.ModelAdmin):
	#fields = ('name', 'email')
	inlines = [TagInline]	#Inline	内联显示
	list_display = ('name', 'age', 'email')	#列表显示
	search_fields = ('name',)	#搜索栏功能
	fieldsets = (	#自定义表单
		[
			'Main', {
				'fields': ('name', 'email')
			}
		],
		[
			'Advance', {
				'classes': ('collapse',),	#css
				'fields': ('age',)
			}
		]
	)

	
#admin.site.register([Test, Contact, Tag])
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])