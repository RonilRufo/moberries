from django.utils.translation import ugettext_lazy as _

ORDER_IN_PROGRESS = 'progress'
ORDER_PAID = 'paid'
ORDER_COMPLETED = 'completed'
ORDER_CANCELLED = 'cancelled'


ORDER_CHOICES = (
    (ORDER_IN_PROGRESS, _('In Progress')),
    (ORDER_PAID, _('Paid')),
    (ORDER_COMPLETED, _('Completed')),
    (ORDER_CANCELLED, _('Cancelled')),
)
