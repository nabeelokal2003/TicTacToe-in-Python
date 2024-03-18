print('Welcome to my Quiz Game!')

playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()
else:
    print("Okay! let's play!")
    score = 0

    answer = input('Q.1 : What does CPU stand for? ').lower()
    if answer == 'central processing unit':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')


    answer = input('Q.2 : What does GPU stand for? ').lower()
    if answer == 'graphics processing unit':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input('Q.3 : What does RAM stand for? ').lower()
    if answer == 'random access memory':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input('Q.4 : What does PSU stand for? ').lower()
    if answer == 'power supply':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    answer = input('Q.5 : What does ROS stand for? ').lower()
    if answer == 'robotics operating system':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    # print(f'You got {score} out of 5!')
    print('You got ' + str(score) + ' questions correct!')
