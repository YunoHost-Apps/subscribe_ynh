# -*- coding: utf-8 -*-

""" License

    Copyright (C) 2014 YUNOHOST.ORG

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program; if not, see http://www.gnu.org/licenses

"""

""" yunohost_subscription.py

    Manage subscriptions
"""
import os
import sys
import crypt
import random
import string
import json
import errno
import MySQLdb

from moulinette.core import MoulinetteError


def subscription_test():
	return { 'subscriptions' : 'ok' }
	
	
def subscription_list(auth, fields=None, limit=None, offset=None):
    """
    List subscriptions

    Keyword argument:
        offset -- Starting number for user fetching
        limit -- Maximum number of user fetched
        fields -- fields to fetch

    """
    user_attrs = [ 'username','firstname','lastname','mail',
                   'password']
    attrs = ""
    result_list = []

    if offset is None:
        offset = 0
    if limit is None:
        limit = 1000
    if fields:
        if any(attr not in user_attrs for attr in fields) :
            raise MoulinetteError(errno.EINVAL,
                                      m18n.n('field_invalid', attr))
        attrs=fields.join(",")
    else:
        attrs = "username, firstname, lastname, mail"
            
         
    cur = _get_db() 
    
    cur.execute("SELECT "+attrs+" FROM prefix_subscriptions LIMIT %d,%d",
        [offset,limit])

    for row in cur.fetchall() :
        result_list.append({
        'username': row[0],
        'firstname': row[1],
        'lastname': row[2],
        'mail': row[3]})

    return { 'subscriptions' : result_list }

def subscription_create(username, firstname, lastname, mail, password):
    """
    Create subscription

    Keyword argument:
        firstname
        lastname
        username -- Must be unique
        mail -- Main mail address must be unique
        password

    """
    import pwd
    from yunohost.domain import domain_list
    from yunohost.hook import hook_callback
    from yunohost.app import app_ssowatconf


    # Validate uniqueness of username in system users
    try:
        pwd.getpwnam(username)
    except KeyError:
        pass
    else:
        raise MoulinetteError(errno.EEXIST, m18n.n('system_username_exists'))

    # Check that the mail domain exists
    #~ if mail[mail.find('@')+1:] not in domain_list(auth)['domains']:
        #~ raise MoulinetteError(errno.EINVAL,
                              #~ m18n.n('mail_domain_unknown',
                                     #~ mail[mail.find('@')+1:]))

    char_set = string.ascii_uppercase + string.digits
    salt = ''.join(random.sample(char_set,8))
    salt = '$1$' + salt + '$'
    pwd = '{CRYPT}' + crypt.crypt(str(password), salt)
    
    cur = _get_db() 
    
    try:
        cur.execute("INSERT INTO prefix_subscriptions VALUES (%s,%s,%s,%s,%s)",
            [username,firstname,lastname,mail,pwd])
    

    if True: 
        msignals.display(m18n.n('subscription_created'), 'success')
        hook_callback('post_subscription_create', [username, mail, password, firstname, lastname])
        return { 'firstname' : firstname,
                'lastname':lastname, 
                'username' : username, 
                'mail' : mail }

    raise MoulinetteError(169, m18n.n('subscription_creation_failed'))
    
    
def subscription_valid(auth, username):
    """
    Valid a subscription

    Keyword argument:
        username -- Must be unique

    """
    from yunohost.user import user_create
    from yunohost.domain import domain_list
    from yunohost.app import app_ssowatconf
    
    info=subscription_info(auth, username)
    user_create(auth, info['username'], info['firstname'], info['lastname'], info['mail'], info['password'])
    
    #Update password
    new_attr_dict = {'userPassword':info['password']}  

    if auth.update('uid=%s,ou=users' % username, new_attr_dict):
       app_ssowatconf(auth)
    else:
       raise MoulinetteError(169, m18n.n('user_creation_failed'))
    
    #Remove subscription from database
    cur = _get_db()     
    cur.execute("DELETE FROM prefix_subscriptions WHERE `username`=%s",[username])

def subscription_delete(auth, username):
    """
    Delete subscription

    Keyword argument:
        username -- Username to delete

    """
    
    cur = _get_db() 
    
    cur.execute("DELETE FROM prefix_subscriptions WHERE `username`=%s",[username])
    
    if False:
        raise MoulinetteError(169, m18n.n('subscription_deletion_failed'))

    msignals.display(m18n.n('subscription_deleted'), 'success')

def subscription_info(auth, username):
    """
    Get subscription informations

    Keyword argument:
        username -- Username or mail to get informations

    """
    
    cur = _get_db() 
    
    cur.execute("SELECT * FROM prefix_subscriptions WHERE `username`=%s",[username])
    row = cur.fetchone()

    if row is None:
        raise MoulinetteError(errno.EINVAL, m18n.n('subscription_unknown'))

    result_dict = {
        'username': row[0],
        'firstname': row[1],
        'lastname': row[2],
        'mail': row[3],
        'password': row[4]
    }

    return result_dict
        
        
def _get_db():

    mysql_root_pwd = open('/etc/yunohost/mysql').read().rstrip()
    db = MySQLdb.connect(host="localhost", user="root",
        passwd=mysql_root_pwd, 
        db="subscribe")
         
    return  db.cursor() 
    
