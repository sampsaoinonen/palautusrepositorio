from entities.user import User
import re
import string


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if self._user_repository.find_by_username(username):
                raise UserInputError("Username already used")
        
        if not username or not password:
            raise UserInputError("Username and password are required")
                
        if len(username) < 3:         
            raise UserInputError("Username too short. (Minimum 3 characters)")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username must consist of characters from a to z")
        
        if len(password) < 8:         
            raise UserInputError("Password too short. (Minimum 8 characters)")
        
        if all(char in string.ascii_letters for char in password):
            raise UserInputError("Password must not consist of letters only")

        
