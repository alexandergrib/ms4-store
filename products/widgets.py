from django.forms.widgets import ClearableFileInput
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/' \
                    'custom_clearable_file_input.html'


class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [
            super(RelatedFieldWidgetCanAdd, self).render(name, value, *args,
                                                         **kwargs),
            '<a href="%s" class="add-another" id="add_id_%s" \
             onclick="return showAddAnotherPopup(this);"> ' % (
                self.related_url, name),

            '<i class="fas fa-plus"></i>%s</a>' % (
                'Add Another')]
        return mark_safe(''.join(output))
