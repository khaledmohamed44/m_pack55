<<<<<<< HEAD
import os
from app import app, db, User, Settings

def init_database():
    print("⚙️ جاري إنشاء قاعدة البيانات...")
    
    with app.app_context():
        print("↻ حذف الجداول القديمة...")
        db.drop_all()
        
        print("⚡ إنشاء جداول جديدة...")
        db.create_all()
        
        # إنشاء الإعدادات الافتراضية
        print("⚙️ إنشاء الإعدادات الافتراضية...")
        settings = Settings(
            background_image='/static/images/default-background.jpg',
            primary_color='#139694',
            secondary_color='#ffffff',
            accent_color='#ff0000',
            text_color='#333333',
            header_text='شركة عالم البلاستك',
            header_description='نقدم أفضل المنتجات البلاستيكية والورقية بجودة عالية',
            phone1='+96556502009',
            phone2='+96550781493',
            whatsapp='+96556502009',
            email='info@example.com',
            address='الشويخ الصناعية/شارع التمور/شارع 79',
            location_url='https://maps.app.goo.gl/188HQpp',
            facebook_url='https://facebook.com/yourpage',
            instagram_url='https://instagram.com/yourpage',
            twitter_url='https://twitter.com/yourpage',
            about_title='من نحن',
            about_description='شركة عالم البلاستك هي شركة رائدة في مجال توريد المنتجات البلاستيكية والورقية في الكويت',
            about_services='توريد منتجات بلاستيكية عالية الجودة\nتوفير منتجات ورقية متنوعة\nخدمة توصيل سريعة وموثوقة\nأسعار تنافسية'
        )
        db.session.add(settings)
        
        # إنشاء حساب المسؤول
        print("👤 إنشاء حساب المسؤول...")
        admin = User(
            username='admin',
            password='admin123',
            is_admin=True
        )
        db.session.add(admin)
        
        try:
            db.session.commit()
            print("\n✅ تم إنشاء قاعدة البيانات بنجاح!")
            print("✅ تم إنشاء حساب المسؤول:")
            print("   - اسم المستخدم: admin")
            print("   - كلمة المرور: admin123")
        except Exception as e:
            print(f"❌ حدث خطأ: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    init_database()
=======
import os
from app import app, db, User, Settings

def init_database():
    print("⚙️ جاري إنشاء قاعدة البيانات...")
    
    with app.app_context():
        print("↻ حذف الجداول القديمة...")
        db.drop_all()
        
        print("⚡ إنشاء جداول جديدة...")
        db.create_all()
        
        # إنشاء الإعدادات الافتراضية
        print("⚙️ إنشاء الإعدادات الافتراضية...")
        settings = Settings(
            background_image='/static/images/default-background.jpg',
            primary_color='#139694',
            secondary_color='#ffffff',
            accent_color='#ff0000',
            text_color='#333333',
            header_text='شركة عالم البلاستك',
            header_description='نقدم أفضل المنتجات البلاستيكية والورقية بجودة عالية',
            phone1='+96556502009',
            phone2='+96550781493',
            whatsapp='+96556502009',
            email='info@example.com',
            address='الشويخ الصناعية/شارع التمور/شارع 79',
            location_url='https://maps.app.goo.gl/188HQpp',
            facebook_url='https://facebook.com/yourpage',
            instagram_url='https://instagram.com/yourpage',
            twitter_url='https://twitter.com/yourpage',
            about_title='من نحن',
            about_description='شركة عالم البلاستك هي شركة رائدة في مجال توريد المنتجات البلاستيكية والورقية في الكويت',
            about_services='توريد منتجات بلاستيكية عالية الجودة\nتوفير منتجات ورقية متنوعة\nخدمة توصيل سريعة وموثوقة\nأسعار تنافسية'
        )
        db.session.add(settings)
        
        # إنشاء حساب المسؤول
        print("👤 إنشاء حساب المسؤول...")
        admin = User(
            username='admin',
            password='admin123',
            is_admin=True
        )
        db.session.add(admin)
        
        try:
            db.session.commit()
            print("\n✅ تم إنشاء قاعدة البيانات بنجاح!")
            print("✅ تم إنشاء حساب المسؤول:")
            print("   - اسم المستخدم: admin")
            print("   - كلمة المرور: admin123")
        except Exception as e:
            print(f"❌ حدث خطأ: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    init_database()
>>>>>>> a7cdc5c4d3159e24e80dc8157e670c03bb65388e
