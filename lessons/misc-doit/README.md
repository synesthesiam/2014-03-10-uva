# Make and doit - An Extremely Brief Overview

## Make

Make lets you group and name shell commands that perform common workflow tasks. These tasks are called *targets*, and are specified in a special file called `Makefile` (note the capital 'M'). This is just a text file with some special formatting.

A Makefile looks like this:

    target1: target2
        shell-command
        shell-command

    target2:
        shell-command; shell-command

In the example above, `target1` depends on `target2`. This means that `target2` will run before `target1`. Each target has a set of shell commands that will be executed, one after the other. If the shell commands are on separate lines, they will be isolated from each other as if they were typed in **different** terminals. If they're on the same line and separated by semi-colons, however, they will behave as if they were typed in the **same**.

When you run the `make` command, it will search for a `Makefile` file in the current directory and run the first target it finds. If you give `make` an argument, as in `make target2`, it will only run that target (and all of its dependent targets).

Makefiles can contain all sorts of [special syntax](http://www.gnu.org/software/make/manual/make.html) for transforming file names and complex dependencies, but it's hard to learn and maintain. A better option (for us) is to use the Python tool `doit`.

## doit

[DoIt](http://pydoit.org/) is a Python automation tool. At its core, its just a coding convention plus a command-line tool called `doit`.

Like `make`, `doit` handles dependencies between *tasks* (instead of targets). In addition to shell commands, though, you can write arbitrary Python code! When you run `doit`, it looks for a file in the current directory called `dodo.py` and runs all of the functions inside that start with the word `task_` (with the underscore after). Here's an example:

    def task_example():
        return {
            'actions': [my_function],
            'file_dep': ['my_input_file'],
            'targets': ['result_file'],
        }

Each task function should return a dictionary with a few special fields:

    * `actions` - the name of a Python function
    * `file_dep` - name(s) of input file(s)
    * `targets` - name(s) of output file(s)

DoIt is smart enough to figure out the order to run the tasks based on file dependencies and targets. If you run `doit` without arguments, it will run all tasks. Providing `doit` with an argument, such as `doit X` will just run the task named `task_X`.

A common way to write DoIt tasks is like this:

    def task_example():
        input_files = ['my_input_file']
        output_files = ['result_file']
        
        def my_function():
            for input, output in zip(input_files, output_files):
                pass  # Do something

        return {
            'actions': [my_function],
            'file_dep': input_files,
            'targets': output_files,
        }

In the example above, we define lists with our input and output files for the tasks (e.g., what files we will process and what files we will produce). We define a function inside our task, and pass it to `actions`. When the task is run, `my_function` will be executed, and will process the input/output file pairs.
