from setuptools import setup, find_packages

setup(
      version="0.3",
      name="divya-blog",
      author="Divya",
      author_email="divya.chandran10@gmail.com",
      description="This is the blog system created by Divya",
      url="https://github.com/blog-divya",
      license="MIT",
      keywords="blog bms",
      requires=[],
      packages=find_packages(),
      entry_points={
            "console_scripts": ['blog=blog.main:main']
      }
)
