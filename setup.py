"""
EveryFlip Atlanta LLC - Setup
By Ouwen Zhu
"""

from setuptools import setup

APP=['DropPay.py']
OPTIONS={
  'argv_emulation': True,
  'packages':['certifi'],
}

setup(
  app=APP,
  options={'py2app':OPTIONS},
  setup_requires=['py2app'],
)
