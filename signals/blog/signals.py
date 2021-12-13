from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,pre_init,post_init,pre_delete,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in,sender=User)#decorator method used to connect signal
def login_success(sender,request,user,**kwargs):
    print("---------------------------------------")
    print("Logged_in signal...")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)#decorator method used to connect signal
def log_out(sender,request,user,**kwargs):
    print("---------------------------------------")
    print("Logged_out signal...")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# user_logged_out.connect(log_out,sender=User)



@receiver(user_login_failed)#decorator method used to connect signal
def login_failed(sender,credentials,request,**kwargs):
    print("---------------------------------------")
    print("user_login_failed signal...")
    print("Sender:",sender)
    print("Request:",request)
    print("Credentials:",credentials)
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# user_login_failed.connect(login_failed)


#----------------------------------------------------------------------------------------------------------------
# built in model signals

@receiver(pre_save,sender=User)#decorator method used to connect signal
def at_beginning_save(sender,instance,**kwargs):
    print("---------------------------------------")
    print("Pre_save signal...")
    print("Sender:",sender)
    print("Instance:",instance)    
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# pre_save.connect(at_beginning_save,sender=User)

@receiver(post_save,sender=User)#decorator method used to connect signal
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("---------------------------------------")
        print('New Record')
        print("Post_save signal...")
        print("Sender:",sender)
        print("Created:",created)
        print("Instance:",instance)    
        print(f'kwargd:{kwargs}')
    else:
        print("---------------------------------------")
        print('Update Record')
        print("Post_save signal...")
        print("Sender:",sender)
        print("Created:",created)
        print("Instance:",instance)    
        print(f'kwargd:{kwargs}')


# manual route method to connect signal
# post_save.connect(at_ending_save,sender=User)

#-------------------------------------------------------------------------------------------------------------------

@receiver(pre_delete,sender=User)#decorator method used to connect signal
def at_beginning_delete(sender,instance,**kwargs):
    print("---------------------------------------")
    print("Pre_delete signal...")
    print("Sender:",sender)
    print("Instance:",instance)    
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# pre_delete.connect(at_beginning_delete,sender=User)


@receiver(post_delete,sender=User)#decorator method used to connect signal
def at_ending_delete(sender,instance,**kwargs):
    print("---------------------------------------")
    print("Post_delete signal...")
    print("Sender:",sender)
    print("Instance:",instance)    
    print(f'kwargd:{kwargs}')

# manual route method to connect signal
# post_delete.connect(at_ending_delete,sender=User)


#---------------------------------------------------------------------------------------------------------------
@receiver(pre_init,sender=User)#decorator method used to connect signal
def at_begining_init(sender,*args,**kwargs):
    print("---------------------------------------")
    print("Pre_init signal...")
    print("Sender:",sender)
    print(f'args:{args}')    
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# pre_init.connect(at_begining_init,sender=User)


@receiver(post_init,sender=User)#decorator method used to connect signal
def at_ending_init(sender,*args,**kwargs):
    print("---------------------------------------")
    print("Post_init signal...")
    print("Sender:",sender)
    print(f'args:{args}')    
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# post_init.connect(at_ending_init,sender=User)

#-----------------------------------------------------------------------------------------------------------
@receiver(request_started)#decorator method used to connect signal
def at_begining_request(sender,environ,**kwargs):
    print("---------------------------------------")
    print("At begining signal...")
    print("Sender:",sender)
    print("Environ:",environ)    
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# request_started.connect(at_begining_request)

@receiver(request_finished)#decorator method used to connect signal
def at_ending_request(sender,**kwargs):
    print("---------------------------------------")
    print("At Ending signal...")
    print("Sender:",sender)  
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# request_finished.connect(at_ending_request)


@receiver(got_request_exception)#decorator method used to connect signal
def at_req_exception(sender,request,**kwargs):
    print("---------------------------------------")
    print("At Request Exception signal...")
    print("Sender:",sender)  
    print("Request:",request)  
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# got_request_exception.connect(at_req_exception)



#-------------------------------------------------------------------------------------------------------------

@receiver(pre_migrate)
def  before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("---------------------------------------")
    print("Before Install App signal...")
    print("sender:",sender)
    print("App_config:",app_config)
    print("Verbosity:",verbosity)
    print("Interactive:",interactive)
    print("Using:",using)
    print("Plan:",plan)
    print("Apps:",apps)
    print(f'kwargs:{kwargs}')
# manual route method to connect signal
# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def  after_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("---------------------------------------")
    print("After Install App signal...")
    print("sender:",sender)
    print("App_config:",app_config)
    print("Verbosity:",verbosity)
    print("Interactive:",interactive)
    print("Using:",using)
    print("Plan:",plan)
    print("Apps:",apps)
    print(f'kwargs:{kwargs}')
# manual route method to connect signal
# post_migrate.connect(after_install_app)
#------------------------------------------------------------------------------------------------------

@receiver(connection_created)#decorator method used to connect signal
def conn_db(sender,connection,**kwargs):
    print("---------------------------------------")
    print("Initial Connection to DB.....")
    print("Sender:",sender)  
    print("Connection:",connection)  
    print(f'kwargs:{kwargs}')

# manual route method to connect signal
# connection_created.connect(conn_db)