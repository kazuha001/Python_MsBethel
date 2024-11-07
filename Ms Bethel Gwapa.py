
import math

arraysForFname = []

arraysForMname = []

arraysForLname = []

arraysForAge = []

arraysForBirth = []

def choose():
    
    
    
    loop = True

    while loop:
        print("")
        number = int(input("Enter Decimal Number: "))
        print("")
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        print("4. All")
        print("0. Exit")
        print("")
        choose = input("Choose: ")

        if choose == '1':

           

            print("")
            print("Your Decimal: ", number)
            print("")

            binary_digits = []

            # Seperators
            fractional, integer = math.modf(number)

            number = integer / 2

            # Result and Ramainders
            combined1 = float(integer + fractional)

            if combined1 != integer:

                binary_digits.append("1")

            else:

                binary_digits.append("0")

            loop1 = True

            while loop1:
                # Seperators
                fractional, integer = math.modf(number)

                number = integer / 2

                # Result and Ramainders
                combined1 = float(integer + fractional)

                if combined1 != integer:

                    print(float(combined1), "- R 1")

                    binary_digits.append("1")

                else:

                    print(float(combined1), "- R 0")

                    binary_digits.append("0")

                if number <= 0:

                    break

                else:

                    loop1 = True

            binary_digits.reverse()

            if binary_digits:

                binary_digits.pop()


                binary_represent1 = ''.join(binary_digits)

                print("")
                print("Binary: ", binary_represent1)

                print("")

                input("Press Enter")

        elif choose == '2':

            print("")
            print("Your Decimal: ", number)
            print("")

            octalArrays = []

            loop2 = True

            fractional, integer = math.modf(number)
            number = integer / 8
            fractionaltimes = int(fractional * 8)

            octalArrays.append(fractionaltimes)


            while loop2:

            # Seperators
                fractional, integer = math.modf(number)

                number = integer / 8

                fractionaltimes = int(fractional * 8)

            # Result and Ramainders
                combined1 = float(integer + fractional)
                print(float(combined1), "R -", int(fractionaltimes))

                octalArrays.append(fractionaltimes)

                if number <= 0:

                    break

                else:

                    loop2 = True


            octalArrays.reverse()

            if octalArrays:

                octalArrays.pop()

                resultArrays = "".join(map(str, octalArrays))

                print("")
                print("Octal: ",resultArrays)
                print("")

                input("Press Enter")

        elif choose == '3':

            print("")
            print("Your Decimal: ", number)
            print("")

            loop2 = True

            hexaArrays = []

            fractional, integer = math.modf(number)
            number = integer / 16
            fractionaltimes = int(fractional * 16)

            if fractionaltimes == 10:

                hexaArrays.append("A")

            elif fractionaltimes == 11:

                hexaArrays.append("B")

            elif fractionaltimes == 12:

                hexaArrays.append("C")

            elif fractionaltimes == 13:

                hexaArrays.append("D")

            elif fractionaltimes == 14:

                hexaArrays.append("E")

            elif fractionaltimes == 15:

                hexaArrays.append("F")

            else:

                hexaArrays.append(fractionaltimes)

            while loop2:

            # Seperators
                fractional, integer = math.modf(number)

                number = integer / 16

                fractionaltimes = int(fractional * 16)
    
                print(int(integer), "R -", fractionaltimes)
    

                if fractionaltimes == 10:

                    hexaArrays.append("A")

                elif fractionaltimes == 11:

                    hexaArrays.append("B")

                elif fractionaltimes == 12:

                    hexaArrays.append("C")

                elif fractionaltimes == 13:

                    hexaArrays.append("D")

                elif fractionaltimes == 14:

                    hexaArrays.append("E")

                elif fractionaltimes == 15:

                    hexaArrays.append("F")

                else:

                    hexaArrays.append(fractionaltimes)

                if number <= 0:

                    break

                else:

                    loop2 = True


            hexaArrays.reverse()

            if hexaArrays:

                hexaArrays.pop()

                resultArrays = "".join(map(str, hexaArrays))

                print("")
                print("Hexadecimal: ",resultArrays)
                print("")

                input("Press Enter")

        elif choose == '4':

            number1 = number

            number2 = number

            number3 = number

            print("")
            print("Your Decimal: ", number)
            print("")

            binary_digits = []

            hexaArrays = []

            octalArrays = []

            # Binary----------------------------------------------------
            print("---Binary---")

            # Seperators
            fractional, integer = math.modf(number1)

            number1 = integer / 2

            # Result and Ramainders
            combined1 = float(integer + fractional)

            if combined1 != integer:

                binary_digits.append("1")

            else:

                binary_digits.append("0")

            loop0 = True

            loop9 = True

            loop8 = True

            while loop0:
                # Seperators
                fractional, integer = math.modf(number1)

                number1 = integer / 2

                # Result and Ramainders
                combined1 = float(integer + fractional)

                if combined1 != integer:

                    print(float(combined1), "- R 1")

                    binary_digits.append("1")

                else:

                    print(float(combined1), "- R 0")

                    binary_digits.append("0")

                if number1 <= 0:

                    break

                else:

                    loop0 = True

            binary_digits.reverse()

            if binary_digits:

                binary_digits.pop()


                binary_represent1 = ''.join(binary_digits)

                print("")
                print("Binary: ", binary_represent1)
                print("")

            # Octal------------------------------------------------------------

            print("---Octal---")

            fractional, integer = math.modf(number2)
            number2 = integer / 8
            fractionaltimes = int(fractional * 8)

            octalArrays.append(fractionaltimes)

            while loop9:

                # Seperators
                fractional, integer = math.modf(number2)

                number2 = integer / 8

                fractionaltimes = int(fractional * 8)

                # Result and Ramainders
                combined1 = float(integer + fractional)
                print(float(combined1),"R -", int(fractionaltimes))

                octalArrays.append(fractionaltimes)

                if number2 <= 0:

                    break

                else:

                    loop = True


            octalArrays.reverse()

            if octalArrays:

                octalArrays.pop()

                resultArrays = "".join(map(str, octalArrays))

                print("")
                print("Octal: ",resultArrays)
                print("")




            # Hexadecimal---------------------------------------------------------

            print("---Hexadecimal---")

            fractional, integer = math.modf(number3)
            number3 = integer / 16
            fractionaltimes = int(fractional * 16)

            if fractionaltimes == 10:

                hexaArrays.append("A")

            elif fractionaltimes == 11:

                hexaArrays.append("B")

            elif fractionaltimes == 12:

                hexaArrays.append("C")

            elif fractionaltimes == 13:

                hexaArrays.append("D")

            elif fractionaltimes == 14:

                hexaArrays.append("E")

            elif fractionaltimes == 15:

                hexaArrays.append("F")

            else:

                hexaArrays.append(fractionaltimes)

            while loop8:

                # Seperators
                fractional, integer = math.modf(number3)

                number3 = integer / 16

                fractionaltimes = int(fractional * 16)
                    
                print(int(integer), "R -", fractionaltimes)
                    

                if fractionaltimes == 10:

                    hexaArrays.append("A")

                elif fractionaltimes == 11:

                    hexaArrays.append("B")

                elif fractionaltimes == 12:

                    hexaArrays.append("C")

                elif fractionaltimes == 13:

                    hexaArrays.append("D")

                elif fractionaltimes == 14:

                    hexaArrays.append("E")

                elif fractionaltimes == 15:

                    hexaArrays.append("F")

                else:

                    hexaArrays.append(fractionaltimes)

                if number3 <= 0:

                    break

                else:

                    loop = True


            hexaArrays.reverse()

            if hexaArrays:

                hexaArrays.pop()

                resultArrays = "".join(map(str, hexaArrays))

                print("")
                print("Hexadecimal: ",resultArrays)
                print("")

                input("Press Enter")


        else:

            break


def main():
    print("")
    print("Input Personal Information")
    print("")
    fname = input("Enter your First Name: ")
    arraysForFname.append(fname)
    print("")
    mname = input("Enter your Midlle Name: ")
    arraysForMname.append(mname)
    print("")
    lname = input("Enter your Last Name: ")
    arraysForLname.append(lname)
    print("")
    age = int(input("Enter your Age: "))
    print("")
    ageBirth = int(2024 - age)
    arraysForAge.append(age)
    arraysForBirth.append(ageBirth)
    
    input("Press Enter to Confirm")

    fnameR = arraysForFname[0]

    mnameR = arraysForMname[0]

    lnameR = arraysForLname[0]

    ageR = arraysForAge[0]

    birthR = arraysForBirth[0]

    print("")

    print("-----------------------------------------------")

    print("Your Name: ", fnameR, mnameR, lnameR)

    print("Your Age: ", ageR, "Your Birth Year: ", birthR)

    print("-----------------------------------------------")

    choose()
    
main()
