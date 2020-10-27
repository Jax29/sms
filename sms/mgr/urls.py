from django.urls import path
from . import customer, login_in_out, medicine, order


urlpatterns = [
    path('customers', customer.dispatcher),
    path('medicines', medicine.dispatcher),
    path('orders', order.dispatcher),

    path('signin', login_in_out.signin),
    path('signout', login_in_out.signout),

]
