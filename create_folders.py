<<<<<<< HEAD
import os

def create_project_structure():
    # تحديد المسارات
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = [
        'static',
        'static/images',
        'static/css',
        'static/uploads',
        'templates',
        'instance'
    ]
    
    # إنشاء المجلدات
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✅ تم إنشاء مجلد: {folder}")
        else:
            print(f"ℹ️ المجلد موجود: {folder}")

if __name__ == '__main__':
    create_project_structure()
=======
import os

def create_project_structure():
    # تحديد المسارات
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = [
        'static',
        'static/images',
        'static/css',
        'static/uploads',
        'templates',
        'instance'
    ]
    
    # إنشاء المجلدات
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✅ تم إنشاء مجلد: {folder}")
        else:
            print(f"ℹ️ المجلد موجود: {folder}")

if __name__ == '__main__':
    create_project_structure()
>>>>>>> a7cdc5c4d3159e24e80dc8157e670c03bb65388e
