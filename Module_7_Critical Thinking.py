def courseInfo(courseKey):
    courseRooms = {"CSC101":3004,
                  "CSC102":4501,
                  "CSC103":6755,
                  "NET110":1244,
                  "COM241":1411}
    courseInstructors = {"CSC101":"Haynes",
                        "CSC102":"Alvarado",
                        "CSC103":"Rich",
                        "NET110":"Burke",
                        "COM241":"Lee"}
    courseTimes = {"CSC101":"8:00 a.m.",
                  "CSC102":"9:00 a.m.",
                  "CSC103":"10:00 a.m.",
                  "NET110":"11:00 a.m.",
                  "COM241":"1:00 p.m."}
    try:
        print('Room: ' + str(courseRooms[courseKey]))
        print('Instructor: ' + str(courseInstructors[courseKey]))
        print('Meeting Time: ' + str(courseTimes[courseKey]))
        return 'Complete'
    except:
        print('This is not an available course.')
        tryAgain = input('Would you like to try again? ')
        if tryAgain in('Yes','yes','YES','Y','y'):
            return 'try again'
        else:
            return 'Complete'
   

print('Avalable Courses:')
print('')
print('CSC101')
print('CSC102')
print('CSC103')
print('NET110')
print('COM241')
    
status = "try again"

while status == 'try again':
    searchedCourse = input('Enter a course to see its info: ')
    status = courseInfo(searchedCourse)