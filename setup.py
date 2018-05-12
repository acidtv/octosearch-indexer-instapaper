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
            'instapaper==0.4',
            # dep required by instapaper lib
            'oauth2>=1.9.0.post1',
            ],
        dependency_links=[
            # this fork from rsgalloway/instapaper has a working python 3 branch
            'git+https://github.com/yusongmen/instapaper.git@issue-6#egg=instapaper-0.4',
            ]
        )
