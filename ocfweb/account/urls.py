from django.conf.urls import url

from ocfweb.account.chpass import change_password
from ocfweb.account.commands import commands
from ocfweb.account.register import account_created
from ocfweb.account.register import account_pending
from ocfweb.account.register import request_account
from ocfweb.account.register import wait_for_account
from ocfweb.account.vhost import request_vhost
from ocfweb.account.vhost import request_vhost_success
from ocfweb.account.vhost_mail import vhost_mail
from ocfweb.account.vhost_mail import vhost_mail_add_address
from ocfweb.account.vhost_mail import vhost_mail_edit_forward_to
from ocfweb.account.vhost_mail import vhost_mail_remove_address
from ocfweb.account.vhost_mail import vhost_mail_update_password


urlpatterns = [
    url(r'^password/$', change_password, name='change_password'),
    url(r'^commands/$', commands, name='commands'),

    # account creation
    url(r'^register/$', request_account, name='register'),
    url(r'^register/wait/$', wait_for_account, name='wait_for_account'),
    url(r'^register/created/$', account_created, name='account_created'),
    url(r'^register/pending/$', account_pending, name='account_pending'),

    # request vhost
    url(r'^vhost/$', request_vhost, name='request_vhost'),
    url(r'^vhost/success/$', request_vhost_success, name='request_vhost_success'),

    # mail vhost management
    url(r'^vhost/mail/$', vhost_mail, name='vhost_mail'),
    url(r'^vhost/mail/add_address/$', vhost_mail_add_address, name='vhost_mail_add_address'),
    url(r'^vhost/mail/remove_address/$', vhost_mail_remove_address, name='vhost_mail_remove_address'),
    url(r'^vhost/mail/update_password/$', vhost_mail_update_password, name='vhost_mail_update_password'),
    url(r'^vhost/mail/edit_forward_to/$', vhost_mail_edit_forward_to, name='vhost_mail_edit_forward_to'),
]
