from django.contrib import admin
from django import forms

import polls.models as models


class PollsForm(forms.ModelForm):
    class Meta:
        model = models.Polls
        fields = '__all__'

    def clean_to_date(self):
        from_date = self.cleaned_data['from_date']
        to_date = self.cleaned_data['to_date']

        if from_date > to_date:
            raise forms.ValidationError(
                "Дата окончания не может быть раньше, даты старта")
        return to_date


@admin.register(models.Polls)
class PollsAdmin(admin.ModelAdmin):
    list_display = ("name", "from_date", "to_date", "description")
    search_fields = ("name", "description")
    form = PollsForm

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()
        return ("from_date",)


class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 1
    fields = ('text', 'is_valid')


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("name", "polls", "type", "draft")
    list_filter = ("polls", "name", "type")
    inlines = [AnswerInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
