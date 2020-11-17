from django.conf.urls import url

import fatpercentage.views

urlpatterns = [
    url(r'^$', fatpercentage.views.FatpercentageView.as_view(), name='new_fatpercentage'),
]