from django.conf.urls import url
from fatpercentage.views import FatpercentageView

import metrics.views

urlpatterns = [
    url(r'^$', metrics.views.MetricsView.as_view(), name='metrics'),
    url(r'new_fatpercentage/', FatpercentageView.as_view(), name='new_fatpercentage'),
]
