# persistence/alchemy_models.py
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
class Person(Base):
 __tablename__ = 'person'
 id = Column(Integer, primary_key=True)
 name = Column(String)
 age = Column(Integer)
 addresses = relationship(
 'Address',
 back_populates='person',
 order_by='Address.email',
 cascade='all, delete-orphan'
 )
 def __repr__(self):
    return f'{self.name}(id={self.id})'
class Address(Base):
 __tablename__ = 'address'
 id = Column(Integer, primary_key=True)
 email = Column(String)
 person_id = Column(ForeignKey('person.id'))
 person = relationship('Person', back_populates='addresses')
 def __str__(self):
    return self.email
 __repr__ = __str__
Base.metadata.create_all(engine)