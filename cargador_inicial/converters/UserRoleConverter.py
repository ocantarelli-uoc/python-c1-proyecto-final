from cargador_inicial.converters.Converter import Converter
from cargador_inicial.dtos.UserRole import UserRole


class UserRoleConverter(Converter):
  #method that its responsibility it's to convert a dataframe of user roles to list of UserRole class objects (instances)
     def convert(self,dataFrame) -> list:
        user_roles = []
        for row in dataFrame.itertuples():
            user_role = UserRole(
                id_user_role=None,
                name=row.name
            )
            user_roles.append(user_role)
        return user_roles