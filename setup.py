from setuptools import setup, find_packages

setup(
    name='Department App',
    version='1.0',
    author='Mykyta Komarov',
    author_email='nikita6kom@gmail.com',
    description='Web application for managing departments and employees',
    url='https://github.com/R0ixy/epam_project',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.2',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-RESTful==0.3.9',
        'Flask-Migrate==3.1.0',
        'Flask-Login==0.5.0',
        'PyMySQL==1.0.2',
        'Werkzeug==2.0.2',
        'cryptography==36.0.0',
        'python-dotenv==0.19.2',
    ]
)
