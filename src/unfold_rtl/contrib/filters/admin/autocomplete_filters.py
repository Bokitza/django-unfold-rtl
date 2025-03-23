from unfold_rtl.contrib.filters.admin.dropdown_filters import (
    MultipleRelatedDropdownFilter,
    RelatedDropdownFilter,
)
from unfold_rtl.contrib.filters.admin.mixins import AutocompleteMixin
from unfold_rtl.contrib.filters.forms import AutocompleteDropdownForm


class AutocompleteSelectFilter(AutocompleteMixin, RelatedDropdownFilter):
    form_class = AutocompleteDropdownForm


class AutocompleteSelectMultipleFilter(
    AutocompleteMixin, MultipleRelatedDropdownFilter
):
    form_class = AutocompleteDropdownForm
