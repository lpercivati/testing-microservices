from repositories import userRepository

class UserService:
    def __init__(self, userRepository: userRepository.UserRepository) -> None:
        self.userRepository = userRepository

    def get_users(self):
        return self.userRepository.get_all()

    def create_user(self, name, email):
        self.userRepository.create(name, email.strip())

    def delete_by_name(self, name: str) -> bool:
        self.userRepository.delete_by_name(name)