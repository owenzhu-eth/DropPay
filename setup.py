"""
Book of Resell - Setup
By OwenZhu78#0001
"""

from setuptools import setup

APP=['DropPay.py']
OPTIONS={
  'argv_emulation': True,
}

setup(
  app=APP,
  options={'py2app':OPTIONS},
  setup_requires=['py2app']
)
