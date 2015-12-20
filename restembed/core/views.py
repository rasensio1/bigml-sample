from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import pdb
import bigml.api

from .models import IrisPrediction
from bigml.api import BigML

def index(request):
  latest_prediction_list = IrisPrediction.objects.order_by('-created_at')[:5]
  context = {'latest_prediction_list': latest_prediction_list}
  return render(request, "core/index.html", context)

def new(request):
  api = BigML(dev_mode=True)

  req = request.POST
  sepal_l = req['sepal_l']
  sepal_w = req['sepal_w']
  petal_l = req['petal_l']
  model = "model/567620699ed233520200737a"

  pdb.set_trace()

  prediction = api.create_prediction(model, {'sepal length': sepal_l, 'sepal width': sepal_w, 'petal length': pteal_l})

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
