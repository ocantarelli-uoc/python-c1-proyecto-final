from converters.Converter import Converter
from models.UserRole import UserRole


class UserRoleConverter(Converter):
  #method that its responsibility it's to convert a dataframe of user roles to list of UserRole class objects (instances)
     def convert(self,dataFrame) -> list:
        user_roles = []
        for row in dataFrame.itertuples():
            if row.entity_type == "user_role":
                user_role = UserRole(
                    id_user_role=None,
                    name=row.role_name
                )
                user_roles.append(user_role)
        return user_roles