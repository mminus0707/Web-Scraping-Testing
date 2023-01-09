def add(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               string
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " + "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " + "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " + "
  if inp4 == "s":
    inp5 = input("Enter your string: ")
    str1 = "  result" + str(len(var)) + " = " + "'" + inp5 + "'" + " + "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               string
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
  if inp6 == "s":
    inp5 = input("Enter your string: ")
    str1 = "'" + inp5 + "'"
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " + "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   string
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
      if inp8 == "s":
        inp5 = input("Enter your string: ")
        str1 = "'" + inp5 + "'"
    else:
      cont = False
    
  return str1

def sub(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " - "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " - "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " - "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " - "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
    
  return str1

def mult(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " * "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " * "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " * "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " * "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
    
  return str1


def divide(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " / "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " / "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " / "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " / "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
    
  return str1
def div(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " // "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " // "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " // "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " // "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
    
  return str1

##########
def mod(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  result = "result" + str(len(var)+1)
  var.append(result)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = "  result" + str(len(var)) + " = " + str(param[inp5-1]) + " % "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  result" + str(len(var)) + " = " + str(inp5) + " % "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  result" + str(len(var)) + " = " + str(var[inp5-1]) + " % "
  
  inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
    
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " % "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
    
  return str1
def prnt(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = " print( " + str(param[inp5-1])
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  print( " + str(inp5)
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  print( " + str(var[inp5-1])

  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True
      str1 += " , "
      inp8 = input(""" 
      Next value I would like to add is an
                   parameter
                   number
                   variable
                   """)
      if inp8.lower() == "p":
        inp9 = int(input("Which parameter ?"))
        str1 = str1 + str(params[inp9-1])
      if inp8.lower() == "n":
        inp9 = int(input("Enter the number"))
        str1 = str1 + str(inp9)
      if inp8 == "v":
        print(var)
        inp5 = int(input("Which variable? "))
        str1 = str1 + str(var[inp5-1])
    else:
      cont = False
  str1 += " )"
  return str1
  
def rtrn(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = " return( " + str(param[inp5-1]) + " )"
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  return( " + str(inp5) + " )"
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  return( " + str(var[inp5-1]) + " )"
  
  return str1


########
def whle(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = " while " + str(param[inp5-1])
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  while " + str(inp5)
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  while " + str(var[inp5-1])

  comparison = ["equal","not equal","greater","less","greater or equal","less or "]
  comparison2 = ["==","!=",">","<",">=","<="]
  
  print("Enter an operator")
  print(str1," is")
  inp6 = input("")

  chk = False
  num = 0
  
  for x in range(0,len(comparison)):
    if comparison[x] == inp6:
      chk = True
      num = x
      break

  if chk == True:
    str1 = str1 + " " + comparison2[num] + " "

    inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
  
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True

      ops = ["and","or","not"]
      inp11 = input("Please choose an operator")
      
      chk1 = False
      
      for y in range(0,len(ops)):
        if comparison[y] == inp11.lower():
          chk1 = True
          break

      if chk1 == True:
        str1 = str1 + inp11 + " "
      
        inp8 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp8.lower() == "p":
          inp9 = int(input("Which parameter ?"))
          str1 = str1 + str(params[inp9-1])
        if inp8.lower() == "n":
          inp9 = int(input("Enter the number"))
          str1 = str1 + str(inp9)
        if inp8 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])

        comparison = ["equal","not equal","greater","less","greater or equal","less or "]
        comparison2 = ["==","!=",">","<",">=","<="]
        
        print("Enter an operator")
        print(str1," is")
        inp6 = input("")
      
        chk = False
        num = 0
        
        for x in range(0,len(comparison)):
          if comparison[x] == inp6:
            chk = True
            num = x
            break
      
        if chk == True:
          str1 = str1 + " " + comparison2[num] + " "
      
          inp6 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp6 == "p":
          inp5 = int(input("Which parameter? "))
          str1 = str1 + str(params[inp5-1])
        if inp6 == "n":
          inp5 = int(input("Enter the number "))
          str1 = str1 + str(inp5)
        if inp6 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])
    else:
      cont = False
  str1 += " :"
  return str1

def f(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = " if " + str(param[inp5-1])
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  if " + str(inp5)
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  if " + str(var[inp5-1])

  comparison = ["equal","not equal","greater","less","greater or equal","less or "]
  comparison2 = ["==","!=",">","<",">=","<="]
  
  print("Enter an operator")
  print(str1," is")
  inp6 = input("")

  chk = False
  num = 0
  
  for x in range(0,len(comparison)):
    if comparison[x] == inp6:
      chk = True
      num = x
      break

  if chk == True:
    str1 = str1 + " " + comparison2[num] + " "

    inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
  
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True

      ops = ["and","or","not"]
      inp11 = input("Please choose an operator")
      
      chk1 = False
      
      for y in range(0,len(ops)):
        if comparison[y] == inp11.lower():
          chk1 = True
          break

      if chk1 == True:
        str1 = str1 + inp11 + " "
      
        inp8 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp8.lower() == "p":
          inp9 = int(input("Which parameter ?"))
          str1 = str1 + str(params[inp9-1])
        if inp8.lower() == "n":
          inp9 = int(input("Enter the number"))
          str1 = str1 + str(inp9)
        if inp8 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])

        comparison = ["equal","not equal","greater","less","greater or equal","less or "]
        comparison2 = ["==","!=",">","<",">=","<="]
        
        print("Enter an operator")
        print(str1," is")
        inp6 = input("")
      
        chk = False
        num = 0
        
        for x in range(0,len(comparison)):
          if comparison[x] == inp6:
            chk = True
            num = x
            break
      
        if chk == True:
          str1 = str1 + " " + comparison2[num] + " "
      
          inp6 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp6 == "p":
          inp5 = int(input("Which parameter? "))
          str1 = str1 + str(params[inp5-1])
        if inp6 == "n":
          inp5 = int(input("Enter the number "))
          str1 = str1 + str(inp5)
        if inp6 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])
    else:
      cont = False
  str1 += " :"
  return str1

def elf(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = " elif " + str(param[inp5-1])
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = "  elif " + str(inp5)
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = "  elif " + str(var[inp5-1])

  comparison = ["equal","not equal","greater","less","greater or equal","less or "]
  comparison2 = ["==","!=",">","<",">=","<="]
  
  print("Enter an operator")
  print(str1," is")
  inp6 = input("")

  chk = False
  num = 0
  
  for x in range(0,len(comparison)):
    if comparison[x] == inp6:
      chk = True
      num = x
      break

  if chk == True:
    str1 = str1 + " " + comparison2[num] + " "

    inp6 = input(""" 
  Next value I would like to add is an
               parameter
               number
               variable
               """)
  if inp6 == "p":
    inp5 = int(input("Which parameter? "))
    str1 = str1 + str(params[inp5-1])
  if inp6 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str1 + str(inp5)
  if inp6 == "v":
    print(var)
    inp5 = int(input("Which variable? "))
    str1 = str1 + str(var[inp5-1])
  
  cont = True

  while cont == True:
    inpcont = input("Would you like to continue to add? ")
    if inpcont.lower() == "yes":
      cont = True

      ops = ["and","or","not"]
      inp11 = input("Please choose an operator")
      
      chk1 = False
      
      for y in range(0,len(ops)):
        if comparison[y] == inp11.lower():
          chk1 = True
          break

      if chk1 == True:
        str1 = str1 + inp11 + " "
      
        inp8 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp8.lower() == "p":
          inp9 = int(input("Which parameter ?"))
          str1 = str1 + str(params[inp9-1])
        if inp8.lower() == "n":
          inp9 = int(input("Enter the number"))
          str1 = str1 + str(inp9)
        if inp8 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])

        comparison = ["equal","not equal","greater","less","greater or equal","less or "]
        comparison2 = ["==","!=",">","<",">=","<="]
        
        print("Enter an operator")
        print(str1," is")
        inp6 = input("")
      
        chk = False
        num = 0
        
        for x in range(0,len(comparison)):
          if comparison[x] == inp6:
            chk = True
            num = x
            break
      
        if chk == True:
          str1 = str1 + " " + comparison2[num] + " "
      
          inp6 = input(""" 
        Next value I would like to add is an
                     parameter
                     number
                     variable
                     """)
        if inp6 == "p":
          inp5 = int(input("Which parameter? "))
          str1 = str1 + str(params[inp5-1])
        if inp6 == "n":
          inp5 = int(input("Enter the number "))
          str1 = str1 + str(inp5)
        if inp6 == "v":
          print(var)
          inp5 = int(input("Which variable? "))
          str1 = str1 + str(var[inp5-1])
    else:
      cont = False
  str1 += " :"
  return str1
  
###########################
def els(param,var):
  str1 = "  else:"
  return str1
def set(param,var):
  print(param)
  print(var)
  inp4 = input("""
               parameter
               number
               variable
               """)
  if inp4 == "p":
    print(param)
    inp5 = int(input("Which parameter? "))
    str1 = str(param[inp5-1]) + " = "
  if inp4 == "n":
    inp5 = int(input("Enter the number "))
    str1 = str(inp5) + " = "
  if inp4 == "v":
    inp5 = int(input("Which variable? "))
    str1 = str(var[inp5-1]) + " = "

    return str1

def display(line1arr,lines):
  line1 = ""
  for x in range(0,len(line1arr)):
    line1 += str(line1arr[x])
    
  print(line1)
  for x in range(0,len(lines)):
    print(lines[x])
    
#######
    
inp = input("I would like a ")

line1arr = ["def newfunction(",]
params = []
variables = []

if inp.lower() == "f":
  inp2 = int(input("I would like this many parameters "))
  if inp2 > 0:
    for x in range(0,inp2):
      param = "parameter" + str(x)
      line1arr.append(param)
      params.append(param)
      if x == inp2-1:
        break
      line1arr.append(",")
      
    line1arr.append("):")
  line2 = []

nline = True
lines = []

while nline == True:
  inpline = input("Would you like to add another line? ")
  if inpline.lower() == "yes":
    print("//////////////")
    display(line1arr,lines)
    print("//////////////")
    inp3 = input("I would like this line to ")
    if inp3 == "add":
      line2 = lines.append(add(params,variables))
    if inp3 == "sub":
      line2 = lines.append(sub(params,variables))
    if inp3 == "mult":
      line2 = lines.append(mult(params,variables))
    if inp3 == "divide":
      line2 = lines.append(divide(params,variables))
    if inp3 == "div":
      line2 = lines.append(div(params,variables))
    if inp3 == "mod":
      line2 = lines.append(mod(params,variables))
    if inp3 == "print":
      line2 = lines.append(prnt(params,variables))
    if inp3 == "return":
      line2 = lines.append(rtrn(params,variables))
    if inp3 == "while":
      line2 = lines.append(whle(params,variables))
    if inp3 == "set":
      line2 = lines.append(set(params,variables))
    if inp3 == "if":
      line2 = lines.append(f(params,variables))
    if inp3 == "elif":
      line2 = lines.append(elf(params,variables))
    if inp3 == "else":
      line2 = lines.append(els(params,variables))
      
  else:
    nline = False

print(" FINAL CODE ")
display(line1arr,lines)



f = open("code","a")

line1p = ""
for x in range(0,len(line1arr)):
  line1p += str(line1arr[x])

line1p += "\n"

f.write(line1p)
  
for x in range(0,len(lines)):
  wline = lines[x] + "\n"
  f.write(wline)
f.close()