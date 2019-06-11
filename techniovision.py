import Techniovision


def inside_contest(faculty, file_name):
    f = open(file_name, 'r')
    study_programs = []
    student_idz = []
    for line in f:
        y = line.split(" ")
        if y[0] == 'staff' and y[-1] == faculty:
             study_programs =  y[2:len(y)-2]
             break
    votes = [0]*(len(study_programs))
    f.close()
    f = open(file_name, 'r')
    for line in f:
        x = line.split(" ")
        if x[0] == 'inside' and x[4] == faculty:
            if student_idz.count(x[2]) == 0:
                student_idz.append(x[2])
                for i, e in enumerate(study_programs):
                    if e == x[3]:
                        votes.insert(i, votes[i]+1)
                        
    votes[0]+=20
    maximum = max(votes)
    for i, e in enumerate(votes):
        if e == maximum:
            f.close()
            return study_programs[i]


def find_faculty(program, file_name):
    f = open(file_name, 'r')
    for line in f:
        x = line.split(" ")
        if x[0] == 'staff':
            for e in x:
                if e == program:
                    f.close()
                    return x[-1]


h = open('input.txt', 'r')
programs = []
system = Techniovision.TechniovisionCreate()
for line in h:
    z=line.split(" ")
    if z[0] == 'staff':
        programs.append(inside_contest(z[-1], 'input.txt'))

h.close()
h=open('input.txt', 'r')
for raw in h:
    y = raw.split(" ")
    if y[0] == 'techniovision':
            if y[2] in programs:
                curr_faculty = find_faculty(y[2], 'input.txt')
                Techniovision.TechniovisionStudentVotes(system, int(y[1]), str(y[-1][0:-1:1]), str(curr_faculty[0:-1:1]))
Techniovision.TechniovisionWinningFaculty(system)
h.close()
Techniovision.TechniovisionDestroy(system)


