from setuptools import setup, find_packages

VERSION = '0.0.1' 
# DESCRIPTION = 'My first Python package'
# LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# 配置
setup(
       # 名称必须匹配文件名 'verysimplemodule'
        name="lib", 
        version=VERSION,
        author="Jason Dsouza",
        author_email="<youremail@email.com>",
        # description=DESCRIPTION,
        # long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        # install_requires=[], # add any additional packages that 
        # 需要和你的包一起安装，例如：'caer'
        
        keywords=['python'],
        # classifiers= [
        #     "Development Status :: 3 - Alpha",
        #     "Intended Audience :: Education",
        #     "Programming Language :: Python :: 2",
        #     "Programming Language :: Python :: 3",
        #     "Operating System :: MacOS :: MacOS X",
        #     "Operating System :: Microsoft :: Windows",
        # ]
)