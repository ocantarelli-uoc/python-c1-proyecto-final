import sys
from dtos.User import User
from dtos.UserRole import UserRole
from exceptions.authorization.ErrorHasOcurredValidatingRoleException import ErrorHasOcurredValidatingRoleException
from exceptions.authorization.UnauthorizedRoleException import UnauthorizedRoleException

#It defines the method for checking if user has required role
def user_has_role(required_roles:list[str],*args, **kwargs):
    try:
        #It gets the authorized_user from kwargs
        user_role = None
        authorized_user : User = kwargs.get('authorized_user')
        #It checks if authorized user (authorized_user) is not None (null)
        if authorized_user is not None:
         #It gets user_role from authorized_user
         user_role : UserRole = authorized_user.user_role
        #It checks if user role (user_role) is None (null) or if its name it isn't on required roles (required_roles)
        if user_role is None or user_role.name not in required_roles:
            #In this case, it throws an unauthorized user role exception (UnauthorizedRoleException)
            raise UnauthorizedRoleException()
    #It captures the unauthorized role exception
    except UnauthorizedRoleException as e_unauthorized_role:
        #It raise the captured exception above (previous classes and/or invoking methods)
        raise e_unauthorized_role
    #It captures generic exception
    except Exception as e:
        print(e.__str__(),file=sys.stderr)
        print(e.__repr__(),file=sys.stderr)
        #It raise the validating role exception above (previous classes and/or invoking methods)
        raise ErrorHasOcurredValidatingRoleException()