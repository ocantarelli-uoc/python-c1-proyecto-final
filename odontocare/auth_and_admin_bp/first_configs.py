from admin_bp.user_roles.services.create_user_role import create_user_role
from admin_bp.users.services.create_user import create_user
from dotenv import dotenv_values
from admin_bp.user_roles.enums.UserRoleEnum import UserRoleEnum
#It defines method for creating first admin user
def create_first_admin_user():
    #It reads value from .env configuration file
    config_dotenv_values = dotenv_values(".env")
    #It creates the user role admin
    created_role = create_user_role({'role_name':'admin'})
    #It creates the first admin user
    created_user = create_user({
        'username':config_dotenv_values['ADMIN_FIRST_APP_USER_USERNAME'],
        'password':config_dotenv_values['ADMIN_FIRST_APP_USER_PASSWORD']
    },UserRoleEnum.ADMIN.value)
    #It returns the created user
    return created_user
