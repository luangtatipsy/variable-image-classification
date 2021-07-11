import os
import shutil

base_dir = "datasets/iris-computer-vision"
directories = [
    class_dir
    for class_dir in os.listdir(base_dir)
    if not class_dir.startswith(".")
    and os.path.isdir(os.path.join(base_dir, class_dir))
]

os.mkdir(os.path.join(base_dir, "train"))
os.mkdir(os.path.join(base_dir, "val"))

for directory in directories:
    shutil.move(
        os.path.join(base_dir, directory), os.path.join(base_dir, "train", directory)
    )
    os.mkdir(os.path.join(base_dir, "val", directory))


for class_name in os.listdir(os.path.join(base_dir, "train")):
    train_class_dir = os.path.join(base_dir, "train", class_name)
    test_class_dir = os.path.join(base_dir, "val", class_name)

    images = sorted(os.listdir(train_class_dir))
    test_size = len(images) // 10

    for image in images[:test_size]:
        shutil.move(
            os.path.join(train_class_dir, image), os.path.join(test_class_dir, image)
        )

    print(f"Finished splitting images of {class_name}")
