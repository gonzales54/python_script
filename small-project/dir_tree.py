import os

root_dir = os.path.abspath(os.path.dirname(__file__))
for root, dirs, files in os.walk(root_dir):
    print(root)
