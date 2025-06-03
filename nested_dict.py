# Nested Dictionary

#1. Nested Dictionary: Nesting Dictionary means putting a
# dictionary inside another dictionary
# 2. it is a collection of dictionaries into one single dictionary

# create a Nested Dictionary


course={
    'php':{'duration':'2 Months','fees':10000},
    'django':{'duration':'3 Months','fees':15000},
    'java':{'duration':'4 Months','fees':20000},
}
print(course)
course['java']['fees']=25000
print(course['django'])

for k,v in course.items():
    print(k,v['duration'],v['fees'])