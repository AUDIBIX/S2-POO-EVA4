from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from repositories.base_repository import BaseRepository

T = TypeVar('T')

class BaseService(ABC, Generic[T]):
    def __init__(self, repository: BaseRepository):
        self._repository = repository
    
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[dict]:
        pass 