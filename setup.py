# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='ddy',
    author_email='duan_danyang@163.com',
    url='https://www.the5fire.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    #package_data={'': [    # 打包数据文件，方法一
    #  'themes/*/*/*/*',  # 需要按目录层级匹配
    #]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'appnope==0.1.0',
        'autopep8==1.4.4',
        'backcall==0.1.0',
        'backports.csv==1.0.7',
        'certifi==2019.6.16',
        'chardet==3.0.4',
        'coreapi==2.3.3',
        'coreschema==0.0.4',
        'Cython==0.29.12',
        'decorator==4.4.0',
        'defusedxml==0.6.0',
        'diff-match-patch==20181111',
        'Django==1.11.28',
        'django-autocomplete-light==3.2.10',
        'django-ckeditor==5.4.0',
        'django-crispy-forms==1.7.2',
        'django-debug-toolbar==1.9.1',
        'django-formtools==2.1',
        'django-import-export==1.2.0',
        'django-js-asset==1.2.2',
        'django-redis==4.9.0',
        'django-rest-framework==0.1.0',
        'django-reversion==3.0.4',
        'django-silk==3.0.0',
        'djangorestframework==3.9.4',
        'djdt-flamegraph==0.2.12',
        'et-xmlfile==1.0.1',
        'future==0.17.1',
        'gprof2dot==2016.10.13',
        'hiredis==0.2.0',
        'httplib2==0.9.2',
        'idna==2.8',
        'ipython==7.6.1',
        'ipython-genutils==0.2.0',
        'itypes==1.1.0',
        'jdcal==1.4.1',
        'jedi==0.14.0',
        'Jinja2==2.10.1',
        'MarkupSafe==1.1.1',
        'mistune==0.8.4',
        'odfpy==1.4.0',
        'openpyxl==2.6.2',
        'parso==0.5.0',
        'pexpect==4.7.0',
        'pickleshare==0.7.5',
        'Pillow==9.0.1',
        'prompt-toolkit==2.0.9',
        'ptyprocess==0.6.0',
        'pycodestyle==2.5.0',
        'Pygments==2.4.2',
        'Pympler==0.5',
        'PyMySQL==0.9.3',
        'python-dateutil==2.8.0',
        'pytz==2019.1',
        'PyYAML==5.1.1',
        'redis==3.2.1',
        'requests==2.22.0',
        'six==1.12.0',
        'sqlparse==0.3.0',
        'tablib==0.13.0',
        'traitlets==4.3.2',
        'uritemplate==3.0.0',
        'urllib3==1.25.3',
        'wcwidth==0.1.7',
        'xadmin==0.6.1',
        'xlrd==1.2.0',
        'xlwt==1.3.0',
    ],
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

)
