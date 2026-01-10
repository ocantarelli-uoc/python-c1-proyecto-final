from admin_bp.user_roles.services.create_user_role import create_user_role
from admin_bp.users.services.create_user import create_user
from dotenv import dotenv_values

def create_first_admin_user():
    config_dotenv_values = dotenv_values(".env")
    created_role = create_user_role({'role_name':'admin'})
    created_user = create_user({
        'username':config_dotenv_values['ADMIN_FIRST_APP_USER_USERNAME'],
        'password':config_dotenv_values['ADMIN_FIRST_APP_USER_PASSWORD']
    },'admin')
    return created_user
