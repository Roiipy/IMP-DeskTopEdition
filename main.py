import time
import random
import datetime
import unicodedata
#######################IMP RunFile###############################
file = r"test.imp"
#################################################################


imp_var = {}
imp_function_end = []
imp_function_start = []
imp_function_name = []
file = open(file, encoding="utf8")
imp_data = file.read().split("\n")
file.close()
# codelist

code_list = [
    "Name : say\nCode : say - [Data(variables can also be used and must be of type str)];\nDescription : Prints characters to the console.\nexample : say - HELLO WORLD;\n",
    "Name : help\nCode : help(If you do not enter the code name to search, all codes will be displayed);\nDescription : Find the code that exists in the IMP. The result is also assigned to the variable help as True or False.\nexample : help();\n",
    "Name : quiz\nCode : quiz - [Data(variables can also be used and must be of type str)];\nDescription : Ask a question on the console. Also, the answer assigns the answer data to the variable Answer.\nexample : quiz - how st weather?;\n",
    "Name : sleep\nCode : sleep - [Data(variables can also be used and must be of type int)];\nDescription : You can stop the process for a specified second.\nexample : sleep - 5;\n",
    "Name : var\nCode : var [VariableName] = [SubstitutionValue];\nDescription : Assign a value to the variable. You can also assign variables and perform some operations.\nexample : var name = Roii.py;\n",
    "Name : function\nCode : function [FunctionName](){\n[RunCode]\n}\nDescription : Assign a value to the variable. You can also assign variables and perform some operations.\nexample : function hello(){\n  say - HelloWorld!;\n}\n",
    "Name : fun\nCode : fun.[FunctionName]();\nDescription : Execute the function.\nexample : fun.hello();\n> Hello World!\n",
    "Name : rand\nCode : rand();\nDescription : Generates an integer random number within the specified range. The return value is assigned to the variable rand.\nexample : rand(1,50);\nsay - (rand);\n> 43\n",
    "Name : date\nCode : rand();\nDescription : Gets the current time. You can put any character in the argument of the date function, replacing y with year, m with month, d with day, mi with minute, se with second, and mis with microsecond.\nexample : date(This year is y year)\n> This year is 2021 year\n",
    "Name : line_run\nCode : line_run([Run_Line]);\nDescription : Executes the program on the specified line on the spot.\nexample : say - hi;\nline_run(1);\n> hi \n> hi\n"

]
code_name = [
    "say - ",
    "help - ",
    "quiz - ",
    "sleep - ",
    "var ",
    "function ",
    "func.",
    "rand()",
    "date()",
    "line_run()"
]
# error list
error_list = {
    "s": "SyntaxError",
    "t": "TypeError",
    "v": "ValueError",
    "k": "KeyError",
    "i": "InternalError",
    "e": "ExceptionError",
    "o": "OverflowError",
    "r": "RecursionError",
    "index": "IndexError"
}
# error_description
error_data = {
    "varnotdata": "There is no name to assign to the variable.",
    "varnotvalue": "There is no value to assign to the variable.",
    "i": "invalid syntax",
    "notvar1": "The called variable ",
    "notvar2": " is undefined.",
    "notdevar": "The variables needed internally were not defined. Please re-download the IMP.",
    "varmulti": "You cannot specify multiple data.",
    "replacenovar": "The variable VARNAME cannot be replaced.",
    "notpydef": "The usage of the Python function used when assigning is incorrect.",
    "notint": "Specify an int type (not str type) value.",
    "oversleep": "You cannot use a value greater than 2147483647.",
    "notfun": "The called function FUNNAME is not defined.",
    "maxobj": "The maximum number of internal memories has been reached during execution.",
    "replacenofun": "You do not have permission to replace the function.",
    "notargument": "Not enough arguments are required by the function.",
    "notline": "The line does not exist.",
    "ifnotfun": "Only one function can be described as the execution content of the if statement.",
    "varstraddnot": "You cannot add letters to letters."
}
# Bad Variable
BAD_VAR_NAME = []
# Bad Function
BAD_FUNCITON_NAME = []

