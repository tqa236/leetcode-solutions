import argparse
import string
import os
from string import Template


def make_exercise(id, name, method):
    path = os.getcwd()
    words = []
    for word in name.split():
        words.append(word[0].upper() + word[1:])

    folder_name = str(id).zfill(4) + "-" + "".join(words)
    exercise_name = name.lower().replace(" ", "_")
    folder_path = f"{path}/exercises/{folder_name}"
    if not os.path.exists(folder_path):
        print(f"Create {folder_path}.")
        os.mkdir(folder_path)
    else:
        print(f"Path {folder_path} already existed.")
    info = {"exercise_name": exercise_name, "method_name": method}
    with open("utils/skeleton_test.py", "r") as f:
        test_file = f.read().format(exercise_name=exercise_name, method=method)

    with open(f"{folder_path}/{exercise_name}.py", "w") as f:
        f.write("")

    with open(f"{folder_path}/{exercise_name}_test.py", "w") as f:
        f.write(test_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse arguments for new exercises.")
    parser.add_argument("-i", "--id", type=int, help="Exercise's id.")
    parser.add_argument("-n", "--name", type=str, help="Exercise's name.")
    parser.add_argument("-m", "--method", type=str, help="Class's method name.")
    args = parser.parse_args()
    make_exercise(args.id, args.name, args.method)