from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,phone_number,email,full_name,password):
        if not phone_number:
            raise ValueError('user must have phone_number')
        
        if not full_name:
            raise ValueError('user must have full_name')
        
        user=self.model(phone_number=phone_number,full_name=full_name)
        user.set_password(password)
        user.save()

    def create_superuser(self,phone_number,email,full_name,password):
        user=self.create_user(phone_number=phone_number,full_name=full_name)
        user.is_admin=True
        user.save(using=self._db)
        return user
        