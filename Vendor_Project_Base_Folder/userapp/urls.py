from django.urls import path
from userapp import views


urlpatterns = [

    path('', views.home, name='home'),
    path('register', views.Register, name='reg'),
    path('login',views.LoginFunction,name='login'),
    path('logout',views.Logout_Function,name='logout'),
    path('createven',views.Create_vendor,name='createven'),
    path('add_vendor/', views.add_vendor, name='add_vendor'),
    path('vendortable',views.vendor_table,name='vntb'),
    path('delete_vendor/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    path('edit_vendor/<int:vendor_id>/',views.edit_vendor,name='edit_vendor'),
    path('editven/<int:id>/',views.EditingVendor,name='editven'),
    path('transactions/',views.vendor_transactions_api,name='excel'),
    path('addtransaction',views.AddingTransaction,name='addtran'),
    path('addtrans',views.AddTransaction,name='addtransacction'),
]
