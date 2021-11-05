from setuptools import setup, find_packages

setup(
    name="ccknn",
    version="1.5.1",
    description="class-comparable KNN",
    url="https://github.com/celsiustx/bbknn",
    packages=find_packages(exclude=["docs", "figures", "examples"]),
    install_requires=[
        "Cython",
        "numpy",
        "scipy",
        "annoy",
        "pynndescent",
        "umap-learn",
        "scikit-learn",
        "packaging",
    ],
    extras_require=dict(faiss=["faiss"]),
    author="Krzysztof Polanski, Jongeun Park",
    author_email="kp9@sanger.ac.uk",
    license="MIT",
)
