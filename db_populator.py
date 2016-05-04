from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

engine = create_engine('sqlite:///babystuff.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#Create dummy user
User1 = User(name="Admin_User", email="tinnyTim@udacity.com",
             picture='http://imgfave-herokuapp-com.global.ssl.fastly.net/image_cache/1329360868344111.jpg')
session.add(User1)
session.commit()


# Items for category baby food
category1 = Category(user_id=1, name="Baby Food")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Banana Porridge", description="Organic deliciouse banana Porridge",
                     price="1.50", category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Carrot puree", description="Yummy and smooth carrot puree",
                     price="2.00", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Chicken casserole thick puree", description="Yummy mix of organic vegetable and chicken puree",
                     price="2.00", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Fish pie thick puree", description="Yummy mix of organic vegetable and fish puree",
                     price="2.00", category=category1)

session.add(item4)
session.commit()


# Items for category baby clothes
category2 = Category(user_id=1, name="Baby Clothes")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Sweater", description="Cute white baby sweater with clowns",
                     price="6.50", category=category2)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Baby Jeans", description="Cozy blue jeans for active babies",
                     price="12.50", category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="T-shirt", description="White T-shirt with little teddy bears",
                     price="10.50", category=category2)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Sleepsuit", description="Yellow Sleepsuit with little stars",
                     price="6.50", category=category2)
session.add(item4)
session.commit()


# Items for baby shoes
category3 = Category(user_id=1, name="Baby Shoes")

session.add(category3)
session.commit()


item1 = Item(user_id=1, name="Baby Boots", description="Yellow boots for jumping in muddy puddles!",
                     price="8.50", category=category3)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Baby slippers", description="Comfortable and soft baby slippers",
                     price="10.00", category=category3)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Baby ballerina flats", description="Lovely pinkballerina flats for fashion girls",
                     price="15.00", category=category3)
session.add(item3)
session.commit()


# Items for baby toys
category4 = Category(user_id=1, name="Baby Toys")

session.add(category4)
session.commit()



item1 = Item(user_id=1, name="Doll", description="Lovely rag doll with blue eyes and pink clothes",
                     price="13.50", category=category4)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Dinosuar", description="Sacring green plastic dinosaur for brave boys",
                     price="8.50", category=category4)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Stuffed animal", description="Cute white stuffed kitten",
                     price="12.50", category=category4)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Toy construction blocks", description="100 colourful funny constraction blocks",
                     price="15.50", category=category4)
session.add(item4)
session.commit()

#Items for Baby books
category5 = Category(user_id=1, name="Baby Books ")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Peppa pig's adeventure", description="Peppa and her friends go to camping site",
                     price="8.50", category=category5)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Mog the cat", description="The story of a muddler cat that becomes a hero by chance",
                     price="12.00", category=category5)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="I don't want to go to bad", description="The story of a little tiger that doesn't want to sleep",
                     price="7.50", category=category5)
session.add(item3)
session.commit()



# Items for Buggies
category6 = Category(user_id=1, name="Buggies")

session.add(category6)
session.commit()

item1 = Item(user_id=1, name="Twin stroller", description="Buggy that allow to carry two children without wasting space",
                     price="200.00", category=category6)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Three wheels", description="Three wheels buggy, really maneuvrable",
                     price="150.00", category=category6)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Four wheels", description="Four wheels buggy, really solid",
                     price="130.00", category=category6)
session.add(item3)
session.commit()

print "added items!"