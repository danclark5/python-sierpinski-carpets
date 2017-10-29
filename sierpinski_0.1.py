#-------------------------------------------------------------------------------
# Sierpinski's carpet
# Version: 0.1
# Date: 2017-10-25
# By: D. Clark
# Description:
# --------------------------------------
# End result of first attempt to create a script to generate a sierpinski's
# carpet. It's crude in that you can't change the number of colors, and it's 
# very brittle.
#-------------------------------------------------------------------------------
rules = {0:'000010000',
        1:'111111111'}

def main():
    raw_parameters = input('Enter number of colors and iterations deliminated by a space:')
    num_colors, num_iterations = raw_parameters.split(' ')

    #initialze the output so that it is the first character of the "0" rule
    output = rules[0][0] + '\n'
    lcv = 0
    while lcv < int(num_iterations)-1:
        next_output = ''
        staged_line_1 = ''
        staged_line_2 = ''
        staged_line_3 = ''
        for focus in output:
            if focus == '\n':
                #End of line prep for next line
                next_output = next_output + '\n'.join([staged_line_1, staged_line_2, staged_line_3]) + '\n'
                staged_line_1 = ''
                staged_line_2 = ''
                staged_line_3 = ''
            else:
                staged_line_1 = staged_line_1 + rules[int(focus)][0:3]
                staged_line_2 = staged_line_2 + rules[int(focus)][3:6]
                staged_line_3 = staged_line_3 + rules[int(focus)][6:9]
        output = next_output
        lcv += 1
    print('***********output***********')
    print(output)

    #a way to store rules
    #how to render

if __name__ == '__main__':
    main()


#Notes
#=====
# * Patterns are generated using string replacement
# * Need to generate 3 lines at once
