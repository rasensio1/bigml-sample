from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
import pdb
import bigml.api

from .models import IrisPrediction
from bigml.api import BigML

def index(request):
  latest_prediction_list = IrisPrediction.objects.order_by('-created_at')
  context = {'latest_prediction_list': latest_prediction_list}
  return render(request, "core/index.html", context)

def new_set(request):
  return render(request, "core/new_set.html")

def new(request):
  api = BigML(dev_mode=True)

  req = request.POST
  sepal_l = req['sepal_l']
  sepal_w = req['sepal_w']
  petal_l = req['petal_l']
  model = "model/567620699ed233520200737a"
  prediction = api.create_prediction(model, {'sepal length': sepal_l,
                                             'sepal width': sepal_w,
                                             'petal length': petal_l})

  prediction_name = prediction['object']['prediction'].get('000004')

  pred = IrisPrediction(sepal_length=sepal_l,
                        sepal_width=sepal_w,
                        petal_length=petal_l,
                        prediction=prediction_name,
                        created_at=timezone.now())

  pred.save()

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
