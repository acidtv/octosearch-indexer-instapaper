from setuptools import setup

setup(
        name='octosearch-indexer-instapaper',
        # packages=find_packages(),
        entry_points={
            'octosearch.indexer': [
                'instapaper = indexer:Indexer',
                ],
            },
        install_requires=[
            'octosearch',
            'instapaper',
            # dep required by instapaper lib
            'oauth2>=1.9.0.post1',
            ]
        )
