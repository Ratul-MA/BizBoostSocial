# p2p_network/urls.py

from django.urls import path
import p2p_network.views

urlpatterns = [
    path('make_transaction/', p2p_network.views.make_transaction, name='make_transaction'),
    path('view_transactions/', p2p_network.views.view_transactions, name='view_transactions'),
]
