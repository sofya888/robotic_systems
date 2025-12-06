from setuptools import setup

package_name = 'ros_ai_assistant'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/assistant.launch.py']),
    ],
    install_requires=[
        'setuptools',
        'aiohttp',
        'flask',
        'flask-restful',
    ],
    zip_safe=True,
    maintainer='sofus',
    maintainer_email='sofushka.2004@mail.ru',
    description='ROS 2 AI assistant with OpenAI integration',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'openai_integration = ros_ai_assistant.openai_integration:main',
            'api_gateway = ros_ai_assistant.api_gateway:main',
        ],
    },
)
