#!python
"""
Start new file from boilerplate template
"""

from optparse import OptionParser
import os
import shutil
import sys


def parse_command_line():

    parser = OptionParser(
        usage = """

    # create new file from template
    %prog CATEGORY TEMPLATE FILE

    # create new file (deduce template from extension)
    %prog FILE

    # list all available templates
    %prog -l"""
    )
    

    parser.add_option(
        '-l', '--list', dest='list_templates', default=False,
        help='list all available templates',
        action='store_true',
    )
    
    (options, args) = parser.parse_args()

    if len(args) == 1:
        pass
    elif len(args) == 3:
        pass
    elif options.list_templates:
        pass
    else:
        parser.print_usage()
        sys.exit(1)

    return (options, args)


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
CATEGORIES = (
    'git',
    'py',
    'web',
)


def list_templates():
    print ''
    for category in CATEGORIES:
        print category + ':'
        for filename in os.listdir(os.path.join(SCRIPT_DIR, category)):
            if filename[0] is '.':
                continue
            print '    %s[%s]' % os.path.splitext(filename)
    print ''


def create_from_category(category, template, output_path):
    for filename in os.listdir(os.path.join(SCRIPT_DIR, category)):
        if filename[0] is '.':
            continue
        (temp, ext) = os.path.splitext(filename)
        if template == temp or template == filename:
            path = os.path.join(SCRIPT_DIR, category, filename)
            shutil.copyfile(path, output_path)
            return
    print 'no template found'
    sys.exit(2)


def create_from_filename(output_path):
    ext = os.path.splitext(output_path)[1] or os.path.basename(output_path)
    if ext == '.gitignore':
        create_from_category('git', 'ignore', output_path)
    elif ext == '.py':
        create_from_category('py', 'script', output_path)
    elif ext == '.css':
        create_from_category('web', 'stylesheet', output_path)
    elif ext == '.html':
        create_from_category('web', 'page', output_path)
    elif ext == '.js':
        create_from_category('web', 'script', output_path)
    else:
        print 'could not deduce template from file extension'
        sys.exit(3)


if __name__ == '__main__':

    (options, args) = parse_command_line()

    if options.list_templates:
        list_templates()
    elif len(args) == 1:
        create_from_filename(args[0])
    elif len(args) == 3:
        create_from_category(args[0], args[1], args[2])
