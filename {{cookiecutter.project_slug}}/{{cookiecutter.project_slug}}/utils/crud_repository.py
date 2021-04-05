from fastapi.encoders import jsonable_encoder
from {{cookiecutter.project_slug}}.utils.repositories import BaseRepository


class CRUDBRepository(BaseRepository):
    model = None

    def get(self, id):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, skip=0, limit=100):
        return self.session.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def update(self, db_obj, obj_in):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def remove(self, id):
        obj = self.session.query(self.model).get(id)
        self.session.delete(obj)
        self.session.commit()
        return obj
