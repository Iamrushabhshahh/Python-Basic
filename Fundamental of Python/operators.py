# ================== Arithmatic operator ===========================

# Exponential     **
# Multiplication  *
# Division        /
    # Division always return the float value a output.
    # Python also provide Floor Division operator that rounds the value to lesser nearest number represent by [ // ]
#  Modulo 
    # Returns reminder after the division
# Addition + 
# Substraction - 

# Binary Operator
    # E.g 5 -5 
    #  Binary operator always expect value to right and left
# Unary Operator 
    # Unary operator can used to only define value to right 
    # E.g -5 

# we can use as many as  operator in single expression
# eg print( 10 - 6 ** 7 / 9 * 23 + 1 )
    # For this you have to make sure the  important thing in mind is priority.
    # Highest priority
    #                      [ + ] [ - ]  Unary Operator
    #                      [ ** ]  
    #                      [ * ][ / ][ // ][ % ]
    #                      [ + ][ - ]   binary operator
     
# If multiple operator have same priority we go from left hand side.

# In sub expression that subexpression has highest priority in expression.abs
    # Eg. print(2*(5+3))
