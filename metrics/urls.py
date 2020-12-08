from django.conf.urls import url
from fatpercentage.views import FatpercentageView, NewFatpercentageView

import metrics.views

urlpatterns = [
    url(r'^$', metrics.views.MetricsView.as_view(), name='metrics'),
    url(r'new_fatpercentage/', NewFatpercentageView.as_view(), name='new_fatpercentage'),
    url(r'fatpercentage/', FatpercentageView.as_view(), name='new_fatpercentage'),
]
