import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1" 

repo_name = "Kidney-disease-classification-deeplearning-project"
author_user_name = "rawlin"
src_repo = "cnnclassificatier"
author_email = "rawlin2002@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description="CNN classifier for kidney disease classification.",
    long_description=long_description,
    long_description_content="text/markdown",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)