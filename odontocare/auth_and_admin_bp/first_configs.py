from admin_bp.user_roles.services.create_user_role import create_user_role
from admin_bp.users.services.create_user import create_user

def create_first_admin_user():
    created_role = create_user_role({'role_name':'admin'})
    created_user = create_user({
        'username':'admin',
        'password':'test2xa'
    },'admin')
    return created_user
