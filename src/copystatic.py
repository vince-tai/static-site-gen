import os
import shutil

def copy(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    src_items = os.listdir(src)
    for item in src_items:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
        else:
            dst_dir_path = os.path.join(dst, item)
            copy(item_path, dst_dir_path)