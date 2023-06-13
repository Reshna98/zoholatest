from django.urls import path,include,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from .views import EmailAttachementView, save_data

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('sample/',views.sample,name="sample"),
    path('view_vendor_list/',views.view_vendor_list,name='view_vendor_list'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('sendmail/<int:pk>',views.sendmail,name='sendmail'),
    path('edit_vendor/<int:pk>',views.edit_vendor,name='edit_vendor'),
    path('edit_vendor_details/<int:pk>',views.edit_vendor_details,name='edit_vendor_details'),
    path('upload_document/<int:pk>',views.upload_document,name='upload_document'),
    path('download_doc/<int:pk>',views.download_doc,name='download_doc'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('retainer_invoices/',views.retainer_invoice,name='retainer_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('create_invoice_draft/',views.create_invoice_draft,name='create_invoice_draft'),
    path('create_invoice_send/',views.create_invoice_send,name='create_invoice_send'),
    path('view_invoice/<int:pk>',views.invoice_view,name='invoice_view'),
    path('retainer_template/<int:pk>',views.retainer_template,name='retainer_template'),
    path('retainer_invoice_edit/<int:pk>',views.retainer_edit_page,name='retainer_edit_page'), 
    path('retainer_invoice_update/<int:pk>',views.retainer_update,name='retainer_update'),
    path('send_mail/<int:pk>',views.mail_send,name='mail_send'),
    path('retaineritem_delete/<int:pk>',views.retaineritem_delete,name='retaineritem_delete'),
    path('retainer_delete/<int:pk>',views.retainer_delete,name='retainer_delete'),
    path('allestimates',views.allestimates,name='allestimates'),
    path('newestimate/',views.newestimate,name='newestimate'),
    path('createestimate/',views.createestimate,name='createestimate'),
    path('itemdata_est/',views.itemdata_est,name='itemdata_est'),
    path('create_and_send_estimate/',views.create_and_send_estimate,name='create_and_send_estimate'),
    path('estimateslip/<int:est_id>',views.estimateslip,name='estimateslip'),
    path('editestimate/<int:est_id>',views.editestimate,name='editestimate'),
    path('updateestimate/<int:pk>',views.updateestimate,name='updateestimate'),
    path('converttoinvoice/<int:est_id>',views.converttoinvoice,name='converttoinvoice'),
    path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    path('add_customer_for_estimate/',views.add_customer_for_estimate,name='add_customer_for_estimate'),
    path('entr_custmr_for_estimate/',views.entr_custmr_for_estimate,name='entr_custmr_for_estimate'),
    path('payment_term_for_estimate/',views.payment_term_for_estimate,name='payment_term_for_estimate'),
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    # path('edited/<int:id>',views.edited,name='edited'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('deleteestimate/<int:est_id>',views.deleteestimate,name='deleteestimate'),
    path('additem_est',views.additem_est,name='additem_est'),
    path('additem_page_est',views.additem_page_est,name='additem_page_est'),
    path('add_unit_est',views.add_unit_est,name='add_unit_est'),
    path('add_sales_est',views.add_sales_est,name='add_sales_est'),
    path('add_account_est',views.add_account_est,name='add_account_est'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
    path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice'),
    path('addprice',views.addprice,name='addprice'),
    path('addpl',views.addpl,name='addpl'),
    path('viewpricelist',views.viewpricelist,name='viewpricelist'),
    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('editlist/<int:id>',views.editlist,name='editlist'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('active_status/<int:id>',views.active_status,name='active_status'),
    path('createpl',views.createpl,name='createpl'),
    path('banking_home',views.banking_home,name='banking_home'),
    path('create_banking',views.create_banking,name='create_banking'),
    path('save_banking',views.save_banking,name='save_banking'),
    path('view_bank/<int:id>',views.view_bank,name='view_bank'),
    path('banking_edit/<int:id>',views.banking_edit,name='banking_edit'),
    path('save_edit_bnk/<int:id>',views.save_edit_bnk,name='save_edit_bnk'),
    path('save_banking_edit/<int:id>',views.save_banking_edit,name='save_banking_edit'),
    path('save_bank',views.save_bank,name='save_bank'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('get_customer_names', views.get_customer_names, name='get_customer_names'),
    path('expense/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('get_profile_details/<int:profile_id>/', views.get_profile_details, name='get_profile_details'),
    path('recurringhome',views.recurringhome,name='recurringhome'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('recurringbase',views.recurringbase,name='recurringbase'),
    path('show_recurring/<int:expense_id>/', views.show_recurring, name='show_recurring'),
    path('expense_details', views.expense_details, name='expense_details'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('newexp',views.newexp,name='newexp'),
    path('save-data/', save_data, name='save_data'),
    path('get-account-names/', views.get_account_names, name='get_account_names'),
    path('profileshow',views.profileshow,name='profileshow'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('payment_term',views.payment_term,name='payment_term'),
    ####challan
    path('create_delivery_chellan',views.create_delivery_chellan,name='create_delivery_chellan'),
    path('delivery_chellan_home',views.delivery_chellan_home,name='delivery_chellan_home'),
    path('add_customer_for_challan',views.add_customer_for_challan,name='add_customer_for_challan'),
    path('entr_custmr_for_challan',views.entr_custmr_for_challan,name='entr_custmr_for_challan'),
    path('additem_page_challan',views.additem_page_challan,name='additem_page_challan'),
    path('additem_challan',views.additem_challan,name='additem_challan'), 
    path('delivery_challan_view/<int:id>',views.delivery_challan_view,name='delivery_challan_view'),
    path('delivery_challan_edit/<int:id>',views.delivery_challan_edit,name='delivery_challan_edit'),
    path('update_challan/<int:id>',views.update_challan,name='update_challan'),
    path('create_and_send_challan',views.create_and_send_challan,name='create_and_send_challan'),
    path('create_challan_draft',views.create_challan_draft,name='create_challan_draft'),
    path('get_cust_mail',views.get_cust_mail,name='get_cust_mail'),
    path('additem_edit_challan',views.additem_edit_challan,name='additem_edit_challan'),
    path('additem_challan_edit',views.additem_challan_edit,name='additem_challan_edit'),
    path('add_customer_edit_challan',views.add_customer_edit_challan,name='add_customer_edit_challan'),
    path('sv_cust_edit_challan',views.sv_cust_edit_challan,name='sv_cust_edit_challan'),
    path('add_account_challan_edit',views.add_account_challan_edit,name='add_account_challan_edit'),
    path('add_unit_edit_challan',views.add_unit_edit_challan,name='add_unit_edit_challan'),
    path('add_sales_edit_challan',views.add_sales_edit_challan,name='add_sales_edit_challan'),
    path('payment_term_challan_edit',views.payment_term_challan_edit,name='payment_term_challan_edit'),
    path('payment_term_challan',views.payment_term_challan,name='payment_term_challan'),

    path('add_account_challan',views.add_account_challan,name='add_account_challan'),
    path('add_unit_challan',views.add_unit_challan,name='add_unit_challan'),
    path('add_sales_challan',views.add_sales_challan,name='add_sales_challan'),
    path('render_challan_pdf/<int:id>',views.render_challan_pdf,name='render_challan_pdf'),
    path('deletechallan/<int:id>',views.deletechallan,name='deletechallan'),


    #---------Nithya------Recurring Bills----------------
    path('recurring_bills',views.recurring_bills,name='recurring_bills'),
    path('add_recurring_bills',views.add_recurring_bills,name='add_recurring_bills'),
    path('get_vendordet',views.get_vendordet,name='get_vendordet'),
    path('get_customerdet',views.get_customerdet,name='get_customerdet'),

    path('recurbills_vendor',views.recurbills_vendor,name='recurbills_vendor'),
    path('vendor_dropdown',views.vendor_dropdown,name = 'vendor_dropdown'),

    path('recurbills_pay',views.recurbills_pay,name='recurbills_pay'),
    path('pay_dropdown',views.pay_dropdown,name = 'pay_dropdown'),

    path('recurbills_unit',views.recurbills_unit,name='recurbills_unit'),
    path('unit_dropdown',views.unit_dropdown,name = 'unit_dropdown'),

    path('recurbills_item',views.recurbills_item,name='recurbills_item'),
    path('item_dropdown',views.item_dropdown ,name = 'item_dropdown'),
    path('recurbills_account',views.recurbills_account,name='recurbills_account'),
    path('account_dropdown',views.account_dropdown ,name = 'account_dropdown'),
    path('get_rate',views.get_rate ,name = 'get_rate'),
    path('get_cust_state',views.get_cust_state,name = "get_cust_state"),

    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)