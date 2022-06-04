from rest_framework.authentication import TokenAuthentication



class ExpiringTokenAuthentication(TokenAuthentication):
    
    def authenticate_crendentials(self,key):
        message,token,user = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido.'
            
        if token is not None:
            message = 'Este usuario ha sido eliminado'
            
        return (user,token,message)