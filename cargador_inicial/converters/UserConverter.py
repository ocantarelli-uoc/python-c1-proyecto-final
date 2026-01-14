from cargador_inicial.converters.Converter import Converter
from cargador_inicial.dtos.User import User
from cargador_inicial.dtos.UserRole import UserRole


class UserConverter(Converter):
  #method that its responsibility it's to convert a dataframe of users to list of User class objects (instances)
  def convert(self,dataFrame) -> list:
    users = []
    for row in dataFrame.itertuples():
      if row.entity_type == "user":
        user = User(id_user=None,username=row.username,password=row.password,
                      user_role=UserRole(id_user_role=None,name=row.user_role))
        users.append(user)
    return users