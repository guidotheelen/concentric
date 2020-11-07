from django.conf.urls import url

import metrics.views

urlpatterns = [
    url(r'^$', metrics.views.MetricsView.as_view(), name='metrics'),
]
