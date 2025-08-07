from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database.database import Base, SessionLocal
import datetime

class TaskItem(Base):
    __tablename__ = "taskitens"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    finished = Column(Boolean, nullable=False, default=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    deadline = Column(DateTime, nullable=True)
    
class TaskItem_Repo:
    def __init__(self):
        self.session = SessionLocal()
    
    def add(self,description:str,deadline:datetime.datetime = None):
        new_task = TaskItem(description=description,deadline=deadline)
        self.session.add(new_task)
        self.session.commit()
        self.session.refresh(new_task)
        return new_task
    
    def get_all(self):
        return self.session.query(TaskItem).all()
    
    def get_by_id(self, task_id:int):
        return self.session.query(TaskItem).filter(TaskItem.id == task_id).first()
    
    def update(self, task_id:int, description:str = None, finished:bool=None,deadline:datetime.datetime=None):
        task = self.get_by_id(task_id)
        
        if not task_id : return None
        
        if description is not None: task.description = description
        
        if finished is not None : task.finished = finished
        
        if deadline is not None : task.deadline = deadline
        
        self.session.commit()
        self.session.refresh(task)
        return task
        
    def delete(self,task_id:int):
        task = self.get_by_id(task_id)
        if not task : return False
        self.session.delete(task)
        self.session.commit()
        return True
    
    def close(self):
        self.session.close()
        