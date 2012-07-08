from setuptools import setup, find_packages

version = __import__('cmsplugin_randomquote').__version__

setup(
    name = 'cmsplugin-randomquote',
    version = version,
    description = 'Random quote plugin for the django CMS.',
    author = 'Danilo Bargen',
    author_email = 'gezuru@gmail.com',
    url = 'http://github.com/gwrtheyrn/cmsplugin-randomquote',
    license='MIT',
    keywords='django django-cms cms plugin quotes testimonials',
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-cms>=2.1',
        'django>=1.2',
    ]
)
