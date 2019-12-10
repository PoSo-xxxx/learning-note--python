#modules training
def bmi(w, h):
    return w/(h/100)**2
def showing():
    print('this is module testing!!!')

if __name__ == '__main__':
    height=float(input('Height(cm):'))
    weight=float(input('Weight(kg):'))
    print('BMI is:{:2.2f}'.format(bmi(weight, height)))