import attr
from PIL import Image
#-------------------------------------------------------------------------------
# Sierpinski's carpet
# Version: 0.3
# Date: 2017-10-25
# By: D. Clark
# Credit: CJ Carey for his input and assistance
# Description:
# --------------------------------------
# Simplistic utility to generate Sierpinski carpets. It's a command line driven
# script that will take basic commands to generate the patterns, and if desired,
# images of those patterns
#
# Todos:
# --------------------------------------
# * Testing
# * Logging
# * Investigate usage of matrices 
#-------------------------------------------------------------------------------
# Some sane defaults. Need a better place for this Using globals for now.
default_rules = {
    0:'000010000',
    1:'111111111'}
default_iterations = 3
colors = {'0': b'\xf3\x86\x30',
          '1': b'\x69\xd2\xe7',
          '2': b'\xe0\xe4\xcc',
          '3': b'\xa7\xdb\xd8',
          '4': b'\xfa\x69\x00',
        }
rules = None


@attr.s
class SierpinskiConfig(object):
    output = attr.ib(default='')
    rules = attr.ib(default=default_rules)
    iterations = attr.ib(default=default_iterations)


def print_help():
    """Explain what this is and show the user possible commands so that they can do stuff"""
    print("""
A sierpinski's carpet is a design that is derived from string or pattern replacement that is done over a number of
passes. An initial single value is replaced by a rule from a rule set where each rule defines how each value is
replaced. The number of rules is dependent on the number of possible values and output of each rule can only include
possible values.

This tool generates these carpets, but it also allows the user to set the rules and number of iterations. The user can
set a rule set and the number of iterations, but if not the default is a classic sierpinski carpet over 3 iterations. 
It also has a number of utilities as listed below.

    quit     (q,x)  - Exit the script.
    generate (g)    - Generate and print out a textual representation of the sierpinski pattern.
    help     (h)    - Display this message.
    print    (p)    - Reprints the last pattern that was generated.
    rules    (r)    - Go to the rule set up menu.
    image    (i)    - Write the pattern to an image file. 
    """

def generate(cfg):
    """All this does is take the user's desired configs (or the default) and generate/print the associated sierpinski
    carpet."""
    iterations = input('Number of iterations: ')
    #initialze the output so that it is the first character of the "0" rule
    print('Generation started...')
    cfg.output = cfg.rules[0][0] + '\n'
    lcv = 0
    while lcv < int(iterations)-1:
        next_output = ''
        staged_line_1 = ''
        staged_line_2 = ''
        staged_line_3 = ''
        for focus in cfg.output:
            if focus == '\n':
                #End of line prep for next line
                next_output = next_output + '\n'.join([staged_line_1, staged_line_2, staged_line_3]) + '\n'
                staged_line_1 = ''
                staged_line_2 = ''
                staged_line_3 = ''
            else:
                try:
                    staged_line_1 = staged_line_1 + cfg.rules[int(focus)][0:3]
                    staged_line_2 = staged_line_2 + cfg.rules[int(focus)][3:6]
                    staged_line_3 = staged_line_3 + cfg.rules[int(focus)][6:9]
                except KeyError as e:
                    print('rule set error: Check your rules for {}. It doesn\'t have a rule'.format(e))
        cfg.output = next_output
        cfg.iterations = iterations
        lcv += 1
    print_output(cfg)
    return cfg

def rules(cfg):
    """front end function that guides rule set up."""
    rules_menu = """
********************************************************************************
Rules Setup
********************************************************************************
Options
  p   - print rules
  r   - reset defaults
  m   - modify rules
  x,q - return to the main menu
"""
    print(rules_menu)
    while 1==1:
        command = input('> ')
        if command == 'p':
            print_rules(cfg)
            print('\n',rules_menu)
        elif command == 'r':
            cfg = reset_rules(cfg)
            print('\n',rules_menu)
        elif command == 'm':
            cfg = modify_rules(cfg)
            print('\n',rules_menu)
        elif command in ('x','q'):
            return cfg
        elif len(command) == 0:
            print('Type a command and then press enter')
        else:
            print('Invalid command', '\n\n', rules_menu)

def print_rules(cfg):
    print('Current rules')
    for rule_id, rule_value in cfg.rules.items():
        print(rule_id, ' > ', rule_value)

def reset_rules(cfg):
    cfg.rules = default_rules
    print('Rules reset to classic Sierpinski')
    return cfg

def modify_rules(cfg):
    print('Enter in new rules. q, x, or just enter to stop.')
    rule = 0
    new_rule_set = {}
    new_rule = input('{} > '.format(rule))
    while new_rule not in ('q', 'x', ''):
        if len(new_rule) == 9:
            new_rule_set[rule] = new_rule
            rule += 1
        else:
            print('Rule must be 9 characters long')
        new_rule = input('{} > '.format(rule))
    if len(new_rule_set) > 0:
        print('New rule set defined:')
        print(new_rule_set)
        cfg.rules = new_rule_set
    else:
        print('New rule set is empty. Ignoring changes')
    return cfg

def print_output(cfg):
    """Convenience function that check if there is output to be printed and prints it."""
    if len(cfg.output) > 0:
        print(cfg.output)
    else:
        print('*'*40, 'Warning', '*'*40)
        print('A carpet hasn''t been generated yet. Use the "generate" command to generate one. See "help"')
        print('for more commands"')

def chunker(s):
    """Spilt s string into 8 long chunks and convert to ints"""
    for i in range(0, len(s), 8):
        yield int(s[i:i+8],2)

def generate_image(cfg):
    size = 3 ** (int(cfg.iterations)-1)
    color_count = len(cfg.rules)

    #For two rules we need to padd and chunk
    if color_count == 2:
        padding = '0'*(8-size%8)
        stripped_data = cfg.output.translate({ord(c): padding for c in '\n'})
        refined_data = bytes(list(chunker(stripped_data)))
        mode = '1'

    if color_count > 2:
        stripped_data = cfg.output.translate({ord(c): None for c in '\n'})
        refined_data = b''.join([colors[n] for n in stripped_data])
        mode = 'RGB'

    image = Image.frombytes(mode, (size, size), refined_data)
    image.save('test.bmp')

def main():
    """Main function to drive the user interface"""
    cfg = SierpinskiConfig()
    print('*'*80)
    print('Sierpinski''s Carpet Generator')
    print('*'*80)
    while 1==1:
        command = input('>')
        if command in ('h', 'help'):
            print_help()
        elif command in ('q', 'x', 'quit', 'exit'):
            return 0
        elif command in ('g', 'generate'):
            cfg = generate(cfg)
        elif command in ('r', 'rules'):
            cfg = rules(cfg)
        elif command in ('p', 'print'):
            print_output(cfg)
        elif command in ('i', 'image'):
            generate_image(cfg)
        elif len(command) == 0:
            print('Type a command and then press enter')
        else:
            print('Invalid command. Try again or type "h" or "help" for an explanation.')

if __name__ == '__main__':
    main()


#Notes
#=====
# * Patterns are generated using string replacement
# * Need to generate 3 lines at once
