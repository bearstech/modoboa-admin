"""Custom form tools."""

from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.utils.translation import ugettext as _, ugettext_lazy


def validate_email_address(value):
    """Check if value contains exactly one @."""
    if value.count("@") != 1:
        raise ValidationError(_("Enter a valid email address"), "invalid")


class SimpleEmailField(CharField):

    """A field that accepts email addresses."""

    default_error_messages = {
        "invalid": ugettext_lazy("Enter a valid email address")
    }

    default_validators = [validate_email_address]

    def clean(self, value):
        """Clean address."""
        value = self.to_python(value).strip()
        return super(SimpleEmailField, self).clean(value)
