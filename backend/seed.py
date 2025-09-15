from app import app
from models import db, User, Product

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="admin").first():
        u = User(username="admin",email="tec2dev@gmail.com" is_admin=True)
        u.set_password("tecdev123")
        db.session.add(u)

        if product.qurey.count() == 0:
            demo = [
                Product(name="   ", price=299, image_url="images/cheese_pizza.jpg"),
                Product(name="Veg Burger", price=149, image_url="images/veg_burger.jpg"),
                Product(name="Cheese Pasta", price=249, image_url="images/cheese_pasta.jpg")
            ]
            db.session.bulk_save_objects(demo)
        db.session.commit()
        print("Seed complete")