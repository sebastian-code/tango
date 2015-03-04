from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url_display')

	def url_display(self, obj):
		return u"<a href='%s'>%s</a>" % (obj.url, obj.url)

	url_display.allow_tags = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)