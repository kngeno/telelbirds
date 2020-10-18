from datetime import datetime

from django import forms
from django.contrib import admin

from redactor.widgets import RedactorEditor

from blogs.models import Blog, BlogAd


class BlogAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogAdminForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget = RedactorEditor()


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'modified')
    list_display = ('title', 'author', 'status', 'date_published', 'created',
                    'modified', 'tag_list',)
    list_select_related = ('author', 'tags',)
    list_filter = ('status', 'author', 'tags',)
    search_fields = (
        'title',
        'content',
    )

    fieldsets = (
        ('', {
            'fields': ('status', 'author',)
        }),
        ('Content', {
            'fields': ('title', 'slug', 'content', 'tags', 'date_published')
        }),
    )

    def tag_list(self, obj):
        """
        Retrieve the tags separated by comma.
        """
        return ', '.join([t.name for t in obj.tags.all()])
    tag_list.short_description = 'Tags'

    def get_form(self, request, obj=None, **kwargs):
        """
        Set default author based on logged in user.
        """
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)

        form.base_fields['author'].initial = request.user

        return form

    def save_model(self, request, obj, form, change):
        """
        Automatically set the published_date if the value is None
        and the status is set to 'published'.
        """
        if not obj.date_published and obj.status == 'published':
            obj.date_published = datetime.now()

        super(BlogAdmin, self).save_model(request, obj, form, change)


class BlogAdAdmin(admin.ModelAdmin):
    list_display = ('description', 'position', 'created', 'modified')


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogAd, BlogAdAdmin)