try:
    def error(type, des, input):

        if input == "not":
            print(error_list[type] + " : [Line" +
                  str(line) + "] " + error_data[des])
        elif type == "k" and des == "notvar":
            print(error_list[type] + " : " + error_data["notvar1"] +
                  str(input) + error_data["notvar2"])
        elif type == "e" and des == "replacenovar":
            cash = error_list[type] + " : [Line" + \
                str(line) + "] " + error_data[des]
            cash = cash.replace("VARNAME", input)
            print(cash)
        elif type == "k" and des == "notfun":
            cash = error_list[type] + " : [Line" + \
                str(line) + "] " + error_data[des]
            cash = cash.replace("FUNNAME", input)
            print(cash)

        else:
            print("UnknownError : An unexpected error has occurred.")

        time.sleep(10000)

    def exc(haizyo, data):
        global imp_data, iet, BAD_VAR_NAME, code_list, imp_function_name, imp_function_start, imp_function_end, BAD_FUNCITON_NAME
        cmf = haizyo
        imp_text = data
        return_text = imp_text[imp_text.find(cmf) + len(cmf):]
        iet = {}
        iet = return_text[:-1]
        return iet

    def say(data):
        if data.endswith(";"):
            rt = exc("say - ;", data)
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        replace_text = str(replace_text)
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                print(rt)
            except KeyError:
                error("k", "notvar", "not")

        else:
            error("s", "i", "not")

    def var(data):
        if data.startswith("var "):

            p = len("var ")
            imp_text = data[p:]
            if data.endswith(";"):
                imp_text = imp_text.split()
                if imp_text[1] == "=":
                    if not len(imp_text) > 3:
                        VAR_NAME = imp_text[0]
                        p3 = imp_text[2]
                        imp_text_sub = p3[:-1]
                        VAR_CONTENT = imp_text_sub
                        if VAR_NAME in BAD_VAR_NAME:
                            error("e", "replacenovar", VAR_NAME)
                        try:
                            try:
                                i = 0
                                var_list = list(imp_var)
                                var_dlist = imp_var.values()
                                var_dlist = list(var_dlist)
                                while i < len(imp_var):
                                    if var_list[i] in VAR_CONTENT:
                                        replace_text = var_dlist[i]
                                        VAR_CONTENT = VAR_CONTENT.replace(
                                            '(' + var_list[i] + ')', replace_text)
                                    i += 1
                            except KeyError:
                                error("k", "notvar", "not")
                            try:
                                imp_var[VAR_NAME] = str(eval(VAR_CONTENT))
                            except NameError:
                                imp_var[VAR_NAME] = VAR_CONTENT
                            except TypeError:
                                error("t", "notpydef", "not")
                        except SyntaxError:
                            error("v", "varnotvalue", "not")
                    else:
                        error("v", "varmulti", "not")
                elif imp_text[1] == "+=":
                    if not len(imp_text) > 3:
                        VAR_NAME = imp_text[0]
                        p3 = imp_text[2]
                        imp_text_sub = p3[:-1]
                        VAR_CONTENT = imp_text_sub
                        if VAR_NAME in BAD_VAR_NAME:
                            error("e", "replacenovar", VAR_NAME)
                        try:
                            try:
                                i = 0
                                var_list = list(imp_var)
                                var_dlist = imp_var.values()
                                var_dlist = list(var_dlist)
                                while i < len(imp_var):
                                    if var_list[i] in VAR_CONTENT:
                                        replace_text = var_dlist[i]
                                        VAR_CONTENT = VAR_CONTENT.replace(
                                            '(' + var_list[i] + ')', replace_text)
                                    i += 1
                            except KeyError:
                                error("k", "notvar", VAR_NAME)
                            try:
                                imp_var[VAR_NAME] = int(imp_var[VAR_NAME]) + int(eval(VAR_CONTENT))
                            except ValueError:
                                error("t", "varstraddnot", "not")
                            except NameError:
                                error("k", "notvar", VAR_NAME)
                            except TypeError:
                                imp_var[VAR_NAME] = str(imp_var[VAR_NAME])
                            except KeyError:
                                var(f"var {VAR_NAME} = {VAR_CONTENT};")
                        except SyntaxError:
                            error("v", "varnotvalue", "not")
                    else:
                        error("v", "varmulti", "not")                
                else:
                    error("v", "varnotvalue", "not")

            else:
                error("s", "i", "not")

    def quiz(data):
        if data.endswith(";"):
            rt = exc("quiz - ;", data)
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                Answer = input("" + rt + "\n> ")
                imp_var["Answer"] = Answer
            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def sleep(data):
        if data.endswith(";"):
            rt = exc("sleep - ;", data)
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                    try:
                        time.sleep(int(rt))
                    except ValueError:
                        error("v", "notint", "not")
                    except OverflowError:
                        error("o", "oversleep", "not")
            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def help(data):
        if data.endswith(";"):
            rt = exc("help();", data)
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1

                if rt == "":
                    i = 0
                    while i < len(code_list):
                        print(code_list[i])
                        i += 1
                else:
                    code_list_save = []
                    rt = data[5:]
                    rt = rt[:3]
                    if rt in code_name:
                        i = 0
                        while i < len(code_list):
                            if code_name[i] in rt:
                                code_list_save += code_list[i]
                                print(code_list[i])
                                imp_var["help"] = "True"
                            i += 1
                    else:
                        imp_var["help"] = "False"

            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def function(data):
        if data.endswith("{") and data[-3:] == "(){":
            f_end_if = 0
            f_name = exc("function ", data)
            f_name = f_name[:-2]
            if f_name in BAD_FUNCITON_NAME:
                error("e", "replacenofun", "not")
            for imp_datasub in imp_data:
                if imp_datasub == "}":
                    f_end_if = 1
                    f_line = imp_data.index(imp_datasub) + 1
                    break
            if f_end_if == 1:
                imp_function_end.append(f_line)
                imp_function_start.append(line)
                imp_function_name.append(f_name)
                line_i = f_line
            else:
                error("s", "i", "not")

        elif not data.endswith("{"):
            error("s", "i", "not")
        else:
            error("s", "i", "not")

    def function_run(data):
        if data.endswith(";"):
            f_name = data[:-3]
            f_name = f_name[4:]
            if f_name in imp_function_name:
                run_code = imp_data[imp_function_start[imp_function_name.index(
                    f_name)]:imp_function_end[imp_function_name.index(f_name)]]
                run_codes = []
                for run_code2 in run_code:
                    run_codes.append(run_code2.lstrip())
                    
                for targets in run_codes:
                   main(targets)
            else:
                error("k", "notfun", f_name)
        else:
            error("s", "i", "")

    def rand(data):
        if data.endswith(");"):
            data = data[5:]
            data = data[:-2]
            data = data.split(",")
            try:
                var("var rand = " +
                    str(random.randint(int(data[0]), int(data[1]))) + ";")
            except ValueError:
                error("v", "notint", "not")
            except IndexError:
                error("v", "notargument", "not")

        else:
            error("s", "i", "not")

    def line_run_for(data):
        if data.endswith(");"):
            data = data[13:]
            data = data[:-2]
            if data == "":
                error("v","noargument","not")
            else:
                data = data.split(",");
                for hey in range(int(data[1])):
                    try:
                        main(imp_data[int(data[0]) - 1])
                    except IndexError:
                        error("index","notline","not")
    def line_run(data):
        if data.endswith(");"):
            data = data[9:]
            data = data[:-2]
            if data == "":
                error("v", "notargument", "not")
            else:
                try:
                    main(imp_data[int(data) - 1])
                except IndexError:
                    error("index", "notline", "not")

        else:
            error("s", "i", "not")

    def date(data):
        if data.endswith(");"):
            data = data[5:]
            data = data[:-2]
            dt_now = datetime.datetime.now()
            data = data.replace("mi", str(dt_now.minute))
            data = data.replace("se", str(dt_now.second))
            data = data.replace("mis", str(dt_now.microsecond))
            data = data.replace("y", str(dt_now.year))
            data = data.replace("m", str(dt_now.month))
            data = data.replace("d", str(dt_now.day))
            data = data.replace("h", str(dt_now.hour))
            try:
                var("var date = " + str(data) + ";")
            except ValueError:
                error("v", "notint", "not")
            except IndexError:
                error("v", "notargument", "not")

        else:
            error("s", "i", "not")

    def len_(data):
        if data.endswith(";"):
            rt = data
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', str(replace_text))
                    i += 1
                imp_var["len"] = len(rt) - 6
            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def num_for_(data):
        if data.endswith(";"):
            rt = data[8:]
            rt = rt[:-2]
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                rt = rt.split(',',1)
                if len(rt) == 2:
                    for i in range(int(rt[0])):
                        main(rt[1])
                else:
                    error("s","i","not")

            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def if_(data):
        global if_1, if_2, replace_if, var_inifs, data_sub
        var_inifs = ""
        if data.endswith("){"):
            data_sub = data[:-2]
            data_sub = data_sub[3:]
            data_sub = data_sub.split()
            if data_sub == "":
                error("s", "i", "not")
            elif len(data_sub) == 1 or len(data_sub) == 2:
                error("s", "i", "not")
            elif len(data_sub) != 3:
                error("s","i","not")
            else:
                if_1 = "not"
                if_2 = "not"
                if_test = "not"
                if_test2 = "not"
                try:
                    i = 0
                    var_list = list(imp_var)
                    var_dlist = imp_var.values()
                    var_dlist = list(var_dlist)
                    while i < len(imp_var):
                        if var_list[i] in data_sub[0]:
                            replace_text = var_dlist[i]
                            if_test = data_sub[0].replace('(' + var_list[i] + ')', str(replace_text))
                            break
                        i += 1
                    if if_test == "not":
                        if_1 = data_sub[0]
                    else:
                        if_1 = if_test
                except KeyError:
                    error("k", "notvar", "not")      
                try:
                    i = 0
                    var_list = list(imp_var)
                    var_dlist = imp_var.values()
                    var_dlist = list(var_dlist)
                    while i < len(imp_var):
                        if var_list[i] in data_sub[2]:
                            replace_text = var_dlist[i]
                            if_test2 = data_sub[2].replace('(' + var_list[i] + ')', replace_text)
                            break
                        i += 1
                    if if_test2 == "not":
                        if_2 = data_sub[2]
                    else:
                        if_2 = if_test2
                except KeyError:
                    error("k", "notvar", "not")
                #if_(==)_(!=)
                if data_sub[1] == "==":
                    if str(if_1) == str(if_2):
                        try:
                            i = line
                            if_end_if = 0
                            while i < len(imp_data):
                                if imp_data[i].lstrip() == "}":
                                    if_end_if = 1
                                    break
                                if imp_data[i].lstrip() == "}else{":
                                    if_end_if = 2
                                    break
                                else:
                                    main(imp_data[i].lstrip())
                                i += 1
                            if if_end_if == 1:
                                return
                            if if_end_if == 2:
                                return
                            else:
                                error("s","i","not")
                        except IndexError:
                            error("s","i","not")
                    else:
                        try:
                            i = line
                            if_end_if = 0
                            while i < len(imp_data):
                                if imp_data[i].lstrip() == "}":
                                    if_end_if = 1
                                    break
                                if imp_data[i].lstrip() == "}else{":
                                    if_end_if = 2
                                    break
                                i += 1
                            if if_end_if == 1:
                                return
                            if if_end_if == 2:
                                i += 1
                                if_end_if = 0
                                while i < len(imp_data):
                                    if imp_data[i].lstrip() == "}":
                                        if_end_if = 1
                                        return
                                    else:
                                        main(imp_data[i].lstrip())
                                    i += 1
                                if if_end_if == 1:
                                    return
                                else:
                                    error("s","i","not")
                            else:
                                error("s","i","not")
                        except IndexError:
                            error("s","i","not")                        
                elif data_sub[1] == "!=":
                    if str(if_1) != str(if_2):
                        try:
                            i = line
                            if_end_if = 0
                            while i < len(imp_data):
                                if imp_data[i].lstrip() == "}":
                                    if_end_if = 1
                                    break
                                if imp_data[i].lstrip() == "}else{":
                                    if_end_if = 2
                                    break
                                else:
                                    main(imp_data[i].lstrip())
                                i += 1
                            if if_end_if == 1:
                                return
                            if if_end_if == 2:
                                return
                            else:
                                error("s","i","not")
                        except IndexError:
                            error("s","i","not")
                    else:
                        try:
                            i = line
                            if_end_if = 0
                            while i < len(imp_data):
                                if imp_data[i].lstrip() == "}":
                                    if_end_if = 1
                                    break
                                if imp_data[i].lstrip() == "}else{":
                                    if_end_if = 2
                                    break
                                i += 1
                            if if_end_if == 1:
                                return
                            if if_end_if == 2:
                                i += 1
                                if_end_if = 0
                                while i < len(imp_data):
                                    if imp_data[i].lstrip() == "}":
                                        if_end_if = 1
                                        return
                                    else:
                                        main(imp_data[i].lstrip())
                                    i += 1
                                if if_end_if == 1:
                                    return
                                else:
                                    error("s","i","not")
                            else:
                                error("s","i","not")
                        except IndexError:
                            error("s","i","not")   
                else:
                    error("s", "i", "not")
        else:
            error("s","i","not")

    def imp_flat(data):
        if data.endswith(";"):
            rt = data.lstrip("imp.flat(")
            rt = rt.rstrip(");")
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                rt = rt.split(",")
                if len(rt) == 2:
                    error("s","i","not")
                if not type(rt[0]) == "<class 'int'>" and type(rt[1]) == "<class 'int'>":
                    error("s","i","not")  
                imp_subline = 0
                imp_subsubline = 0        
                print_imp = []     
                while imp_subline < int(rt[0]):
                    while imp_subsubline < int(rt[1]):
                        print_imp.append(rt[2])
                        imp_subsubline += 1
                    imp_subline += 1
                    print("".join(print_imp))
            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")
            

    def imp_square(data):
        if data.endswith(";"):
            rt = data.lstrip("imp.square(")
            rt = rt.rstrip(");")
            var_inif = rt
            try:
                i = 0
                var_list = list(imp_var)
                var_dlist = imp_var.values()
                var_dlist = list(var_dlist)
                while i < len(imp_var):
                    if var_list[i] in var_inif:
                        replace_text = var_dlist[i]
                        rt = rt.replace('(' + var_list[i] + ')', replace_text)
                    i += 1
                rt = rt.split(",")
                if len(rt) == 2:
                    error("s","i","not")
                if not type(rt[0]) == "<class 'int'>" and type(rt[1]) == "<class 'int'>":
                    error("s","i","not")  
                imp_subline = 0
                imp_subsubline = 0        
                print_imp = [] 
                while imp_subline < int(rt[0]):
                    while imp_subsubline < int(rt[1]):
                        print_imp.append(rt[2])
                        imp_subsubline += 1
                    imp_subline += 1
                print("".join(print_imp))   
                if unicodedata.east_asian_width('Π') == "W" or unicodedata.east_asian_width('Π') == "F":
                    pr_1 = rt[2]
                    pr_4 = int(rt[1]) - 2
                    pr_5 = pr_4 - 1
                    pr_2 = "　" + "　" * pr_5
                    pr_3 = rt[2]
                    for i in range(pr_4):
                        print(str(pr_1) + str(pr_2) + str(pr_3))
                else:
                    pr_1 = rt[2]
                    pr_4 = int(rt[1]) - 2
                    pr_5 = pr_4 - 1
                    pr_2 = " " + " " + " " + " " + " " + " " + " " + " " + " " + " " * pr_5
                    pr_3 = rt[2]
                    for i in range(pr_4):
                        print(str(pr_1) + str(pr_2) + str(pr_3))      
                while imp_subline < int(rt[0]):
                    while imp_subsubline < int(rt[1]):
                        print_imp.append(rt[2])
                        imp_subsubline += 1
                    imp_subline += 1
                print("".join(print_imp))   
                        
            except KeyError:
                error("k", "notvar", "not")
        else:
            error("s", "i", "not")

    def main(target):
        # say
        if target.startswith("say - "):
            say(target)
        # var
        if target.startswith("var "):
            var(target)
        # quiz
        if target.startswith("quiz - "):
            quiz(target)
        # function
        if target.startswith("function "):
            function(target)
        # sleep
        if target.startswith("sleep - "):
            sleep(target)
        # function_run
        if target.startswith("fun."):
            function_run(target)
        # help
        if target.startswith("help("):
            help(target)
        # rand
        if target.startswith("rand("):
            rand(target)
        # date
        if target.startswith("date("):
            date(target)
        # line_run()
        if target.startswith("line_run("):
            line_run(target)
        # line_run_for()
        if target.startswith("line_run_for("):
            line_run_for(target)
        # if
        if target.startswith("if("):
            if_(target)
        # len()
        if target.startswith("len("):
            len_(target)
        # num_for()
        if target.startswith("num_for("):
            num_for_(target)
        # imp.flat(回数,長さ,文字)
        if target.startswith("imp.flat("):
            imp_flat(target)
        # imp.square(回数,長さ,文字)
        if target.startswith("imp.square("):
            imp_square(target)

    # Main
    imp_line = imp_data
    line_i = 0
    while line_i < len(imp_line):
        global line
        target2 = imp_line[line_i]
        line = line_i + 1
        main(target2)

        line_i += 1

except RecursionError:
    error("r", "maxobj", "not")
