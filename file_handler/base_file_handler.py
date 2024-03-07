from abc import ABC, abstractmethod

class BaseFileHandler(ABC):

    @abstractmethod
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def get_vacancies(self, data):
        pass

    @abstractmethod
    def delete_all_vacancy(self):
        pass
