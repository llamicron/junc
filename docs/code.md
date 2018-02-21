# DISCLAIMER: this isn't even close to being done

# Junc Code Overview

Here's an overview of the source code of this project. Read this, and then actually take a look at it.

## Table of Contents
* [Classes](#classes)
  * [Junc](#junc)

## Classes
* [`Junc`](#junc) - Handles the docopt args and connects to servers
* `Storage` - Handles necessary file creation, reading & writing, etc.
* `ServerList` - A collection of `_Servers`. Handles validation, adding, removing, & displaying servers
* `_Server` (private) - Contains server information

### `Junc`
This class handles a dictionary generated by `docopt`. It takes no constructor arguments, other than an optional `testing` arg. Code for this class is in `junc/__init__.py`

It has 2 attributes, a `ServerList` called `junc.sl`, and a `Storage` handler called `junc.st`.

It contains a method `what_to_do_with`, which takes `docopt` args and performs the desired behavior.
```python
args = docopt(__doc__)
junc = Junc()
junc.what_to_do_with(args) # Where the magic happens
```