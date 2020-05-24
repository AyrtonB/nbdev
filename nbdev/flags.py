__all__ = []

from .imports import Config, IN_IPYTHON
import sys, re

def _validate_param(line, magic_name, param_name=None, required=False, fixed_value=None):
    "Checks that `line` contains a single parameter, if required"
    # print warnings, rather than raise exceptions, as we don't want to be intrusive
    line = line.strip()
    if required and line == '':
        print(f'UsageError: {param_name} is missing. Usage `%{magic_name} {param_name}`')
        return False
    if re.search('\s', line):
        print(f'UsageError: {param_name} "{line}" must not contain whitespace')
        return False
    if fixed_value is not None and line != '' and line != fixed_value:
        print(f'UsageError: Invalid option "{line}". Usage `%{magic_name} [{fixed_value}]`')
    return True

def nbdev_export(line):
    """Put an `%nbdev_export` magic on each cell you want exported but not shown in the docs.
    Optionally override `%nbdev_default_export` by specifying a module: `%nbdev_export special.module`"""
    _validate_param(line, 'nbdev_export', 'module_name')

def nbdev_export_and_show(line):
    """Put an `%nbdev_export_and_show` magic on each cell you want exported with source code shown in the docs.
    Optionally override `%nbdev_default_export` by specifying a module: `%nbdev_export_and_show special.module`"""
    _validate_param(line, 'nbdev_export_and_show', 'module_name')

def nbdev_export_internal(line):
    """Put an `%nbdev_export_internal` magic on each cell you want exported without it being added to `__all__`,
    and without it showing up in the docs.
    Optionally override `%nbdev_default_export` by specifying a module: `%nbdev_export_internal special.module`"""
    _validate_param(line, 'nbdev_export_internal', 'module_name')

if IN_IPYTHON:
    from IPython.core.magic import register_line_magic
    fns = [nbdev_export, nbdev_export_and_show, nbdev_export_internal]
    for fn in fns: register_line_magic(fn)