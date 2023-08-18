"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None
        no_of_user = 0

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Args: email and password
           Return: User
        """
        user = User(email=email, hashed_password=hashed_password)
        db._session.add(user)
        db._session.commit()
        return user

    def find_user_by(self, **kwargs):
        fields = ['id',' email', 'hashed_password', 'session_id', 'reset_token']

        for field in kwargs.fields:
            if field not in fields:
                raise InvalidRequestError
            result =self._session.query(User).filter_by(**kwargs).first()
            if result is None:
                raise NoResultFound
        return result

    def update_user(self, user_id: int **kwargs) -> None:
        """Use find_user_by to locate the user to update
        Update user's attribute as passed in methods argument
        Commit changes to database
        Raises ValueError if argument does not correspond to user
        attribute passed
        """
        user_to_update = self.find_user_by(id=user_id)
        user_keys = ['id', 'email', 'hashed_password', 'session_id',
                     'reset_token']
        for key, value in kwargs.items():
            if key in user_keys:
                setattr(user_to_update, key, value)
            else:
                raise ValueError
        self._session.commit()


