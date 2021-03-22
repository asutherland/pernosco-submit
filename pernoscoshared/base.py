import os
import shutil
import subprocess

trace_dir = None
echo_commands = False

# Given a complete source path and a complete destination path,
# replaces the destination with a copy of the source.
def copy_replace_file(src, dst):
    try:
        os.remove(dst)
    except:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        pass
    shutil.copyfile(src, dst)

def check_output(process_args, *proc_args, **kwargs):
    if echo_commands:
        print("Running %s"%(" ".join(process_args)))
    return subprocess.check_output(process_args, *proc_args, **kwargs)

def check_call(process_args, *proc_args, **kwargs):
    if echo_commands:
        print("Running %s"%(" ".join(process_args)))
    return subprocess.check_call(process_args, *proc_args, **kwargs)

def Popen(process_args, *proc_args, **kwargs):
    if echo_commands:
        print("Running %s"%(" ".join(process_args)))
    return subprocess.Popen(process_args, *proc_args, **kwargs)