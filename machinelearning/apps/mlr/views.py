from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . models import Dataset
from django_pandas.io import read_frame
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

qs = Dataset.objects.all()
x = qs.to_dataframe(fieldnames=['luas_lahan','jumlah_pokok', 'jumlah_tbs', 'umur'])
y = qs.to_dataframe(fieldnames=['hasil_produksi'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

def MAPE(y_actual , y_pred):
    mape = np.mean(np.abs((y_actual - y_pred) / y_actual)) * 100 
    return mape

def MAD(y_actual , y_pred):
    n = len(y_actual)
    mad= np.mean(np.abs((y_actual - y_pred) / n ))
    return mad

actual = y_test.to_numpy()
predict = model.predict(x_test)

mape = MAPE(actual,predict)
mad = MAD(actual,predict) 

score = model.score(x_test, y_test)
R2 = "{0:.9f}%".format(100 * score)

coef = model.coef_
const = model.intercept_



@login_required
def dashboard(request):
    context = {
        'data':qs,
        'coef': coef,
        'const':float(const),
        'mape': mape,
        'mad': mad,
        'score': R2,
    }
    return render(request,'models/dashboard.html', context)

@login_required
def multiple(request):
    context = {
        'score': R2,
        'coef': coef,
    }
    return render(request,'models/multiple.html',context)

@login_required
def process(request):
    if request.method == 'POST':
        temp = {}
        temp['X1'] = request.POST.get('X1')
        temp['X2'] = request.POST.get('X2')
        temp['X3'] = request.POST.get('X3')
        temp['X4'] = request.POST.get('X4')
        # temp['X5'] = request.POST.get('X5')
        # temp['X6'] = request.POST.get('X6')
    testData = pd.DataFrame({'x':temp}).transpose()
    scorePredict = model.predict(testData)[0]

    context = {
        'scorePredict' : int(scorePredict),
        'temp': temp,
    }
    return render(request,'models/process.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        Dataset.objects.create(
            luas_lahan      = request.POST['X1'],
            jumlah_pokok    = request.POST['X2'],
            jumlah_tbs      = request.POST['X3'],
            umur            = request.POST['X4'],
            hasil_produksi  = request.POST['Y'],
        )
    # context = {
    #     'done':'dataset telah diperbaharui',
    # }
    return redirect('dashboard')


@login_required 
def cpo(request):
    return render(request, 'models/cpo.html')

@login_required
def kpo(request):
    return render(request, 'models/kpo.html')
